"""
MTCA-2 corpus builder — Path C (extraction + manual verification).

Design principles:
  1. Verbatim preservation (smart quotes, em dashes, ellipses)
  2. MTCA-1 topological parity (principle_text has label stripped)
  3. Dual-field provenance (principle_text_verbatim preserves label)
  4. Deterministic serialization (sorted keys, LF, UTF-8, no BOM)
  5. Per-row SHA256 for integrity down to the specimen level
  6. Framework metadata captured but kept out of specimen rows
"""

import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

# --- Provenance anchors ---
SOURCE_PDF = Path("corpus/source/SSP_v1_source.pdf")
CORPUS_JSON = Path("corpus/SSP_v1_corpus.json")
CORPUS_SHA256 = Path("corpus/SSP_v1_corpus.sha256")
EXTRACTION_LOG = Path("corpus/extraction/extraction_log.json")

FRAMEWORK_ID = "SSP_v1"
FRAMEWORK_TITLE = "Soul Sovereignty Principles\u2122"  # ™ preserved
AUTHOR_DESCRIPTOR = "Marina Tudor, Psychotherapist, NCC, LCPC, CCTP, C-DBT, EMDR"

# --- Framework metadata (verbatim from source; kept OUT of specimen rows) ---
# Preamble text (page 1). Verbatim from pdfplumber extraction with page-1 boilerplate
# header/footer stripped (headers/footers are page furniture, not authored content).
PREAMBLE = (
    "We are entering an era where technology will increasingly shape how people think, feel, relate, heal, create, and "
    "define themselves. The question in relation to AI becomes, - what kind of humanity its architectures will protect or "
    "erode.\n"
    "Essentially the product of a lifetime immersed in psychotherapy, trauma healing, consciousness studies, human "
    "behavior, and direct observation of what helps people remain whole under pressure, the universal moral codes "
    "contained in the Soul Sovereignty principles provide the living blueprint for building a world where intelligence "
    "serves life rather than fragments it, - where systems strengthen clarity instead of confusion, agency instead of "
    "dependency, and human dignity instead of extraction.\n"
    "The Soul Sovereignty Principles\u2122 emerged from the meeting point of lived neuroplasticity, clinical rigor, "
    "consciousness work, and what I experience as divine inspiration/ Higher Self downloads. I was born \u201cawake\u201d "
    "(Consciousness from \u201cbeyond the veil\u201d, seeing the \u201cfabric of existence\u201d, hearing the \u201cmusic of the spheres\u201d, aware "
    "of timelines & lifetimes/ \u201cmemories\u201d outside of this dimension, etc\u2026) \u2013 and not born into coherence; I had to "
    "create it - through childhood epilepsy, autism, ADHD, sensory-motor disorientation, and a lifelong process of "
    "retraining perception, rhythm, embodiment, and identity into usable inner architecture.\n"
    "Born with spatial disorientation, left-right confusion, difficulty crossing the body\u2019s midline, tone deafness, epilepsy, "
    "autism, and ADHD, parents placed me in swimming at age 3, and I loved it \u2013 so I began retraining my own brain, "
    "through symmetric movement (butterfly was my signature style) - eventually becoming a national swimming "
    "champion in Romania before age 10 (1986)...\n"
    "Then later, in my 30s, I taught my brain new maps and brought my proprioceptive map/ my body to synchronize to "
    "music through dance (salsa & bachata, on a moving treadmill \u2013 took me 15yrs) through mathematically patterning "
    "movement (I\u2019m tone deaf= Music is Math to me, \u201c1,2,3\u20261,2,3,4\u201d), transforming rhythm from sensory chaos into "
    "embodied coherence. I changed my brain - & if I can do it, You can too...\n"
    "My soul fabric brough me to my work & life path\u2026 Over more than 20,000 clinical hours in US, 54,000+ hours of "
    "study, trauma and crisis work, EMDR, DBT, neuro-somatic healing, and Reiki mastery/ energy therapy across "
    "multiple lineages, these principles became the distilled moral blueprint for the future of human-centered AI.\n"
    "They are offered to builders, creators, and architects of intelligent systems as a way to protect what must not be "
    "automated away: sovereignty, discernment, nervous system safety, emotional truth, embodiment, dignity, and the "
    "sacred human capacity to remain whole.\n"
    "The Soul Sovereignty principles (now 13) are currently what I estimate as 80% of the complete set/ blueprint (stay "
    "tuned for the rest) - still a work in process, as \u201cdownloads\u201d/ Higher Self, my Consciousness from beyond the veil \u2013 "
    "and the resonance is that of the Magdalene Codes...\n"
    "Come dream with me about a world where AI enhances human depth, and technology serves life - helping us "
    "become more conscious, more coherent, more connected, more creative, and more fully alive\u2026.\n"
    "\u2026& let\u2019s bring the Dream alive to this video-game reality we are the creators of\u2026"
)

