#!/usr/bin/env python3
"""Validate the public M04 evidence catalogue. This is NOT a visual-security review."""
import csv
import hashlib
import re
from collections import Counter
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[2] / "bewijsvoering" / "M04-Network-Citadel"
EXPECTED = {"CONFIG": 120, "TROUBLESHOOT": 24, "ERROR": 12, "FIX": 8, "TEST": 56, "PASS": 35, "FAIL": 11, "PENDING": 4}
RFC1918 = {"10.0.0.0/8", "172.16.0.0/12", "192.168.0.0/16"}
IPV4 = re.compile(r"(?<![A-Za-z0-9_])(?:[0-9]{1,3}\.){3}[0-9]{1,3}(?:/[0-9]{1,2})?(?![A-Za-z0-9_])")
MAC = re.compile(r"(?<![A-Za-z0-9_])(?:[0-9A-Fa-f]{2}[:-]){5}[0-9A-Fa-f]{2}(?![A-Za-z0-9_])")
LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")

def fail(reason):
    raise SystemExit("FAIL: " + reason)

def load(path):
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))

def png_chunk_names(data):
    if not data.startswith(bytes([137, 80, 78, 71, 13, 10, 26, 10])):
        fail("bad PNG signature")
    pos, found = 8, []
    while pos < len(data):
        if pos + 12 > len(data):
            fail("bad PNG chunk header")
        size = int.from_bytes(data[pos:pos + 4], "big")
        kind = data[pos + 4:pos + 8].decode("ascii")
        if pos + size + 12 > len(data):
            fail("bad PNG chunk length")
        found.append(kind)
        pos += size + 12
    return found

def main():
    phases = sorted(p for p in ROOT.iterdir() if p.is_dir() and re.match(r"^[0-9]{2}_", p.name))
    if len(phases) != 19 or [int(p.name[:2]) for p in phases] != list(range(1, 20)):
        fail("expected 19 numbered phase folders")
    if any(not (p / "README.md").is_file() for p in phases):
        fail("phase README missing")

    rows = load(ROOT / "M04-EVIDENCE.csv")
    if len(rows) != 270 or {r["id"] for r in rows} != {f"M04-ZIP-{i:03d}" for i in range(1, 271)}:
        fail("wrong 270-record coverage")
    if dict(Counter(r["type"] for r in rows)) != EXPECTED:
        fail("status count drift")
    if Counter(r["image_status"] for r in rows) != {"BLOCKED_UNTIL_PIXEL_REVIEW": 269, "SOURCE_VIDEO_MISSING": 1}:
        fail("unapproved images marked public")

    crosswalk = load(ROOT / "M04-EVIDENCE-CROSSWALK.csv")
    if len(crosswalk) != 122 or len({r["m04_zip_id"] for r in crosswalk}) != 122:
        fail("crosswalk coverage or duplicate")
    if any(r["verification"] != "EXACT_FILENAME_AND_SOURCE_SHA256" for r in crosswalk):
        fail("crosswalk verification label")
    if any(r["m04_zip_id"] not in {x["id"] for x in rows} for r in crosswalk):
        fail("crosswalk missing source record")

    manifest = {}
    for line in (ROOT / "M04-SHA256SUMS.txt").read_text(encoding="utf-8").splitlines():
        if not line or line.startswith("#"):
            continue
        match = re.fullmatch(r"([a-f0-9]{64})  (.+)", line)
        if not match:
            fail("malformed public hash manifest")
        manifest[match.group(2)] = match.group(1)
    images = {p.relative_to(ROOT).as_posix(): p for p in ROOT.rglob("*.png")}
    if len(images) != 3 or set(images) != set(manifest):
        fail("unexpected number of public PNGs")
    for rel, path in images.items():
        data = path.read_bytes()
        if hashlib.sha256(data).hexdigest() != manifest[rel]:
            fail("PNG digest mismatch: " + rel)
        if any(chunk not in {"IHDR", "IDAT", "IEND"} for chunk in png_chunk_names(data)):
            fail("PNG metadata not stripped: " + rel)

    for p in ROOT.rglob("*"):
        if not p.is_file() or p.suffix.lower() not in {".md", ".csv", ".txt"}:
            continue
        body = p.read_text(encoding="utf-8")
        if any(value not in RFC1918 for value in IPV4.findall(body)):
            fail("unaliased IPv4 in " + str(p.relative_to(ROOT)))
        if MAC.search(body) or "fe80::" in body.lower():
            fail("unaliased MAC/IPv6 in " + str(p.relative_to(ROOT)))
        if p.suffix.lower() == ".md":
            for link in LINK.findall(body):
                if link.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                target = unquote(link.split("#", 1)[0])
                if target and not (p.parent / target).exists():
                    fail("broken Markdown link: " + str(p.relative_to(ROOT)) + " -> " + target)
    print("PASS: 19 phases, 270 evidence records, 122 crosswalk entries, 3 metadata-free SHA256 matched PNGs, local links and alias scan")
    print("WARNING: Automated tests cannot replace visual security review. The 269 newer original images remain blocked.")

if __name__ == "__main__":
    main()
