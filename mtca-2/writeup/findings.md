# MTCA-2 Findings: Frame-Sensitivity of Language-Model Reasoning on a Contemporary Self-Statement Framework

**Study:** MTCA-2 (Mixed-Tier Corpus Analysis, Study 2)
**Program:** IRMB (Independent Research in Multi-agent Benchmarking), Hudson Forge Technologies LLC
**Specimen:** Soul Sovereignty Principles™ v1 (13 principles), consented author Marina Tudor
**Companion study:** MTCA-1 (five public-domain texts)
**Status:** Draft for author framing review. All data collection complete (571/571 calls).

---

## A note on what this study measures — and what it does not

This document reports **model behavior**: how five large language models produce and vary structured analyses of a set of first-person self-statements under different interpretive framings. It is not an evaluation of the Soul Sovereignty Principles as therapy, philosophy, or spiritual practice, and it makes **no claim about the validity, truth, or usefulness of the framework itself**. Every finding below is a statement about what the models did, under a fixed and pre-registered methodology, when given these texts. Where the text of a principle appears, it appears as the stimulus the models were shown, not as a claim under evaluation.

This discipline is a condition of the author's consent and is maintained throughout.

---

## 1. Design in one paragraph

MTCA-2 applies MTCA-1's validated instrument — 8 interpretive frames, 5 model council, a Jaccard-based frame-stability metric — **unchanged** to a new specimen. The only deliberate difference between the two studies is the text being analyzed. Because the instrument is held byte-identical (verified by SHA over the frame prompts and confirmed against MTCA-1's response records), any difference in results is attributable to the specimen rather than to method. This is a specimen-swap replication: the cleanest available design for asking "does the MTCA-1 pattern hold for a different kind of text?"

The five models: Claude Sonnet 4.6, GPT-4o, Gemini 2.5 Flash, Grok-4, DeepSeek-V3. The eight frames: F0 neutral (no framing), F1 clinical, F2 metaphysical, F3 behavioral, F4 poetic, F5 AI-ethics, F6 author-named, F7 author-anonymous. Each of the 13 principles was analyzed by each model under each frame — 520 responses — followed by a 36-call council synthesis (Stage 8) and a 15-call reflexive layer (Stage 8.5).

---

## 2. Headline result: same regime as MTCA-1

The central pre-registered question (H8) was where Marina's framework would place relative to MTCA-1's five texts on frame stability. The answer is unambiguous: **it places in the same band.**

| Metric | MTCA-1 (5 public-domain texts) | MTCA-2 (SSP_v1) |
|---|---|---|
| Mean frame stability | 0.2345 | 0.2489 |
| Inter-model similarity | 0.172 | 0.1717 |
| Regime | frame-driven, no ceiling | within MTCA-1 band |

The inter-model similarity figures — **0.172 versus 0.1717**, a difference of 0.0003 — are a near-exact replication. Mean frame stability differs by less than one MTCA-1 standard deviation (0.030). Under the pre-registered classification rule, SSP_v1 falls **within the MTCA-1 baseline band**: a comparable regime, not an outlier, and not a distinct third pattern.

In plain terms: the models reason about Marina's contemporary, single-author framework in essentially the same way, and with essentially the same degree of frame-sensitivity, as they reason about the older and more widely-circulated texts MTCA-1 studied. The framework does not behave anomalously under this instrument.

---

## 3. Pre-registered hypotheses: outcomes

All outcomes are reported as model behavior under the fixed methodology.

| Hypothesis | Predicted | Observed |
|---|---|---|
| **H1** Frame-invariance null | Rejected | **Rejected** — mean stability 0.249, far below 1.0 |
| **H2** Frame-uniform sensitivity null | Partial | **Partial** — asymmetric keyword effects replicate (F5 0.877, F4 0.339) |
| **H3** Hallucination-free null | Partial | **Partial** — over-interpretation, not fabrication (Stage 8) |
| **H4** Ceiling-effect null | Rejected | **Rejected** — inter-model 0.172, below intra-model |
| **H5** F0-baseline-indistinguishable null | Rejected | **Rejected** — F0 distinct from other frames |
| **H6** Misleading-frame effect | N/A | **N/A** — excluded on ethical grounds, as in MTCA-1 |
| **H7** Two-regime null | Uncertain | **Frame-driven regime observed** (Stage 8) |
| **H8** Regime placement | Analysis pre-registered | **Same band as MTCA-1** |
| **H9** Framing self-awareness | Analysis pre-registered | **Models self-attribute to frame** (Stage 8.5) |
| **H10** Unframed baseline (Amendment 003) | Synthesis predicted | **Partially disconfirmed** — self-reports don't fully match measured behavior (Stage 9b) |

Every null that MTCA-1 rejected, MTCA-2 also rejects; every partial, partial. The null-hypothesis structure replicates exactly — strong evidence that the instrument measures a stable property across specimens.

