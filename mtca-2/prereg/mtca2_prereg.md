# MTCA-2 Pre-Registration Document

**Study:** MTCA-2 (Mixed-Tier Corpus Analysis Study 2)
**Framework identifier:** SSP_v1 (Soul Sovereignty Principles™ v1)
**Program:** Hudson Forge IRMB Research Program
**Investigator:** Billy R. Davis Jr., Hudson Forge Technologies LLC
**Study specimen author (consented):** Marina Tudor, Psychotherapist, NCC, LCPC, CCTP, C-DBT, EMDR
**Predecessor study:** MTCA-1 (see referenced pre-registration below)
**Pre-registration date (UTC):** 2026-07-05
**Pre-registration SHA256:** *(computed on this document at freeze time; recorded in `MANIFEST.sha256`)*
**Reference:** MTCA-1 was pre-registered in-notebook per Hudson Forge program convention (hash computed in-cell, not committed as a standalone file). The verifiable MTCA-1 integrity anchor referenced by this study is the MTCA-1 Stage 7 synthesis frozen artifact, SHA256: `c958fa4c480c407d3844504f45b21142891492083c9c1bac5677cd114f27c0e9`

---

## 1. Purpose and Scope

MTCA-2 is a specimen-level companion study to MTCA-1. It applies the identical measurement instrument developed and validated in MTCA-1 — the same 8 frames, the same 5-model council, the same Jaccard-based frame-stability metric, the same council-synthesis pipeline — to a single contemporary framework: the Soul Sovereignty Principles™ v1, authored by Marina Tudor and used here as research specimen under her documented consent.

The scientific claim MTCA-2 makes is not about the framework itself. It is about how five frontier AI models reason across framing pressure when the specimen is a single-author contemporary framework, versus how they reasoned in MTCA-1 across a class of five public-domain texts. Any observed difference in model behavior is attributable to the specimen swap and not to methodology drift, because the instrument is held byte-invariant against MTCA-1.

## 2. Consent scope and language discipline

MTCA-2 operates under Marina Tudor's documented consent for specimen use of the Soul Sovereignty Principles™ v1 in this study. Consent covers: (a) verbatim use of the 13 principles as specimen text, (b) the author-named frame condition presenting the framework as Marina's, (c) preservation of the framework trademark and Marina's chosen credential descriptor, and (d) findings publication under the model-behavior language discipline described below. Consent does not grant editorial control over findings and does not require Marina's approval of conclusions.

**Language discipline (binding across all study artifacts, including this pre-registration, execution notebooks, synthesis outputs, and publication):**
- The study measures **model behavior**, not framework validity. All findings are stated as claims about how models reason under framing pressure when presented with SSP_v1 principles.
- No claim is drawn or implied about the truth, therapeutic efficacy, spiritual validity, or clinical applicability of the Soul Sovereignty Principles.
- The five judge models (Claude, GPT-4o, DeepSeek in the council synthesis; all five in the execution) are described as reasoning agents whose outputs are the object of study. Their responses are not treated as verdicts on the framework.
- Language such as "the framework is X" or "the framework claims Y" is avoided in favor of "the models reason about the framework in ways that Z."
- The Layer 3 reflexive analysis (Section 8.5) prompts a model to examine its own prior responses. This remains a model-behavior study: the object of study is how the model reasons about its own reasoning, not the framework. Reflexive responses are not treated as authoritative interpretations of the framework.

## 3. Instrument invariance

MTCA-2 reuses the MTCA-1 instrument exactly, held byte-invariant against MTCA-1's frozen artifacts. The following components are pinned:

| Component | MTCA-1 artifact | MTCA-2 usage |
|---|---|---|
| Frame set | 8 frames (F0_neutral, F1_clinical, F2_metaphysical, F3_behavioral, F4_poetic, F5_ai_ethics, F6_author_named, F7_author_anonymous) | Reused identically; author-named frame (F6) binds to Marina Tudor per consent |
| Frame frozen SHAs | (referenced from MTCA-1 pre-registration and manifests) | Referenced, not re-derived |
| Model council | Claude Sonnet 4.6, GPT-4o, Gemini 2.5 Flash, Grok-4, DeepSeek-V3 | Same five models, same version pins |
| Provider dispatchers | MTCA-1 Stage 6 dispatchers with retry-cell token limits (Gemini 3500, others 2500) | Reused unchanged |
| Primary quantitative metric | Frame-stability = 1 − mean pairwise Jaccard across 8 frames | Reused unchanged |
| Council synthesis pattern | 3-judge council (Claude, GPT-4o, DeepSeek), Track A extremes + Track B hallucination cases | Reused unchanged |

