#!/usr/bin/env python3
"""Detect updates to the legislation the privacy skill is based on.

For every source in legislation/sources.json it fetches the official text page,
fingerprints the *normalised visible text* (SHA-256), and compares it with the
recorded fingerprint. It then reports one status per instrument and, with
--write, updates the manifest and the human-readable status table in
skills/privacy-skill/references/legislation-status.md.

Detection is best-effort: official pages can change for formatting or navigation
reasons, and a change in fingerprint means "review the official text", not
"the law changed". Always confirm against the official register.

Usage:
    python scripts/check-legislation.py                # report only
    python scripts/check-legislation.py --write        # update timestamps/status
    python scripts/check-legislation.py --accept       # accept new text as baseline
    python scripts/check-legislation.py --offline      # no network; rebuild table
    python scripts/check-legislation.py --only eu-gdpr

Exit code: 0 = all current; 2 = updates available or an error occurred.
"""

from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import re
import sys
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
MANIFEST = REPO_ROOT / "legislation" / "sources.json"
STATUS_FILE = REPO_ROOT / "skills" / "privacy-skill" / "references" / "legislation-status.md"
# Files that carry a generated status table between the markers.
STATUS_TARGETS = [STATUS_FILE, REPO_ROOT / "README.md"]
USER_AGENT = "privacy-skill-legislation-check/1.0 (+https://github.com/)"

START_MARKER = "<!-- legislation-status:start -->"
END_MARKER = "<!-- legislation-status:end -->"


def today_utc() -> str:
    return datetime.datetime.now(datetime.timezone.utc).date().isoformat()


def normalise(body: bytes) -> bytes:
    """Reduce a fetched page to its visible text so dynamic markup does not
    cause false positives. Scripts/styles and tags are stripped; whitespace is
    collapsed."""
    text = body.decode("utf-8", "ignore")
    text = re.sub(r"(?is)<(script|style)\b.*?</\1>", " ", text)
    text = re.sub(r"(?s)<[^>]+>", " ", text)
    text = re.sub(r"&nbsp;?", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text.encode("utf-8")


def fingerprint(body: bytes) -> str:
    return hashlib.sha256(normalise(body)).hexdigest()


def fetch(url: str, timeout: int) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return response.read()


def check_source(source: dict, timeout: int, date: str, accept: bool, write: bool) -> str:
    """Return the new status for one source and update its fields in place."""
    if accept:
        write = True
    try:
        body = fetch(source["official_url"], timeout)
        digest = fingerprint(body)
    except Exception as exc:  # noqa: BLE001 - report any failure uniformly
        source["status"] = "error"
        source["error"] = f"{type(exc).__name__}: {exc}"
        return source["status"]

    source.pop("error", None)
    previous = source.get("fingerprint")

    if previous is None:
        status = "current"
        source["fingerprint"] = digest
        if not source.get("last_updated"):
            source["last_updated"] = date
    elif digest == previous:
        status = "current"
    else:
        status = "update-available"
        if accept:
            source["fingerprint"] = digest
            source["last_updated"] = date
            status = "current"

    source["status"] = status
    if write:
        source["last_checked"] = date
    return status


def render_status_markdown(sources: list[dict]) -> str:
    rows = [
        "| Instrument | Jurisdiction | Official text | Last checked (UTC) | Last updated (UTC) | Status |",
        "|---|---|---|---|---|---|",
    ]
    labels = {
        "current": "current",
        "update-available": "**update available**",
        "error": "check failed",
        "unverified": "unverified",
    }
    for source in sources:
        status = labels.get(source.get("status", "unverified"), source.get("status", ""))
        rows.append(
            "| {instrument} | {jurisdiction} | [{host}]({url}) | {checked} | {updated} | {status} |".format(
                instrument=source["instrument"],
                jurisdiction=source["jurisdiction"],
                host=re.sub(r"^https?://(www\.)?", "", source["official_url"]).split("/")[0],
                url=source["official_url"],
                checked=source.get("last_checked") or "-",
                updated=source.get("last_updated") or "-",
                status=status,
            )
        )
    table = "\n".join(rows)
    return (
        START_MARKER
        + "\n"
        + "_Status is maintained by `scripts/check-legislation.py`; run it to refresh._\n\n"
        + table
        + "\n"
        + END_MARKER
    )


def write_status_targets(sources: list[dict]) -> None:
    """Replace the generated block between the markers in each target file.

    The status file is created if missing; other targets are skipped (with a
    warning) if they do not already contain the markers."""
    block = render_status_markdown(sources)
    pattern = re.compile(re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER), re.S)
    for target in STATUS_TARGETS:
        if target.exists():
            content = target.read_text(encoding="utf-8")
            if pattern.search(content):
                target.write_text(pattern.sub(lambda _: block, content), encoding="utf-8")
            elif target == STATUS_FILE:
                target.write_text("# Legislation status\n\n" + block + "\n", encoding="utf-8")
            else:
                print(f"warning: no status markers in {target.relative_to(REPO_ROOT)}; skipped", file=sys.stderr)
        elif target == STATUS_FILE:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text("# Legislation status\n\n" + block + "\n", encoding="utf-8")


def save_manifest(data: dict) -> None:
    MANIFEST.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Detect updates to tracked privacy legislation.")
    parser.add_argument("--write", action="store_true", help="write manifest and status table")
    parser.add_argument("--accept", action="store_true", help="accept the fetched text as the new baseline")
    parser.add_argument("--offline", action="store_true", help="skip network access; rebuild the status table")
    parser.add_argument("--only", metavar="ID", help="only check the source with this id")
    parser.add_argument("--timeout", type=int, default=30, help="per-request timeout in seconds (default 30)")
    parser.add_argument("--date", default=today_utc(), help="date to record for 'last checked' (default: today UTC)")
    args = parser.parse_args(argv)

    # --accept rewrites the baseline, so it always implies writing.
    if args.accept:
        args.write = True

    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    sources = data["sources"]

    failed = False
    updates: list[str] = []
    for source in sources:
        if args.only and source["id"] != args.only:
            continue
        if args.offline:
            status = source.get("status", "unverified")
        else:
            status = check_source(source, args.timeout, args.date, args.accept, args.write)
        if status == "update-available":
            updates.append(source["id"])
            failed = True
        elif status == "error":
            failed = True
        marker = {"current": "ok", "update-available": "UPDATE", "error": "ERROR", "unverified": "?"}[status]
        print(f"[{marker:>6}] {source['id']:<24} {source.get('last_checked') or '-'}  {source['instrument']}")

    if updates:
        print("\nUpdates detected: " + ", ".join(updates))
        print("Review the official text, update the reference and top-level text, then re-run with --accept.")
    if any(s.get("status") == "error" for s in sources):
        print("\nSome sources could not be fetched (see 'error' in the manifest).")

    if args.write:
        save_manifest(data)
        write_status_targets(sources)
        print(f"\nWrote {MANIFEST.relative_to(REPO_ROOT)} and status table")

    return 2 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