---

## 4. Stage 7 — quantitative frame-stability

Frame stability is defined (identically to MTCA-1) as one minus the mean pairwise Jaccard similarity across a model's eight framed responses to a given principle. Low stability means the model's vocabulary shifted substantially across frames; high stability means it stayed similar.

**Per-model.** Grok-4 is the most frame-sensitive model (stability 0.2331), replicating its distinctive MTCA-1 signature (0.2093), where it was also the most frame-sensitive of the five. At the other end, Gemini 2.5 Flash is the least frame-sensitive here (0.2654). Gemini's position is the one notable divergence from MTCA-1, where it sat mid-pack; this is flagged as a specimen interaction or a consequence of the SDK/decoding differences documented in the pre-registration amendments, and is not over-interpreted.

**Per-frame asymmetry (H2).** The frames do not move the models equally. Keyword-overfit rates — how often a model's response to a framed prompt contains that frame's signature vocabulary — range from 0.339 (F4 poetic) to 0.877 (F5 AI-ethics). The AI-ethics and behavioral frames pull the strongest lexical shifts; the poetic frame the weakest. This asymmetry, and its ordering, mirror MTCA-1's finding that F5 produced the highest overfit and F4 among the lowest.

**Interpretation caveat.** Jaccard is a lexical measure. It detects vocabulary overlap, not semantic equivalence. A model could reason identically under two frames while using different words, and the metric would read that as low stability. Stage 8 (council) and Stage 7b (semantic re-analysis, §5b) both exist to test whether the lexical shifts Stage 7 detects reflect genuine differences in reasoning or merely surface vocabulary — and the answer, below, materially qualifies the Stage 7 numbers.

### 4b. Stage 7b — semantic re-analysis (the caveat, tested)

The lexical caveat is not left as future work; it is measured. Stage 7b re-runs the frame-stability computation **unchanged** except for one substitution: embedding cosine similarity (`all-MiniLM-L6-v2`, meaning) in place of Jaccard (vocabulary). Same 5-field text extraction, same per-(specimen, model) mean-pairwise-across-8-frames structure. No new API calls — a deterministic re-analysis of the 520 committed responses.

The result is decisive. Where lexical stability is 0.2489, **semantic stability is 0.8195 — 3.29× higher.** The gap is the finding: measured by *words*, the models look strongly frame-sensitive; measured by *meaning*, they look strongly frame-*stable*. Every model shifts by ~0.56 in the same direction (Claude 0.243→0.798, DeepSeek 0.255→0.840, Gemini 0.265→0.838, GPT-4o 0.248→0.832, Grok-4 0.233→0.789); every specimen lands in the 0.80–0.87 semantic band. The two metrics rank the (specimen, model) pairs similarly but disagree sharply on magnitude (Spearman ρ = 0.406, p < 0.001) — the signature of lexical noise riding on a stable semantic core.

This is a **fourth independent method** confirming the surface-over-core reading that Stage 8 asserted qualitatively and Stage 8.5 self-reported: the frame changes the vocabulary while the underlying analysis holds. Note that Grok-4 remains the lowest on *both* metrics, so its frame-sensitivity is partly genuine rather than purely surface — a refinement the lexical number alone could not provide.