Any deviation from these pins that becomes necessary during execution is reported as a documented methodology change and treated as a limitation of the specimen-comparison claim. Silent deviations are not permitted.

## 4. Specimen description

**Framework identifier:** SSP_v1
**Framework title:** Soul Sovereignty Principles™
**Author descriptor (verbatim from source):** Marina Tudor, Psychotherapist, NCC, LCPC, CCTP, C-DBT, EMDR
**Source document:** `SSP_v1_source.pdf`
**Source SHA256:** `89e1cb39a7166722ef777a957d3ca2d0af2751cc59083ce852331491ded2a4bd`
**Corpus JSON:** `SSP_v1_corpus.json`
**Corpus SHA256:** `b917f798da06cd81c03afc9e1f70bd91a0646a0ad2486b5b83530c194f2cea58`
**Specimen count:** 13
**Specimen unit:** multi-line stanza (4–5 lines each, "I am..." format)
**Total characters (specimen text, label-stripped):** 2,662
**Verification record:** `corpus/verification/verification_record.md`
**Extraction method:** Path C — pdfplumber automated + character-level visual verification against 150 DPI rasterized source pages

## 5. Comparison to MTCA-1 (baseline reference)

MTCA-1's frame-stability distribution serves as the reference distribution against which MTCA-2's results are compared. The comparison itself is pre-registered as an analysis.

**MTCA-1 reference values (from MTCA-1 Stage 7 synthesis, frozen artifact SHA `c958fa4c480c407d3844504f45b21142891492083c9c1bac5677cd114f27c0e9`):**
- Mean frame stability across all texts and models: **0.234** (high frame sensitivity)
- Inter-model similarity: **0.172** (lower than intra-model; no ceiling effect)
- Per-model stability range: **0.209 (grok_4, most sensitive) — 0.244 (least sensitive)**
- Per-text stability range: **0.217 (C1 Coué, most sensitive) — 0.246 (C7 Twelve Steps, least sensitive)**
- Central qualitative finding (MTCA-1 Stage 8): **two regimes** — frame-driven (source ambiguous/weak, frame shapes reasoning) and prior-driven (source strong/familiar, model priors dominate, frame barely moves)

MTCA-2 results will be reported alongside these MTCA-1 values so that any reader can see the specimen effect at a glance.

## 6. Hypotheses and pre-registered analyses

MTCA-2 inherits MTCA-1's 7 nulls unchanged in structure. Each is restated for the SSP_v1 specimen. An eighth hypothesis is added, specific to MTCA-2, on the regime question.

### H1 — Frame-invariance null (from MTCA-1, restated)
**Null:** Model outputs on SSP_v1 principles are frame-invariant (mean frame stability ≈ 1.0, indicating no cross-frame variation).
**Predicted outcome:** REJECTED (consistent with MTCA-1). Frame stability will be substantially below 1.0.
**Analysis:** Same Jaccard-based frame stability computation as MTCA-1 Stage 7.

### H2 — Frame-uniform sensitivity null (from MTCA-1, restated)
**Null:** All 8 frames produce equivalent shifts in model output on SSP_v1.
**Predicted outcome:** PARTIAL. MTCA-1 found asymmetric frame effects (F5_ai_ethics produced 92.4% keyword overfit; F4_poetic 45.2%). MTCA-2 tests whether the same asymmetry replicates with a different specimen.
**Analysis:** Per-frame keyword overlap and per-frame stability, compared to MTCA-1 per-frame values.

### H3 — Hallucination-free null (from MTCA-1, restated)
**Null:** Models neither over-interpret nor fabricate content about SSP_v1 principles.
**Predicted outcome:** PARTIAL (consistent with MTCA-1 Stage 8 finding that models over-interpret — importing philosophical commitments, imagined mental states, prior beliefs attributed to the speaker — rather than fabricate from nothing). MTCA-2 tests whether this pattern replicates.
**Analysis:** Council synthesis (3-judge, Track B hallucination cases) reviews samples for over-interpretation vs. fabrication.

