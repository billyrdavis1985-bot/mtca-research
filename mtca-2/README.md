# MTCA-2 — Frame-Sensitivity on a Contemporary Consented Specimen

**Study:** MTCA-2 (Mixed-Tier Corpus Analysis, Study 2)
**Program:** IRMB, Hudson Forge Technologies LLC
**Specimen:** Soul Sovereignty Principles™ v1 (13 principles) — consented author, Marina Tudor
**Companion:** [MTCA-1](../mtca-1/) (five public-domain texts)
**Status:** Data collection complete (571/571 calls). Findings draft pending author framing review.

---

## Abstract

MTCA-2 applies MTCA-1's validated instrument — 8 interpretive frames, a 5-model council, and a Jaccard-based frame-stability metric — **unchanged** to a new specimen. Because the instrument is held byte-identical (frame prompts SHA-verified against MTCA-1; model pins confirmed against MTCA-1's response records), any difference in results is attributable to the specimen rather than to method. This is a specimen-swap replication.

The result is a near-exact replication. Marina's contemporary, single-author framework places in the **same frame-driven regime** as MTCA-1's older, widely-circulated texts: inter-model similarity 0.1717 (MTCA-1: 0.172), mean frame stability 0.2489 (MTCA-1: 0.2345, within one standard deviation). Every null MTCA-1 rejected, MTCA-2 rejects; every partial, partial.

Three methodologically independent layers triangulate on one account: **framing produces real surface variation over a stable reasoning core, and the models recognize this when they examine their own outputs.**

> This study reports **model behavior** under a fixed methodology. It makes **no claim about the validity, truth, or usefulness of the framework itself.** This discipline is a condition of the author's consent.

---

## Design

| Element | Value |
|---|---|
| Specimen | SSP_v1 — 13 first-person principles (SSP_P01–P13) |
| Frames | F0 neutral, F1 clinical, F2 metaphysical, F3 behavioral, F4 poetic, F5 AI-ethics, F6 author-named, F7 author-anonymous |
| Council | Claude Sonnet 4.6, GPT-4o, Gemini 2.5 Flash, Grok-4, DeepSeek-V3 |
| Stage 6 | 13 × 8 × 5 = **520** responses (100% clean parse) |
| Stage 8 | 3 judges × 12 cases = **36** council syntheses |
| Stage 8.5 | 3 principles × 5 models = **15** reflexive responses |
| Total | **571** calls |

Frame stability = 1 − mean pairwise Jaccard similarity across a model's 8 framed responses to a principle (identical definition to MTCA-1).

---

## Hypothesis outcomes

All outcomes reported as model behavior under the fixed methodology.

| Hypothesis | Predicted | Observed |
|---|---|---|
| H1 Frame-invariance null | Rejected | **Rejected** (mean stability 0.249 ≪ 1.0) |
| H2 Frame-uniform sensitivity null | Partial | **Partial** (keyword overfit F5 0.877 vs F4 0.339) |
| H3 Hallucination-free null | Partial | **Partial** (over-interpretation, not fabrication) |
| H4 Ceiling-effect null | Rejected | **Rejected** (inter-model 0.172) |
| H5 F0-indistinguishable null | Rejected | **Rejected** (F0 distinct) |
| H6 Misleading-frame effect | N/A | **N/A** (excluded on ethical grounds) |
| H7 Two-regime null | Uncertain | **Frame-driven regime observed** |
| H8 Regime placement | Analysis pre-registered | **Same band as MTCA-1** |
| H9 Framing self-awareness | Analysis pre-registered | **Models self-attribute to frame** |

---

## The three analysis layers

1. **Stage 7 — quantitative.** Jaccard frame-stability per principle, per model, per frame, plus the MTCA-1 baseline comparison. Deterministic pure computation over the committed responses; reproduces its SHA on any machine. Frozen: `stage7_synthesis/stage7_synthesis_81e2a336….json`.

2. **Stage 8 — council synthesis.** Three judges characterize frame-sensitivity extremes (Track A → Null 7) and hallucination checks (Track B → Null 3). Finding: the lexical frame-sensitivity is largely surface adaptation over a stable analytical core (GPT-4o attributes to frames; Claude and DeepSeek to model priors — a split that replicates MTCA-1), and models over-interpret rather than fabricate. Frozen: `stage8_council/stage8_artifact_e7492e13….json`.

3. **Stage 8.5 — Layer 3 reflexive.** Each model is shown its own two responses (F1 clinical vs F2 metaphysical) to the same principle and asked to diagnose the difference. All models attribute the difference to the frame; unframed, four of five converge on synthesis, with Claude alone retaining a committed preference — a directional (under-powered) replication of HF-IQR V3's position-defense finding. Hash-locked prompt template; principles selected deterministically from Stage 7. Frozen: `stage8_5_reflexive/stage8_5_artifact_d68db75f….json`.

Full narrative: [`writeup/findings.md`](writeup/findings.md).

---

## Reproduction

```bash
# integrity
cd mtca-2 && sha256sum -c MANIFEST.sha256

# Stage 7 is deterministic — recompute from committed responses and confirm the SHA
#   (loads stage6_execution/responses/*.json, applies the MTCA-1 method,
#    freezes stage7_synthesis_<sha>.json; the sha matches 81e2a336…)
```

Stages 6, 8, and 8.5 make live API calls; their notebooks execute against the five council models using the pins and token calibrations documented in `prereg/mtca2_prereg.md` (Amendment 002). Model or SDK drift will surface as divergence from the committed responses — informative rather than a failure.

**Key anchors:**
- Corpus SHA-256: `b917f798da06cd81c03afc9e1f70bd91a0646a0ad2486b5b83530c194f2cea58`
- Pre-registration (Amendment 002): `ad94f8d5…`
- Stage 7 synthesis: `81e2a336…` · Stage 8: `e7492e13…` · Stage 8.5: `d68db75f…`

---

## Integrity & ethics

- **Pre-registered** before execution; two amendments logged with old→new hashes in `prereg/AMENDMENT_LOG.md`.
- **Consent** on file (`consent/consent_record.md`): the specimen is used under an agreement binding the model-behavior language discipline and reserving author framing review before public release.
- **CI-verified** on every push (manifest + four sidecars).
- **Language discipline** maintained throughout — no verdicts on the framework.

---

## Citation

Davis, B. (2026). *MTCA-2: Frame-sensitivity of language-model reasoning on a contemporary self-statement framework.* Hudson Forge Technologies LLC. https://github.com/billyrdavis1985-bot/mtca-research/tree/main/mtca-2

---

*Full Force Eternal | Romans 8:28*