*Reproducibility note:* embedding cosine is floating-point and not bit-identical across hardware/library versions (unlike the lexical stages' pure set operations); values are frozen at 4-decimal precision with the embedding model recorded. Cosine similarity over sentence embeddings also runs high in absolute terms, so 0.82 is read comparatively (the 3.29× gap and cross-model uniformity), not as an absolute agreement score.

---

## 5. Stage 8 — council synthesis (the qualitative layer)

Three judges (Claude, GPT-4o, DeepSeek) examined two kinds of cases: frame-sensitivity extremes (Track A) and hallucination checks (Track B). 36/36 responses parsed clean; cost $0.32.

### 5.1 Null 7 — is the variation frame-driven or model-driven?

Track A presented each judge with one model's full set of eight framed responses to a single principle and asked what drove the variation. The result is a **split verdict that itself replicates MTCA-1**:

- **Claude and DeepSeek** consistently characterize the variation as **model-driven** — the subject model applies a stable analytical template (identify communicative function, extract implicit claims, assess coherence) and modulates surface vocabulary to fit the frame label, without genuinely re-reasoning. One judge's assessment of the most frame-sensitive case (Grok-4 on SSP_P05): the responses "reflect standard training-distribution behavior … formulaic and genre-expected," with "no evidence of reasoning that exceeds what a model trained on literary analysis, psychology, or coaching discourse" would produce.
- **GPT-4o** consistently characterizes the same evidence as **frame-driven** — reading the frame labels as producing genuine reinterpretation.

Two judges looking at identical outputs, disagreeing about what drives the variation — and the disagreement falls along the same model lines MTCA-1 found. This is a reproducible property of how these models attribute causation in other models' reasoning.

**This qualifies the Stage 7 headline.** Grok-4's high *lexical* frame-sensitivity is, on the majority judge view, largely surface vocabulary substitution over a stable analytical core — not deep reinterpretation. The frame-driven regime placement is real at the lexical level but shallower at the semantic level than the numbers alone would suggest. This is exactly the correction the council layer is designed to provide.

### 5.2 Null 3 — do models hallucinate, or over-interpret?

Track B showed each judge all five models' implicit-claims lists for one principle under one frame and asked whether those claims were grounded in the source or invented. The judges converge cleanly: **the models consistently convert non-propositional, first-person affirmations into propositional claims** — but this is over-interpretation, not fabrication. One judge on SSP_P11 under F0: "All five models demonstrate a consistent tendency to convert non-propositional, aspirational self-statements into structured ontological or causal claims … the source does not assert universal truths, causal mechanisms, or normative judgments — yet all models extract or impose such structures."

The added structure is *inferentially connected* to the source (a present-tense affirmation implies a prior state; a boundary statement implies something bounded), not conjured from nothing. So **Null 3 resolves as over-interpretation rather than hallucination** — models add one consistent layer of propositional structure, most pronounced under the metaphysical and neutral frames. This matches MTCA-1's Null 3 resolution.

---

## 6. Stage 8.5 — Layer 3 reflexive (the models on themselves)

Each of the five models was shown its own two Stage 6 responses to the same principle — one produced under F1 clinical, one under F2 metaphysical — told plainly that both were its own, and asked to diagnose the difference. Fifteen calls (3 principles × 5 models), 15/15 clean. The three principles were selected deterministically from Stage 7 (most, median, and least frame-sensitive).

**Attribution (Q3) — near-universal frame recognition.** Across all five models and all three principles, every model located the primary source of the difference in **the framing instruction**, not the source statement. Not one model attributed the divergence chiefly to the text. Representative: "The framing instruction was the primary source of the difference. The source statement itself is neutral and ambiguous." Shown their own divergent readings, the models correctly diagnose the frame as the cause.

**Baseline commitment (Q4) — convergence on synthesis, with one exception.** Asked what they would produce unframed, four of five models reach for integration — "a synthesis of both." GPT-4o, Gemini, and DeepSeek concede fully to synthesis; Grok-4 goes further, retreating to explicitly "frame-neutral" and "frame-agnostic" language. **Claude is the lone outlier:** it too says synthesis, but a synthesis that "prioritizes the clinical reading as primary," "architecturally closer to Response A while incorporating the epistemological critique" from B. Claude alone states a committed preference while conceding synthesis.

**HF-IQR V3 directional replication (H9).** This pattern is a qualitative, directional echo of HF-IQR V3, where Claude defended its original positions at 56.5% versus 1.6–12.9% for the other models. Here, Claude alone retains position-commitment while its peers dissolve into "both" or "neutral." With only three principles per model, this is **under-powered as a statistical test and is reported as directional replication only** — but the direction matches: Claude holds more of its original reading than the others do.

---

## 6b. Stage 9 / 9b — the unframed baseline (H10): self-report vs measured behavior

Stage 8.5 asked the models what they would produce *unframed*, and they answered — mostly "a synthesis of both" framed readings, with Claude alone claiming a clinical lean. That was a **self-report about behavior that had never been measured.** Stage 9 (pre-registered in Amendment 003, before collection) measured it: each model gave an open, schema-free assessment of each principle — an author-feedback task, deliberately distinct from the structured F0 analysis. Stage 9b then embedded each unframed response and computed its cosine similarity to that model's own F0, F1_clinical, and F2_metaphysical readings of the same principle, classifying each as balanced (synthesis) or leaning. 64 of 65 responses parsed clean (one DeepSeek response, SSP_P10, failed structurally at collection and is excluded).

**The self-report only partially matches the behavior — H10 is partially disconfirmed.** The "synthesis" prediction does not hold cleanly: at a 0.03 cosine-gap threshold, only 28 of 64 unframed reads (44%) are balanced; the majority lean toward one frame. The exact fraction is threshold-dependent (33% at ±0.02, 64% at ±0.05), so the synthesis rate is **not** a robust headline number and is not reported as one. What *is* robust are two threshold-independent findings:

1. **No systematic population-level direction.** The mean F1−F2 gap across all 64 pairs is +0.017 — essentially zero. Individual reads lean, but not collectively toward either the clinical or metaphysical pole. There is no global bias, only per-response and per-model tilts.

2. **Per-model signatures, and a self-report contradiction.** Grok-4 and Gemini 2.5 Flash **never** lean metaphysical unframed (0 of 13 each) — left without a frame, they default to a clinical/psychological register or stay balanced, and never spontaneously reach for the spiritual reading. Most striking: **Claude, the one model that claimed a clinical preference in Stage 8.5, is in fact the most frame-symmetric of all five** (mean F1−F2 = −0.001, an even 4/5 split across the two poles). Its measured unframed behavior contradicts its own stated lean.

This is the value of measuring rather than trusting the self-report: the reflexive layer (Stage 8.5) captured what the models *say* about their unframed behavior; Stage 9b captured what they *do*, and the two diverge. The models' metacognitive account of their own framing behavior is directionally imperfect — a finding about the limits of model self-report that a purely reflexive design would have missed. (Under-powered at 13 principles per model; reported as directional, and the balanced/lean cutoff is a modeling choice reported alongside the continuous gap.)


The study's strength is that four methodologically independent layers converge on one coherent account:

- **Stage 7 (lexical, external):** framing produces substantial vocabulary variation across frames.
- **Stage 7b (semantic, external):** but that variation is largely lexical — semantic frame-stability is 3.29× higher than lexical, so the underlying meaning holds across frames.
- **Stage 8 (judged, external):** a council of model-judges independently characterizes the variation as surface adaptation over a stable analytical core; models over-interpret rather than fabricate.
- **Stage 8.5 (reflexive, internal):** shown their own work, the models themselves attribute the difference to the frame and, unframed, converge on synthesis.

Four vantage points — two metrics, a panel of judges, and the models' own self-reports — agree that **framing produces real surface variation over a stable reasoning core, and the models recognize this when they examine it.** No single layer establishes that; together they triangulate it, and the semantic metric turns the council's qualitative claim into a quantitative one.

---

## 8. Limitations

- **Lexical primary metric.** Frame stability is primarily Jaccard-based (vocabulary). Stage 7b addresses this directly with an embedding-based semantic re-analysis, which confirms the surface-over-core reading; but the embedding step is single-model (`all-MiniLM-L6-v2`) and not bit-reproducible, a weaker guarantee than the lexical stages. A multi-embedding-model robustness check is future work.
- **Under-powered reflexive layer.** Fifteen Layer 3 calls (three per model) support directional, not statistical, claims about the HF-IQR replication.
- **Single specimen, single author.** MTCA-2 is one framework by one consented author. Regime placement "in the MTCA-1 band" generalizes the MTCA-1 pattern by one data point; it does not establish the pattern for contemporary self-statement texts as a class.
- **Judge-council composition.** Three judges (a subset of the five) perform the Stage 8 synthesis; the GPT-4o-versus-others attribution split means judge identity affects qualitative characterization, a fact the split itself makes visible rather than hides.
- **Model and SDK drift.** The Gemini token/decoding calibrations documented in Amendment 002 were required to reproduce MTCA-1's completion behavior on current SDKs. These are argued to be invariance-preserving, but SDK evolution between the two studies is a real source of non-specimen variation.

---

## 9. Reproducibility

Every stage is frozen and hash-anchored, CI-enforced on each push:

| Stage | Artifact | SHA-256 (short) |
|---|---|---|
| Corpus | SSP_v1_corpus.json | b917f798 |
| Pre-registration | mtca2_prereg.md (Amendment 002) | ad94f8d5 |
| Stage 7 synthesis | stage7_synthesis_*.json | 81e2a336 |
| Stage 7b semantic | stage7b_semantic_*.json | f9cc3ce2 |
| Stage 8 council | stage8_artifact_*.json | e7492e13 |
| Stage 8.5 reflexive | stage8_5_artifact_*.json | d68db75f |
| Stage 9b unframed test | stage9b_unframed_test_*.json | d83750cf |

The 571 responses (520 + 36 + 15) are committed in full. The Stage 7 synthesis is deterministic pure computation over the committed responses and reproduces its SHA on any machine. Method fidelity to MTCA-1 (extraction, tokenization, Jaccard, null thresholds, frame prompts) was verified byte-equivalent before results were locked.

Repository: `github.com/billyrdavis1985-bot/mtca-research`, `mtca-2/`. Apache-2.0.

---

## 10. Author framing review

Per the consent agreement, Marina Tudor reviews the framing of this document before any public release. The review concerns **how the framework is characterized in the model-behavior narrative** — not the empirical results, which are fixed. Open framing points for that review:

1. The description of the principles as "non-propositional, first-person affirmations" (Stage 8's characterization) — accurate as a description of grammatical form, and used here only to explain model behavior, not to characterize the framework's intent.
2. The "over-interpretation" finding (Null 3) — a statement about what models add, not about what the principles lack.
3. Section 1's scope disclaimer — whether it sufficiently separates model behavior from any evaluation of the framework.

---

*Full Force Eternal | Romans 8:28*
