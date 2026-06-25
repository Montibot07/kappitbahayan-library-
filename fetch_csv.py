#!/usr/bin/env python3
"""
Fetches the Virtual Library CSV from Google Sheets
and saves it to docs/_data/library.csv for Jekyll to use.
"""

import urllib.request
import os
import sys

CSV_URL = (
    "https://docs.google.com/spreadsheets/d/e/"
    "2PACX-1vTwI8N3nm2-Ha1PD5TfNfeN3uT0N0aF0HAT597S1U5yzWWmvY2WXYyql8HUJo-nTIvRXQQ8-WYETOst"
    "/pub?gid=1986119007&single=true&output=csv"
)

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "..", "docs", "_data", "library.csv")

def fetch():
    print(f"Fetching: {CSV_URL}")
    req = urllib.request.Request(CSV_URL, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as response:
        data = response.read().decode("utf-8")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(data)

    lines = data.strip().splitlines()
    print(f"✓ Saved {len(lines) - 1} rows to {OUTPUT_PATH}")
    if lines:
        print(f"  Columns: {lines[0]}")

if __name__ == "__main__":
    try:
        fetch()
    except Exception as e:
        print(f"✗ Failed to fetch CSV: {e}", file=sys.stderr)
        sys.exit(1)
