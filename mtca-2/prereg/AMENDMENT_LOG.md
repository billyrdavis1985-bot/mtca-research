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

---

## Amendment 002 — Model-pin correction and pilot-verified token calibrations

**Date (UTC):** 2026-07-08
**Amended artifacts:** `prereg/mtca2_prereg.md`, `consent/consent_record.md` (pre-reg SHA reference only)

**Prior pre-registration SHA256:** `7c0f524072450028abac9a68f81ea0c0709d0a476f8c8fecda743c5e4e33c3c9` (Amendment 001 output; committed in `93bd993`)

### Reason

This amendment closes two gaps between the pre-registration and the actual instrument as executed in the Stage 5 pilot:

1. **Model-pin correction.** Amendment 001 corrected the model pins to `GPT-5` and `Gemini 2.5 Pro`, taken from the `COUNCIL_MODELS` block in `mtca-1/notebooks/MTCA1_Stage3_Frame_Design.ipynb`. Those notebook values were draft/aspirational and never matched the actual MTCA-1 run. The MTCA-2 pilot surfaced this immediately: `gpt-5` returned instant API errors (invalid model string) and `gemini-2.5-pro` hung. The authoritative source of the real instrument is the MTCA-1 **response records** (`mtca-1/stage6_execution/responses/*.json`), which record the exact `api_model` string that produced each of the 2,000 responses. Reading those records directly established the true pins.

2. **Per-model token calibrations.** The pilot's first iteration showed that MTCA-1's uniform `MAX_OUTPUT_TOKENS = 800` does not produce complete responses on the current SDK versions for two of the five models:
   - **Claude Sonnet 4.6** truncated mid-JSON on F6_author_named at 800 tokens with `stop_reason = max_tokens` (708 tokens visible, response cut off in the fifth key's array). Bumping to 2000 tokens produced complete parseable JSON.
   - **Gemini 2.5 Flash** on `google-generativeai == 0.8.6` failed 0/8 in the first pilot run. Diagnostic showed `finish_reason = 2` (MAX_TOKENS) with `total_token_count = 875` but only 130 visible-answer tokens — ~666 tokens consumed by an internal thinking budget that is not disable-able in this SDK version. The pilot verified that raising the Gemini limit to 8000 and setting `response_mime_type = 'application/json'` restored complete parseable output (8/8 in the corrected pilot).

The final pilot with both calibrations returned **40/40 clean parses**, verifying the corrected instrument end-to-end.

### Real instrument (from MTCA-1 response records + pilot verification)

| model_id | api_model | max_tokens (Stage 6) |
|---|---|---|
| claude_sonnet_4_6 | `claude-sonnet-4-6` | **2000** (was 800; pilot-verified) |
| gpt_4o | `gpt-4o` | 800 (unchanged) |
| gemini_2_5_flash | `gemini-2.5-flash` | **8000** + `response_mime_type='application/json'` (was 800; pilot-verified) |
| grok_4 | `grok-4` | 800 (unchanged) |
| deepseek_v3 | `deepseek-chat` | 800 (unchanged) |

### Changes

**Model-pin corrections:**
- Section 3 instrument table: `GPT-5, Gemini 2.5 Pro` → `GPT-4o, Gemini 2.5 Flash`
- Stage 8 judge-council references: `GPT-5` → `GPT-4o` (Section 2, Section 8, Layer 3 scoring text)

**Token calibrations (added to Section 7 execution parameters):**
- New "Per-model token calibrations" subsection detailing the Claude 2000-token and Gemini 8000-token / JSON-mime-type adjustments
- New "Rationale for invariance preservation" subsection explaining why these calibrations preserve rather than change the instrument (they restore MTCA-1's completion behavior on current SDKs; an 800-token cap on the current Gemini SDK would produce systematically truncated output that MTCA-1 never had)

### Rationale for invariance framing

MTCA-1's Gemini responses achieved 96.5% parse rate with output lengths up to 1132 tokens on the 800 limit — the SDK at that time treated `max_output_tokens` as a soft cap. The current `google-generativeai == 0.8.6` SDK treats it as a hard cap and additionally consumes an unbounded thinking budget from within it. Preserving the *nominal* 800 limit on the new SDK produces truncated responses that MTCA-1 never had. Preserving MTCA-1's *actual completion behavior* — full parseable JSON with all 5 required keys — requires giving Gemini enough budget to reach that behavior. The 8000 budget matches the observed thinking-plus-answer envelope with margin. The same reasoning applies to Claude's calibration: MTCA-1 never hit the 800 ceiling because its public-domain corpus elicited shorter responses than Marina's contemporary framework does. Bumping Claude to 2000 restores the same "completes without truncation" behavior on the SSP specimen.

### What did NOT change

- No hypothesis added, removed, or altered in logic (H1–H9 unchanged).
- Sample size unchanged (571 total calls: 520 Stage 6 + 36 Stage 8 + 15 Stage 8.5).
- Frame definitions unchanged (all 8 remain byte-identical to MTCA-1 Stage 3).
- Parser unchanged (5-key JSON schema, same tolerant-of-fences extractor).
- Analysis pipeline unchanged (Jaccard stability, council synthesis pattern, Layer 3 scoring dimensions).
- Consent scope unchanged; only the pre-reg SHA reference inside the consent record is updated to point at the amended pre-reg.

### Pilot evidence

Amendment 002 is directly evidenced by the committed pilot artifact (`mtca-2/stage5_pilot/responses/`, commit `5266972`):
- 40 pilot response files record `api_model` values `claude-sonnet-4-6`, `gpt-4o`, `gemini-2.5-flash`, `grok-4`, `deepseek-chat` — the corrected pins
- Every response has `parse_succeeded = true` — verifying the corrected token limits produce complete parseable output
- Pilot manifest hash-anchors the artifact into the reproducibility trail

### Lessons recorded

1. Notebook config blocks are not authoritative for what executed — the response records are.
2. SDK version drift between studies can change instrument behavior even when code and configuration are byte-identical. Invariance requires calibrating to preserve *behavior*, not just *configuration values*.
3. Pilot-first execution surfaces both problems within budget (~$0.15) and before the full run commits ~$2 to hash-anchored measurements.

### New hashes

Recorded in `MANIFEST.sha256` after cascade regeneration.

Full Force Eternal | Romans 8:28