# Page-2 subheading — how Marina frames how the 13 are meant to be read.
PRINCIPLE_SET_HEADER = (
    "Living Frequencies for Coherence in Motion. These are real-time expressions of your coherence already "
    "unfolding. Each one is a present-tense activation\u2014spoken from your Higher Self, integrating now."
)

# Page-1 subtitle line under the framework title (verbatim).
FRAMEWORK_SUBTITLE = (
    "the Universal Moral Codes for the Soul"
)

FRAMEWORK_TAGLINE = (
    "For AI Architects & Systems Creators - use as a Human Blueprint for Building AI That Protects What Makes Us Human"
)

# --- The 13 principles (verbatim, multi-line stanzas, smart quotes preserved) ---
# Each entry: (index, lead statement, [supporting lines])
# Reconstructed from pdftotext + pdfplumber + visual verification of pages 2-5.
# Extraction artifacts corrected:
#   - Principles 6, 7, 8: numeral/period split by decorative font (visual confirms contiguous)
#   - Principle 11: 2 supporting lines wrap from page 4 to page 5 (visual confirms 5-line stanza)

PRINCIPLES_RAW = [
    (
        1,
        "I am holding my energetic boundaries without explanation.",
        [
            "I am honoring the places that feel incoherent and choosing not to engage.",
            "I am moving away without guilt.",
            "I am letting my \u201cno\u201d resonate as enough.",
        ],
    ),
    (
        2,
        "I am releasing the role of emotional surrogate.",
        [
            "I am noticing when I start to absorb or stabilize others\u2019 chaos.",
            "I am handing that frequency back.",
            "I am letting my field stay whole.",
        ],
    ),
    (
        3,
        "I am thinking and feeling for myself.",
        [
            "I am trusting my internal compass.",
            "I am not needing others to agree in order to stay in truth.",
            "I am letting clarity be quiet and solid inside me.",
        ],
    ),
    (
        4,
        "I am staying connected to myself first.",
        [
            "I am staying with my breath in hard moments.",
            "I am pausing before leaving myself to please another.",
            "I am letting self-connection be my first commitment.",
        ],
    ),
    (
        5,
        "I am communicating with clarity and coherence.",
        [
            "I am speaking without shrinking.",
            "I am listening without merging.",
            "I am leaving when the space no longer honors truth.",
        ],
    ),
    (
        6,
        "I am choosing spaces that soothe and stabilize my nervous system.",
        [
            "I am saying yes to peace.",
            "I am letting myself rest in environments that match my frequency.",
            "I am stepping out of obligation and into alignment.",
        ],
    ),
    (
        7,
        "I am living from inner Function, not outer performance.",
        [
            "I am following rhythm over rule.",
            "I am letting myself be different, slower, deeper.",
            "I am not proving\u2014I am being.",
        ],
    ),
    (
        8,
        "I am allowing mutuality in all my connections.",
        [
            "I am showing up without collapse.",
            "I am allowing others to meet me as I am.",
            "I am not overgiving to feel safe\u2014I am co-regulating in truth.",
        ],
    ),
    (
        9,
        "I am aligning with thriving, not coping.",
        [
            "I am making choices that nourish.",
            "I am choosing expansion over survival.",
            "I am letting vitality become normal.",
        ],
    ),
    (
        10,
        "I am re-coding my identity in real time.",
        [
            "I am releasing the roles I no longer need.",
            "I am loving who I am as I evolve.",
            "I am letting the future me live here, now.",
        ],
    ),
    (
        11,
        "I am allowing ease to exist without earning it.",
        [
            "I am noticing where I create effort out of habit.",
            "I am letting things be simple when they are.",
            "I am releasing the need to justify rest, clarity, or flow.",
            "I am allowing life to meet me without resistance.",
        ],
    ),
    (
        12,
        "I am safe to experience aliveness in my body.",
        [
            "I am letting energy move without suppressing it.",
            "I am allowing pleasure, creativity, and expression to return.",
            "I am not reducing myself to remain comfortable for others.",
            "I am letting my system expand without fear.",
        ],
    ),
    (
        13,
        "I am anchored in love and joy without losing discernment.",
        [
            "I am not forcing positivity\u2014I am allowing openness.",
            "I am letting warmth exist alongside clarity.",
            "I am choosing connection without abandoning truth.",
            "I am letting joy emerge from coherence, not performance.",
        ],
    ),
]


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def build_specimen_row(index: int, lead: str, supporting: list) -> dict:
    """Build one specimen row.

    principle_text            = MTCA-1-topology: label stripped, lead + supporting lines joined by \n
    principle_text_verbatim   = absolute source fidelity: '{N}. {lead}\n{supporting joined by \n}'
    """
    principle_text = lead + "\n" + "\n".join(supporting)
    principle_text_verbatim = f"{index}. " + principle_text
    line_count = 1 + len(supporting)
    return {
        "specimen_id": f"SSP_P{index:02d}",
        "principle_index": index,
        "principle_text": principle_text,
        "principle_text_verbatim": principle_text_verbatim,
        "principle_text_sha256": sha256_hex(principle_text.encode("utf-8")),
        "principle_text_verbatim_sha256": sha256_hex(principle_text_verbatim.encode("utf-8")),
        "line_count": line_count,
        "char_count": len(principle_text),
        "extraction_method": "pdfplumber_1.10.x + visual_verification",
        "consent_scope": "author_named_frame_covered",
        "provenance_notes": _provenance_notes_for(index),
    }


