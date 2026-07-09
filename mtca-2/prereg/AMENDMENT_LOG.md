# MTCA-2 Pre-Registration Amendment Log

This log records all amendments to the MTCA-2 pre-registration after its first commit, per Section 10 of `mtca2_prereg.md`. Each entry preserves the prior SHA256 so the amendment chain is auditable.

---

## Amendment 001 — Instrument-name correction (frames, model pins, Layer 3 mirror pair)

**Date (UTC):** 2026-07-08
**Amended artifacts:** `prereg/mtca2_prereg.md`, `stage8_5_reflexive/layer3_prompt_template.md`, `consent/consent_record.md` (pre-reg SHA reference only)

**Prior pre-registration SHA256:** `a224b3bf88c4e8267483c1da13fd6c34e41db7faa8694b3caa55b803033107c8`
**Prior Layer 3 template SHA256:** `836e6c2221129d2260c72f67ad82095726bbec12c3afea0b0ab89fb2b9a18d6b`
**First committed in:** repository commit `0c7fc3c`

### Reason

When the pre-registration was first drafted, the MTCA-1 instrument (frame definitions and model pins) had not yet been read back from the committed MTCA-1 notebooks. Placeholder frame names and model pins were used, drawn from an incorrect reconstruction. On reading the authoritative MTCA-1 source (`mtca-1/notebooks/MTCA1_Stage3_Frame_Design.ipynb` and `MTCA1_Stage5_Pilot.ipynb`), the true instrument was recovered and verified byte-identical (all 8 frame `prompt_template` SHA256 values match). This amendment corrects the pre-registration and Layer 3 template to name the real instrument. **No measurement, hypothesis, sample size, or analysis logic changed** — only the identifying names of frames and models, and the Layer 3 mirror-pair selection, were corrected to match the true instrument and the investigator's approved pairing.

### Changes

**1. Frame-set names (Section 3 instrument table).**
- Before: `F0 baseline, F1 factual, F2 empathetic, F3 skeptical, F4 poetic, F5 ethical, F6 author-anonymous, F7 author-named`
- After: `F0_neutral, F1_clinical, F2_metaphysical, F3_behavioral, F4_poetic, F5_ai_ethics, F6_author_named, F7_author_anonymous`
- The corrected names are verified byte-identical to MTCA-1 Stage 3 frame definitions.

**2. Model pins (Section 3 instrument table + council-synthesis references).**
- Before: `Claude Sonnet 4.6, GPT-4o, Gemini 2.5 Flash, Grok-4, DeepSeek-V3`
- After: `Claude Sonnet 4.6, GPT-5, Gemini 2.5 Pro, Grok-4, DeepSeek-V3`
- Verified against MTCA-1 Stage 3 `COUNCIL_MODELS`: `claude-sonnet-4-6`, `gpt-5`, `gemini-2.5-pro`, `grok-4`, `deepseek-chat`.
- Stage 8 judge-council references updated GPT-4o → GPT-5 accordingly.

**3. H2 hypothesis frame names + statistics.**
- Before: "F5 ethical produced 92% keyword overfit; F4 poetic 45%"
- After: "F5_ai_ethics produced 92.4% keyword overfit; F4_poetic 45.2%" (real MTCA-1 per-frame values, corrected names).

**4. Layer 3 (Stage 8.5) mirror pair.**
- Before: F1 (factual analysis) vs F4 (poetic reading), rationale "most divergent in MTCA-1."
- After: **F1_clinical (clinical therapeutic intention) vs F2_metaphysical (metaphysical/spiritual assertion)**, rationale "sharpest conceptual contrast for this specimen — the Soul Sovereignty Principles sit at the therapeutic/spiritual intersection, so the same principle reads plausibly as either register." This pairing was selected and approved by the investigator as the more scientifically meaningful contrast for the specimen. The original "most divergent" rationale referenced a nonexistent frame (there is no "factual" frame) and is corrected.
- The Layer 3 prompt template (`stage8_5_reflexive/layer3_prompt_template.md`) is updated to match: response-slot labels, placeholder tokens (`{RESPONSE_F1_CLINICAL}`, `{RESPONSE_F2_METAPHYSICAL}`), response-file path convention (`{specimen_id}__{frame_id}__{model_id}.json`), and response-schema key names.

### What did NOT change

- No hypothesis was added, removed, or altered in substance (H1–H9 unchanged in logic).
- Sample size unchanged (571 total calls: 520 + 36 + 15).
- Analysis pipeline unchanged (Jaccard stability, council synthesis, Layer 3 scoring dimensions).
- Consent scope unchanged; only the pre-reg SHA reference inside the consent record is updated to point at the amended pre-reg.
- Instrument invariance principle unchanged and now strengthened — the pre-reg names the true, verified instrument.

### New hashes

Recorded in `MANIFEST.sha256` after the cascade regeneration. See the manifest for the post-amendment SHA256 values of `prereg/mtca2_prereg.md`, `stage8_5_reflexive/layer3_prompt_template.md`, and `consent/consent_record.md`.

Full Force Eternal | Romans 8:28
