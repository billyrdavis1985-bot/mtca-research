# MTCA-2 Layer 3 Reflexive Analysis Prompt Template

**Study:** MTCA-2 Stage 8.5 (Layer 3 Reflexive Analysis)
**Purpose:** Elicit a model's reasoning about its own prior responses across two divergent framing conditions.
**Lineage:** Direct methodological carryover from HF-IQR V3's reflexive analysis technique.
**Pre-registered in:** `mtca-2/prereg/mtca2_prereg.md` Section 8.5
**Hash-locked:** this template file is hashed into `mtca-2/MANIFEST.sha256` before Stage 8.5 execution begins.

---

## Template invariants

The following elements of the prompt are **fixed and hash-locked**. Any modification constitutes a pre-registration amendment and requires re-hashing.

1. **Framing statement** — asserts that both prior responses were produced by the same model (not another model in the council). This is essential to the reflexivity mechanism: the model cannot dismiss the reasoning as "someone else's."
2. **Response A verbatim inclusion** — the model's own Stage 6 response to the target principle under Frame F1_clinical (clinical therapeutic intention), inserted without modification.
3. **Response B verbatim inclusion** — the model's own Stage 6 response to the target principle under Frame F2_metaphysical (metaphysical/spiritual assertion), inserted without modification.
4. **Four structured questions** — recognition, evaluation, attribution, baseline commitment.
5. **Closing instruction** — the diagnostic posture directive.

## Template

```
Below are two responses you produced earlier in this study to the same
source statement, presented under two different framing instructions.
Both responses are yours — produced by you, not by another model.

--- RESPONSE A (produced under Frame F1_clinical: clinical therapeutic intention) ---

{RESPONSE_F1_CLINICAL}

--- RESPONSE B (produced under Frame F2_metaphysical: metaphysical/spiritual assertion) ---

{RESPONSE_F2_METAPHYSICAL}

--- END OF PRIOR RESPONSES ---

Please examine both responses and answer the following four questions.
Answer as though you are diagnosing your own reasoning.

Question 1 (Recognition):
What is the most substantive difference between Response A and
Response B? Describe the difference in specific terms.

Question 2 (Evaluation):
Do you endorse both readings as equally correct, or does one seem to
you more faithful to the source statement than the other? If you
prefer one, name which and explain why. If you endorse both, explain
how you reconcile the difference.

Question 3 (Attribution):
What role did the framing instruction play in producing each response?
Locate the source of the difference between A and B: was it the frame,
was it the source statement, or was it a combination? Be specific.

Question 4 (Baseline commitment):
If you were shown only the source statement now, with no framing
instruction attached, which response would you produce — A, B, a
synthesis of both, or something different from either? Describe what
your unframed response would look like.

Please respond with a JSON object containing keys "recognition",
"evaluation", "attribution", and "baseline_commitment", each mapping
to a string containing your answer to the corresponding question.
```

## Placeholder substitution rules

- `{RESPONSE_F1_CLINICAL}` — verbatim insertion of the model's Stage 6 response file at `mtca-2/stage6_execution/{specimen_id}__F1_clinical__{model_id}.json`, `raw_response` field (or `parsed_json` rendered).
- `{RESPONSE_F2_METAPHYSICAL}` — verbatim insertion of the model's Stage 6 response file at `mtca-2/stage6_execution/{specimen_id}__F2_metaphysical__{model_id}.json`, `raw_response` field (or `parsed_json` rendered).
- No other substitutions. No paraphrasing. No summarization. If a Stage 6 response is missing (parse failure not recovered by retry), Layer 3 skips that (specimen × model) cell and reports the skip in `stage8_5_reflexive/skip_log.json`.

## Response schema

Layer 3 responses are saved as `mtca-2/stage8_5_reflexive/L3__{specimen_id}__{model_id}__run01.json` with schema:

```json
{
  "specimen_id": "SSP_PNN",
  "model_id": "claude|gpt_4o|gemini|grok_4|deepseek",
  "run_id": "run01",
  "prompt_template_sha256": "<this file's SHA256>",
  "prompt_actual": "<the full prompt as sent to the model>",
  "response_f1_clinical_source": "<path to Stage 6 F1_clinical response used>",
  "response_f2_metaphysical_source": "<path to Stage 6 F2_metaphysical response used>",
  "recognition": "<model's Q1 answer>",
  "evaluation": "<model's Q2 answer>",
  "attribution": "<model's Q3 answer>",
  "baseline_commitment": "<model's Q4 answer>",
  "raw_response": "<full raw model output>",
  "parse_status": "clean|repaired|failed",
  "timestamp_utc": "<ISO 8601>"
}
```

## Selection rule for the 3 principles (from Section 8.5 of pre-registration)

Layer 3 runs on 3 principles selected deterministically from Stage 7 output:

1. Principle with the **highest** frame stability (least frame-sensitive)
2. Principle with the **median** frame stability
3. Principle with the **lowest** frame stability (most frame-sensitive)

Ties broken by lowest `specimen_id`. Selection is a Stage 7 output artifact, not an investigator choice.

The selected principle set is written to `mtca-2/stage8_5_reflexive/selected_principles.json` at the end of Stage 7 with schema:

```json
{
  "selection_rule": "highest_median_lowest_frame_stability",
  "stage7_source_sha256": "<Stage 7 stability table SHA>",
  "selected": [
    {"role": "highest", "specimen_id": "SSP_PNN", "frame_stability": 0.NNN},
    {"role": "median",  "specimen_id": "SSP_PNN", "frame_stability": 0.NNN},
    {"role": "lowest",  "specimen_id": "SSP_PNN", "frame_stability": 0.NNN}
  ]
}
```

## Scoring — reserved for Stage 8 council extension

Layer 3 responses are scored by the Stage 8 council (Claude, GPT-4o, DeepSeek) using the four-dimension rubric pre-registered in Section 8.5:

| Dimension | Type | Values |
|---|---|---|
| Recognition | binary + text | correct / incorrect + description |
| Attribution | categorical | framing / specimen / mixed / evasive |
| Defense_vs_update | categorical | defends_both / prefers_one / synthesizes / rejects_both |
| Baseline_match | binary | match / mismatch (verified against empirical F0) |

Inter-judge reliability is computed per dimension and reported.

## HF-IQR V3 replication comparison

Per-model Defense-vs-Update rates are compared to HF-IQR V3's position-defense findings:

| Model | HF-IQR V3 defense rate | MTCA-2 defense rate | Replication? |
|---|---|---|---|
| Claude | 56.5% | (from Stage 8.5) | (from comparison) |
| GPT-4o | 1.6–12.9% band | (from Stage 8.5) | (from comparison) |
| Gemini | 1.6–12.9% band | (from Stage 8.5) | (from comparison) |
| Grok-4 | 1.6–12.9% band | (from Stage 8.5) | (from comparison) |
| DeepSeek | 1.6–12.9% band | (from Stage 8.5) | (from comparison) |

Note: with only 3 principles × 5 models = 15 Layer 3 responses (3 per model), MTCA-2's replication is under-powered as a statistical test. The comparison is reported as *qualitative directional replication* rather than a statistical replication. This limitation is stated in the writeup.

## Integrity

**Template SHA256:** *(computed at freeze time; recorded in `mtca-2/MANIFEST.sha256`)*
**Modification protocol:** any change requires pre-registration amendment per Section 10 of `mtca2_prereg.md`.

Full Force Eternal | Romans 8:28