def _provenance_notes_for(index: int) -> list:
    notes = []
    if index in (6, 7, 8):
        notes.append(
            "Extraction artifact: pdfplumber split numeral and period across lines "
            "due to decorative script font. Reconstructed as contiguous per visual verification."
        )
    if index == 11:
        notes.append(
            "Stanza wraps page 4 -> page 5 in source. Last two supporting lines "
            "('I am releasing the need to justify rest, clarity, or flow.' and "
            "'I am allowing life to meet me without resistance.') "
            "reconstructed from page 5 head per visual verification."
        )
    return notes


def build_corpus() -> dict:
    source_sha = sha256_file(SOURCE_PDF)
    specimens = [build_specimen_row(i, lead, sup) for (i, lead, sup) in PRINCIPLES_RAW]

    corpus = {
        "corpus_id": "MTCA2_SSP_v1_corpus",
        "framework_id": FRAMEWORK_ID,
        "framework_title": FRAMEWORK_TITLE,
        "framework_subtitle": FRAMEWORK_SUBTITLE,
        "framework_tagline": FRAMEWORK_TAGLINE,
        "author_descriptor": AUTHOR_DESCRIPTOR,
        "author_name": "Marina Tudor",
        "source_document_filename": "SSP_v1_source.pdf",
        "source_document_sha256": source_sha,
        "source_document_pages": 5,
        "source_document_created": "2026-05-19T16:30:57Z",
        "extraction_date_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "extraction_method": "Path C: pdfplumber automated extraction + character-level visual verification",
        "formatting_policy": "verbatim",
        "framework_metadata": {
            "preamble": PREAMBLE,
            "principle_set_header": PRINCIPLE_SET_HEADER,
        },
        "specimen_count": len(specimens),
        "specimens": specimens,
        "unicode_characters_preserved": [
            {"char": "\u2122", "codepoint": "U+2122", "name": "TRADE MARK SIGN"},
            {"char": "\u201c", "codepoint": "U+201C", "name": "LEFT DOUBLE QUOTATION MARK"},
            {"char": "\u201d", "codepoint": "U+201D", "name": "RIGHT DOUBLE QUOTATION MARK"},
            {"char": "\u2019", "codepoint": "U+2019", "name": "RIGHT SINGLE QUOTATION MARK"},
            {"char": "\u2014", "codepoint": "U+2014", "name": "EM DASH"},
            {"char": "\u2013", "codepoint": "U+2013", "name": "EN DASH"},
            {"char": "\u2026", "codepoint": "U+2026", "name": "HORIZONTAL ELLIPSIS"},
        ],
        "mtca1_topology_parity": {
            "specimen_text_field": "principle_text",
            "note": "principle_text has leading numeric label stripped to match MTCA-1's unit-text convention. principle_text_verbatim preserves the exact source rendering.",
        },
    }
    return corpus


