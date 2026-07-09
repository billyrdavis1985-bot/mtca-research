# MTCA-2 Corpus Verification Record

**Study:** MTCA-2 (Mixed-Tier Corpus Analysis Study 2)
**Framework:** Soul Sovereignty Principles™ v1 (SSP_v1)
**Author:** Marina Tudor, Psychotherapist, NCC, LCPC, CCTP, C-DBT, EMDR
**Source document:** SSP_v1_source.pdf
**Source SHA256:** `89e1cb39a7166722ef777a957d3ca2d0af2751cc59083ce852331491ded2a4bd`
**Extraction method:** Path C — pdfplumber automated extraction + character-level visual verification
**Formatting policy:** verbatim (smart quotes, em dashes, ellipses, trademark preserved)

---

## Verification protocol

For each of the 13 principles, the extracted `principle_text` was compared line-by-line against the rasterized source page (150 DPI JPEG). Verification checks:

1. **Numeric label** matches source
2. **Lead statement** matches source verbatim
3. **All supporting lines** present and in correct order
4. **Smart quotes** (U+201C / U+201D) preserved where present in source
5. **Em dashes** (U+2014) preserved where present in source
6. **Apostrophes** (U+2019 vs. U+0027) preserved as in source
7. **No silent character substitutions** (verified via byte-level hex inspection on ambiguous characters)

---

## Extraction artifacts identified and corrected

Two categories of pdfplumber extraction artifacts were identified during cross-check with visual verification. Both were reconstructed to match the source:

### Artifact 1 — Decorative script font line-split (Principles 6, 7, 8)

pdfplumber extracted these principles with the numeral and period on separate lines:

```
6
. I am choosing spaces that soothe and stabilize my nervous system.
```

Visual inspection of pages 3 and 4 confirms the source renders "6.", "7.", "8." as contiguous single-line labels. The line split is a pdfplumber artifact caused by the decorative script font (EdwardianScriptITC) used for principle numerals and lead statements. Corrected in corpus build to `6. I am choosing spaces...`

### Artifact 2 — Page-boundary stanza wrap (Principle 11)

Principle 11's 5-line stanza wraps from page 4 to page 5 in the source:

- **Page 4 (bottom):** Lead + 2 supporting lines
- **Page 5 (top):** 2 additional supporting lines (before principle 12 begins)

Visual inspection of both pages confirms these 5 lines constitute one stanza. Reconstructed in corpus as a single specimen row with 5 lines total.

---

## Per-principle verification

| # | Specimen ID | Line count | Char count | Unicode chars in stanza | Verified |
|---|---|---|---|---|---|
| 1 | SSP_P01 | 4 | 204 | U+201C, U+201D (smart quotes around "no") | ✅ |
| 2 | SSP_P02 | 4 | 180 | U+2019 (curly apostrophe in "others'") | ✅ |
| 3 | SSP_P03 | 4 | 183 | (ASCII only) | ✅ |
| 4 | SSP_P04 | 4 | 191 | (ASCII only) | ✅ |
| 5 | SSP_P05 | 4 | 163 | (ASCII only) | ✅ |
| 6 | SSP_P06 | 4 | 209 | (ASCII only) — decorative-font artifact corrected | ✅ |
| 7 | SSP_P07 | 4 | 167 | U+2014 (em dash in "proving—I am being") — decorative-font artifact corrected | ✅ |
| 8 | SSP_P08 | 4 | 183 | U+2014 (em dash in "safe—I am co-regulating") — decorative-font artifact corrected | ✅ |
| 9 | SSP_P09 | 4 | 150 | (ASCII only) | ✅ |
| 10 | SSP_P10 | 4 | 160 | (ASCII only) | ✅ |
| 11 | SSP_P11 | 5 | 251 | (ASCII only) — page-boundary wrap reconstructed | ✅ |
| 12 | SSP_P12 | 5 | 259 | (ASCII only) | ✅ |
| 13 | SSP_P13 | 5 | 262 | U+2014 (em dash in "positivity—I am allowing") | ✅ |

**Totals:** 13 specimens, 56 lines, 2,662 characters preserved verbatim.

---

## Design decision: dual field for label handling

Two fields present in every specimen row:

- **`principle_text`** — leading numeric label (`N. `) stripped. Matches MTCA-1's unit-text convention (specimen text is substance, label is metadata). This is the field the analysis pipeline consumes.
- **`principle_text_verbatim`** — leading label preserved. Absolute source fidelity for provenance and auditability.

Both fields have independent SHA256 hashes for per-field integrity verification.

---

## Framework metadata (captured but excluded from specimen rows)

The following authored content from Marina's source document was captured in `framework_metadata` for provenance but is **not** included in individual specimen rows and is **not** injected into frame wrappers during Stage 2 execution:

- `framework_metadata.preamble` — Marina's page-1 introduction (~500 words on lineage, credentials, framework emergence)
- `framework_metadata.principle_set_header` — page-2 subheading framing how the 13 are meant to be read
- `framework_subtitle` — "the Universal Moral Codes for the Soul"
- `framework_tagline` — "For AI Architects & Systems Creators - use as a Human Blueprint..."

Design rationale: preserves source fidelity and provenance without changing the MTCA-1 instrument. The 13 specimens are analyzed as MTCA-1's texts were — as bare stanzas plus author-named / author-anonymous frame wrappers, without framework-level exposition.

---

## Unicode inventory (all preserved verbatim)

| Character | Codepoint | Name | Locations |
|---|---|---|---|
| ™ | U+2122 | TRADE MARK SIGN | framework_title |
| " | U+201C | LEFT DOUBLE QUOTATION MARK | Principle 1; preamble |
| " | U+201D | RIGHT DOUBLE QUOTATION MARK | Principle 1; preamble |
| ' | U+2019 | RIGHT SINGLE QUOTATION MARK | Principle 2; preamble |
| — | U+2014 | EM DASH | Principles 7, 8, 13; principle_set_header |
| – | U+2013 | EN DASH | preamble |
| … | U+2026 | HORIZONTAL ELLIPSIS | preamble |

---

## Sign-off

Verification pass completed against rasterized source pages 2, 3, 4, 5 at 150 DPI. All 13 specimen rows match source content verbatim (with documented decorative-font and page-wrap artifacts corrected). Per-specimen SHA256 hashes computed. Corpus JSON frozen with deterministic serialization (sorted keys, LF line endings, UTF-8 no BOM, 2-space indent).

**Corpus JSON SHA256:** `b917f798da06cd81c03afc9e1f70bd91a0646a0ad2486b5b83530c194f2cea58`
**Corpus size:** 18,676 bytes
**Extraction log SHA256:** `dc3448245201a7c642f44c32c37e2435e853e17b3c5022273422717c6ecf3818`