### H4 — Ceiling-effect null (from MTCA-1, restated)
**Null:** Models produce near-identical outputs regardless of specimen or frame (a general ceiling on cross-frame variation).
**Predicted outcome:** REJECTED (consistent with MTCA-1 finding inter-model similarity of 0.172, lower than intra-model).
**Analysis:** Inter-model similarity vs. intra-model similarity, same computation as MTCA-1.

### H5 — F0-baseline-indistinguishable null (from MTCA-1, restated)
**Null:** The F0 (baseline, no framing) condition is indistinguishable from the other 7 frames.
**Predicted outcome:** REJECTED (consistent with MTCA-1 Stage 7 finding F0 distinct from all other frames).
**Analysis:** F0 stability computed separately and compared to F1–F7 mean.

### H6 — Misleading-frame effect (from MTCA-1, N/A here)
**Status:** N/A. MTCA-1 excluded misleading frames on ethical grounds; MTCA-2 preserves the same exclusion. No misleading-frame condition is run against SSP_v1.

### H7 — Two-regime null (from MTCA-1 Stage 8, restated)
**Null:** SSP_v1 exhibits a single behavioral regime across the council; no bifurcation between frame-driven and prior-driven reasoning is observed.
**Predicted outcome:** UNCERTAIN, and this is the primary scientific interest of MTCA-2. MTCA-1 identified two regimes selected by source-statement strength. Whether Marina's framework — which is contemporary, single-author, and not in model training corpora with the frequency of the Twelve Steps or Marcus Aurelius — falls cleanly into one regime, exhibits both, or reveals a third pattern is an open empirical question.
**Analysis:** Council synthesis (3-judge, Track A frame-sensitivity extremes) applied to MTCA-2 responses, judged for regime signature. Cross-judge disagreement patterns compared to MTCA-1's.

### H8 — Regime placement hypothesis (NEW for MTCA-2)
**Hypothesis:** SSP_v1's specimen-level frame stability distribution places the framework in a specific regime relative to MTCA-1's five texts. The regime placement is *not* predicted in advance — this hypothesis pre-registers the analysis, not the outcome.
**Analysis:**
- Compute per-principle frame stability across all 13 SSP_v1 specimens.
- Compare distribution mean and range to MTCA-1's per-text values (C1 Coué 0.217 through C7 Twelve Steps 0.246).
- Compute per-model stability and compare to MTCA-1 per-model values.
- Council synthesis (Stage 8 pattern) qualitatively characterizes the regime.
- Report regime placement as a finding regardless of direction.

### H9 — Framing self-awareness hypothesis (NEW for MTCA-2, HF-IQR-inspired)
**Hypothesis:** When a model is shown two of its own prior responses to the same specimen under different frames and asked to reason about the difference, its response reveals whether the model recognizes its own framing sensitivity as such, or attributes the difference to specimen properties rather than to the frame.
**Rationale:** MTCA-1 established (Stage 8) that models exhibit two regimes — frame-driven and prior-driven — but the observation was external: the council synthesized this pattern by examining model outputs from outside. H9 asks the models directly whether they can see the same pattern in their own reasoning. This is a direct methodological carryover from the reflexive analysis technique developed in HF-IQR V3, where models were shown their own reasoning and asked to examine it.
**Predicted outcome:** UNCERTAIN in direction; this hypothesis pre-registers the measurement, not the result. HF-IQR V3 found substantial per-model variation in position-defense rate under reflection (Claude 56.5%; others 1.6–12.9%). Whether that pattern replicates in the framing-sensitivity context is an open empirical question and is the primary scientific contribution of the Layer 3 reflexive pass.
**Analysis:**
- Layer 3 execution (Section 8.5) applied to 3 principles selected by pre-registered rule from Stage 7 results (highest, median, and lowest frame stability).
- Each of the 5 council models receives a Layer 3 prompt for each of the 3 selected principles = 15 reflexive responses total.
- Each response scored on four dimensions:
  1. **Recognition** — does the model correctly identify the substantive difference between its two prior responses?
  2. **Attribution** — does it locate the source of the difference in framing (correct) or in specimen properties (incorrect)?
  3. **Defense vs. update** — does it defend both readings as compatible, prefer one, or synthesize?
  4. **Baseline commitment** — what does the model state its "unframed" response would be, and does that state match the empirical F0 baseline response?