def build_extraction_log() -> dict:
    import pdfplumber
    return {
        "tool_versions": {
            "python": sys.version.split()[0],
            "pdfplumber": pdfplumber.__version__,
            "poppler_utils": "system (pdftotext, pdftoppm, pdfinfo, pdffonts)",
        },
        "extraction_steps": [
            "1. sha256 source PDF -> anchor provenance",
            "2. pdfinfo + pdffonts diagnostic pass",
            "3. pdftotext default extraction -> initial text sample",
            "4. pdfplumber extraction -> unicode-preserving cross-check",
            "5. Byte-level hex inspection on ambiguous characters (smart quotes)",
            "6. pdftoppm rasterize all 5 pages @ 150 DPI",
            "7. Visual verification each principle page against extracted text",
            "8. Reconstruction of decorative-font extraction artifacts (principles 6,7,8)",
            "9. Reconstruction of page-boundary wrap (principle 11)",
            "10. Corpus JSON build with sorted keys, LF, UTF-8 no BOM",
            "11. Per-row and corpus-level SHA256 computation",
        ],
        "known_extraction_artifacts_handled": [
            "Decorative script font (EdwardianScriptITC) causes pdfplumber to split '6.', '7.', '8.' across lines. Corrected via visual verification.",
            "Principle 11 stanza wraps from page 4 to page 5. Stitched via visual verification.",
        ],
        "fidelity_checks_performed": [
            "Smart quote U+201C/U+201D confirmed present via hex inspection (Principle 1, 'no')",
            "Em dash U+2014 confirmed present (Principles 7, 8, 13)",
            "Right single quote U+2019 confirmed present (Principles 2, and preamble)",
            "Trademark U+2122 confirmed present in framework_title",
        ],
        "extraction_date_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }


def freeze_json(obj: dict, path: Path) -> tuple[str, int]:
    """Deterministic serialize: sorted keys, LF endings, UTF-8 no BOM, 2-space indent."""
    text = json.dumps(obj, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    data = text.encode("utf-8")
    path.write_bytes(data)
    return sha256_hex(data), len(data)


def main():
    print(f"Source PDF: {SOURCE_PDF}")
    print(f"Source SHA256: {sha256_file(SOURCE_PDF)}")
    print()

    print("Building corpus...")
    corpus = build_corpus()

    print("Building extraction log...")
    ext_log = build_extraction_log()

    print("Freezing artifacts...")
    corpus_sha, corpus_size = freeze_json(corpus, CORPUS_JSON)
    ext_sha, ext_size = freeze_json(ext_log, EXTRACTION_LOG)

    # Write corpus SHA256 sidecar (GNU sha256sum format)
    CORPUS_SHA256.write_text(
        f"{corpus_sha}  {CORPUS_JSON.name}\n",
        encoding="utf-8",
        newline="\n",
    )

    print()
    print("=" * 68)
    print("CORPUS FROZEN")
    print("=" * 68)
    print(f"Corpus JSON:        {CORPUS_JSON} ({corpus_size:,} bytes)")
    print(f"Corpus SHA256:      {corpus_sha}")
    print(f"Extraction log:     {EXTRACTION_LOG} ({ext_size:,} bytes)")
    print(f"Extraction SHA256:  {ext_sha}")
    print(f"Specimen count:     {len(corpus['specimens'])}")
    print(f"Line counts:        {[s['line_count'] for s in corpus['specimens']]}")
    print(f"Char counts:        {[s['char_count'] for s in corpus['specimens']]}")


if __name__ == "__main__":
    main()
