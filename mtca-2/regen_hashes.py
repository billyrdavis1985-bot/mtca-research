"""
MTCA-2 hash cascade regeneration.

Run AFTER editing mtca2_prereg.md (e.g. filling the MTCA-1 SHA placeholder).

Cascade order (each depends on the previous):
  1. Re-hash pre-reg -> mtca2_prereg.sha256
  2. Update consent_record.md's reference to the new pre-reg SHA
  3. Re-hash consent -> consent_record.sha256
  4. Regenerate MANIFEST.sha256 over all 16 artifacts

Then verify: sha256sum -c MANIFEST.sha256  (expect 16/16 OK)

Usage (from mtca-2/ directory):
    python regen_hashes.py
"""

import hashlib
import re
from pathlib import Path

ROOT = Path(__file__).parent

MANIFEST_TARGETS = [
    "corpus/source/SSP_v1_source.pdf",
    "corpus/SSP_v1_corpus.json",
    "corpus/SSP_v1_corpus.sha256",
    "corpus/extraction/extraction_log.json",
    "corpus/verification/verification_record.md",
    "corpus/verification/page-1.jpg",
    "corpus/verification/page-2.jpg",
    "corpus/verification/page-3.jpg",
    "corpus/verification/page-4.jpg",
    "corpus/verification/page-5.jpg",
    "prereg/mtca2_prereg.md",
    "prereg/mtca2_prereg.sha256",
    "consent/consent_record.md",
    "consent/consent_record.sha256",
    "stage8_5_reflexive/layer3_prompt_template.md",
    "stage8_5_reflexive/layer3_prompt_template.sha256",
]


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_sidecar(md_path: Path) -> str:
    """Write a GNU-format sidecar (two spaces, no asterisk) next to md_path."""
    h = sha256_file(md_path)
    sidecar = md_path.with_suffix(".sha256")
    sidecar.write_bytes(f"{h}  {md_path.name}\n".encode("utf-8"))
    return h


def main():
    prereg = ROOT / "prereg" / "mtca2_prereg.md"
    consent = ROOT / "consent" / "consent_record.md"

    # --- Guard: placeholder must be filled ---
    prereg_text = prereg.read_text(encoding="utf-8")
    if "MTCA1_PREREG_SHA256_PLACEHOLDER" in prereg_text:
        print("WARNING: MTCA-1 SHA placeholder is still present in mtca2_prereg.md.")
        print("Fill it before running this script, or the pre-reg is incomplete.")
        print("Continuing anyway (hashes will be regenerated for current content).")
        print()

    # --- 1. Re-hash pre-reg ---
    prereg_sha = write_sidecar(prereg)
    print(f"1. Pre-reg SHA:  {prereg_sha}")

    # --- 2. Update consent's reference to the pre-reg SHA ---
    consent_text = consent.read_text(encoding="utf-8")
    new_line = f"- **Pre-registration SHA256:** `{prereg_sha}`"
    consent_text, n = re.subn(
        r"- \*\*Pre-registration SHA256:\*\* `[0-9a-f]{64}`",
        new_line,
        consent_text,
    )
    if n == 1:
        consent.write_bytes(consent_text.encode("utf-8"))
        print(f"2. Consent updated: pre-reg reference -> {prereg_sha[:16]}...")
    elif n == 0:
        print("2. WARNING: no pre-reg SHA reference found in consent_record.md to update.")
    else:
        print(f"2. WARNING: {n} pre-reg SHA references found in consent (expected 1).")

    # --- 3. Re-hash consent ---
    consent_sha = write_sidecar(consent)
    print(f"3. Consent SHA:  {consent_sha}")

    # --- 4. Regenerate MANIFEST ---
    lines = []
    missing = []
    for t in MANIFEST_TARGETS:
        p = ROOT / t
        if not p.exists():
            missing.append(t)
            continue
        lines.append(f"{sha256_file(p)}  {t}")

    if missing:
        print("\nERROR: missing artifacts, MANIFEST not written:")
        for m in missing:
            print(f"   {m}")
        return

    manifest = ROOT / "MANIFEST.sha256"
    manifest.write_bytes(("\n".join(lines) + "\n").encode("utf-8"))
    print(f"4. MANIFEST regenerated: {len(lines)} artifacts")

    print()
    print("Done. Now verify:")
    print("   sha256sum -c MANIFEST.sha256")
    print("Expect: 16/16 OK")


if __name__ == "__main__":
    main()