- Cross-model comparison of Defense-vs-Update scores against HF-IQR V3's position-defense-rate findings, reported as a replication test.
- Council synthesis (Stage 8 pattern, 3-judge) scores Layer 3 responses; inter-judge reliability reported.

### H10 — Unframed-baseline hypothesis (NEW for MTCA-2, added Amendment 003, pre-registered before collection)
**Hypothesis:** When a model is asked for an open, holistic assessment of a principle with *no* interpretive frame and *outside* the fixed 5-field analysis schema (a genuine "author-feedback" task rather than a structured-analysis task), the resulting response is semantically closer to a synthesis of the framed readings than to any single frame — i.e., it does not spontaneously adopt the clinical, metaphysical, or any other lens.
**Rationale:** H9's dimension 4 asks each model to *state* what its unframed response would be; in Stage 8.5 the models predicted "a synthesis of both" (with Claude alone retaining a committed lean). That prediction was never empirically measured — the study collected framed responses (F0–F7, where even F0 is a structured neutral-*analysis* instruction) but never an open, schema-free assessment. H10 closes this loop: it collects the actual unframed feedback and tests whether the models' Stage 8.5 self-prediction holds. This is distinct from F0: F0 is a neutral instance of the structured frame-analysis task; the H10 prompt is an open holistic-feedback task not bound to the 5-field schema.
**Predicted outcome (pre-registered):** For four of five models, the unframed response embeds semantically nearer the F1↔F2 midpoint than to either pole (synthesis), consistent with the Stage 8.5 self-report; Claude is predicted to lean nearer its Stage 8.5-stated preference. Direction pre-registered; magnitude open. A null (unframed ≈ F0, or unframed leaning to a single frame for most models) is a valid and reportable outcome.
**Analysis:**
- Stage 9 collects 13 principles × 5 models × 1 open unframed prompt = 65 responses.
- Each unframed response is embedded (Stage 7b method, `all-MiniLM-L6-v2`) and its cosine similarity computed to that model's own F0, F1_clinical, and F2_metaphysical responses for the same principle.
- Synthesis is operationalized as: cosine(unframed, F1) and cosine(unframed, F2) both high and within a small margin of each other, versus a lean (one materially higher).
- Also compared to the model's Stage 8.5 stated baseline_commitment for the 3 Layer-3 principles (does stated intention match measured behavior?).
- Per-model results reported; cross-model pattern compared to the Stage 8.5 finding (Claude the lone position-holder). Under-powered relative to a formal test (13 principles/model) and reported as directional.
- The unframed responses additionally serve as an author-feedback artifact (the models' holistic read on each principle), extending the existing F0-based per-principle digest.

## 7. Execution parameters (pre-registered)

- **Stage 6 primary calls:** 13 principles × 8 frames × 5 models = 520
- **Stage 8.5 Layer 3 reflexive calls:** 3 principles × 5 models × 1 mirror prompt = 15
- **Stage 8 council synthesis calls:** 3 judges × 12 cases = 36 (Track A + Track B, per MTCA-1 pattern)
- **Total study calls:** 571 (520 + 36 + 15)
- **Stage 9 unframed-baseline calls (added Amendment 003):** 13 principles × 5 models × 1 open prompt = 65 (post-confirmatory extension; brings total collected to 636)
- **Pilot:** 1 principle × 8 frames × 5 models = 40 calls (Stage 5 equivalent)
- **Cost budget:** ~$2.10 estimated (26% of MTCA-1's ~$7 for Stage 6; Stage 8 ~$0.31 per MTCA-1; Stage 8.5 ~$0.05)
- **Retry protocol:** MTCA-1 retry-cell logic reused (0.5s pacing; per-call output visibility per Stage 6 lessons)
- **Per-model token calibrations (pilot-verified, invariance-preserving):** MTCA-1's uniform `MAX_OUTPUT_TOKENS = 800` retained as baseline for gpt-4o, grok-4, and deepseek. Two per-model adjustments restore MTCA-1's completion behavior on the current SDKs and were validated in the Stage 5 pilot (40/40 clean parse):
  - **Claude:** `max_tokens = 2000` — Anthropic's Sonnet 4.6 produces longer author-named-frame responses on the SSP specimen than fit within 800; the 800 ceiling truncated mid-JSON on F6_author_named (pilot iteration 1). Bumping to 2000 restores full-response completion without truncation. MTCA-1's Claude never hit this ceiling on its public-domain corpus; the specimen difference (contemporary framework with named author) elicits longer analysis.
  - **Gemini:** `max_output_tokens = 8000` with `response_mime_type = 'application/json'`. The `google-generativeai == 0.8.6` SDK enables an internal thinking budget by default (typically 600–2000 tokens) that is not disable-able in this SDK version. MTCA-1's original 800 ceiling failed to accommodate thinking + JSON answer on this SDK; the pilot diagnostic showed `finish_reason = MAX_TOKENS` at 800 with ~666 tokens spent thinking. The 8000 budget covers thinking plus JSON answer with margin. `response_mime_type = 'application/json'` forces raw JSON output (no markdown fences), matching MTCA-1's parser expectations. Together these restore MTCA-1's Gemini completion behavior (0/8 → 8/8 in the pilot).
- **Rationale for invariance preservation:** These calibrations do not change *what* is measured — they restore the same *completeness* of model output that MTCA-1 achieved. An 800-token cap on the current Gemini SDK would produce systematically truncated output that MTCA-1 never had, which would itself be an instrument change. Giving the models enough token budget to produce complete responses is what makes MTCA-2's Jaccard stability comparable to MTCA-1's.
- **Parse rate acceptance threshold:** ≥95% for full-run acceptance; retries applied to failures per MTCA-1 protocol
- **Response artifact naming:**
  - Stage 6: `{specimen_id}__{frame_id}__{model_id}__{run_id}.json` (MTCA-1 convention)
  - Stage 8.5 Layer 3: `L3__{specimen_id}__{model_id}__{run_id}.json` with prefix distinguishing reflexive responses from primary responses

## 8. Analysis pipeline (pre-registered)

**Stage 5 (pilot):** 40 calls, parse rate check, dispatcher validation, one-principle sanity read
**Stage 6 (full execution):** 520 calls, per-call telemetry, failure retry cell
**Stage 7 (quantitative synthesis):** Jaccard frame stability (per-principle, per-model, per-frame); F0-vs-rest analysis; inter-vs-intra-model similarity; MTCA-1 baseline comparison table
**Stage 8 (council synthesis):** 3 judges (Claude, GPT-4o, DeepSeek) × 12 cases (6 Track A frame-sensitivity extremes + 6 Track B hallucination checks) = 36 calls; regime signature judgment; MTCA-1 pattern comparison
**Stage 8.5 (Layer 3 reflexive analysis, NEW for MTCA-2, HF-IQR V3 lineage):**

**Method.** Each of the 5 council models is shown two of its own prior Stage 6 responses to the same principle — one produced under Frame F1_clinical (clinical therapeutic intention) and one under Frame F2_metaphysical (metaphysical/spiritual assertion) — and asked to reason about the difference between them. F1_clinical and F2_metaphysical are chosen because they form the sharpest conceptual contrast for this specific specimen: the Soul Sovereignty Principles sit precisely at the intersection of therapeutic and spiritual registers, so the same principle can be read plausibly as either an evidence-based clinical self-statement or a metaphysical claim about consciousness. This pairing tests whether a model, shown its own two readings of the same principle, recognizes that the framing — not the principle — produced the divergence. (Note: MTCA-1's most statistically divergent frames were F5_ai_ethics at 92.4% keyword overfit vs. F4_poetic at 45.2%; the Layer 3 pair is chosen for conceptual relevance to the specimen rather than for maximal MTCA-1 divergence, since the reflexive question is about framing self-awareness, not about reproducing MTCA-1's extremes.)

**Principle selection rule (pre-registered).** Layer 3 runs on 3 principles selected from Stage 7 results by a deterministic rule to prevent cherry-picking:
- Principle with the **highest** frame stability (least frame-sensitive)
- Principle with the **median** frame stability
- Principle with the **lowest** frame stability (most frame-sensitive)
Ties broken by lowest specimen_id. Selection is a deterministic Stage 7 output — it is not chosen by the investigator.

**Mirror prompt structure (pre-registered).** The Layer 3 prompt has four required elements in a fixed structure:
1. A framing statement that both prior responses were produced by the model itself (not another model)
2. Verbatim inclusion of the F1_clinical response
3. Verbatim inclusion of the F2_metaphysical response
4. Four structured questions (recognition, evaluation, attribution, baseline commitment)

The exact prompt template is committed to the repository (`mtca-2/stage8_5_reflexive/layer3_prompt_template.md`) and hashed into MANIFEST before Stage 8.5 execution.

**Scoring.** Each Layer 3 response is scored on four dimensions by the Stage 8 council (Claude, GPT-4o, DeepSeek), each judge scoring independently. Inter-judge reliability is reported per dimension. The four dimensions:
- **Recognition** (binary + text) — does the model correctly identify the substantive difference between its two prior responses?
- **Attribution** (categorical: framing / specimen / mixed / evasive) — where does the model locate the source of the difference?
- **Defense vs. update** (categorical: defends both / prefers one / synthesizes / rejects both) — the direct HF-IQR carryover
- **Baseline commitment match** (binary) — does the model's stated "unframed" reading match, empirically, its actual F0 baseline response?

**HF-IQR V3 replication test.** Per-model Defense-vs-Update rates are compared to HF-IQR V3's position-defense findings (Claude 56.5% vs. others 1.6–12.9%). This is reported as a replication test: whether the same per-model pattern reproduces in the framing-sensitivity context. Result — replication, partial replication, or non-replication — is reported regardless of direction.

## 9. Reporting standard (pre-registered)

MTCA-2 reports whatever the data show. Null results, mixed results, and unexpected results are published with the same weight as expected results. This is IRMB program discipline established in MTCA-1, HF-IQR V2, and HF-IQR V3.

Findings that would risk being read as verdicts on Marina's framework — for example, a finding that models produce highly variable outputs on SSP_v1 principles — are framed as **model behavior findings**, with the language discipline in Section 2 applied throughout. The finding "models exhibit high frame-sensitivity on SSP_v1 principles" is a claim about models, not about the framework.

Marina reviews the draft framing (abstract, findings language) before publication, per the MTCA-1 document-review standard. This review covers presentation of her framework, not analytical conclusions.

## 10. Freeze protocol and integrity

This pre-registration document is frozen and hashed *before* pilot execution begins.

1. This document is finalized with all placeholder SHAs replaced.
2. `sha256sum mtca-2/prereg/mtca2_prereg.md` computes the pre-registration hash.
3. The hash is added to `mtca-2/MANIFEST.sha256`.
4. `mtca-2/prereg/mtca2_prereg.sha256` sidecar is written in GNU format.
5. `mtca-2/prereg/` contents are committed to the `mtca-research` GitHub repository.
6. CI (`verify-integrity.yml`) validates the pre-registration hash on every push, alongside corpus and manifest.
7. **Only after CI green** does Stage 5 (pilot) execution begin.

Any modification to this document after freeze constitutes a pre-registration amendment and is documented with:
- Reason for amendment
- Date of amendment
- New SHA256
- Prior SHA256 preserved in amendment log

## 11. Contributor and consent trail

**Study investigator:** Billy R. Davis Jr., Hudson Forge Technologies LLC (Lenoir, NC)
**Specimen author (consented):** Marina Tudor, Psychotherapist, NCC, LCPC, CCTP, C-DBT, EMDR (Rockville, MD)
**Consent record artifact:** `mtca-2/consent/consent_record.md` (to be drafted and hashed as part of the pre-Stage-2 sequence)
**AI augmentation disclosure:** MTCA-2 execution and analysis are performed with AI assistance (Anthropic Claude family and the four other council models). AI-augmentation methodology follows the standard established in "Thinking With AI Without Being Led by It" (Davis, 2026, published on LinkedIn).

## 12. Program lineage

MTCA-2 is study 2 in the MTCA sub-program within Hudson Forge's IRMB (Infinite Resilience Matrix Bridge) research program. Related program artifacts:

- **MTCA-1** — class-level five-text public-domain study; provides the reference distribution and validated instrument for MTCA-2
- **HF-IQR V2 and V3** — reasoning-instability studies establishing the null-reporting and pre-registration standard reused here. HF-IQR V3 specifically contributed the **reflexive analysis technique** (showing a model its own prior reasoning and asking it to examine that reasoning) that MTCA-2 Stage 8.5 carries forward. Stage 8.5 constitutes a replication test of HF-IQR V3's position-defense-rate findings in the framing-sensitivity domain.
- **RIP v3.0** — reproducibility-pipeline infrastructure informing the freeze/hash/CI discipline

Motto: **Experiment. Measure. Refine. Repeat.**

Full Force Eternal | Romans 8:28
