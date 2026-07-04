# MTCA Research Program

**Mixed-Tier Corpus Analysis** — studies of how frontier AI systems reason about non-propositional, identity-regulating, therapeutically-framed content. Part of the IRMB research program at Hudson Forge Technologies LLC.

## Overview

The MTCA program studies a class of text — first-person affirmations, therapeutic intentions, spiritual assertions, behavioral commitments — that resists standard empirical evaluation yet increasingly appears as both training data and live input in AI systems. The program's instrument is a multi-model council: several frontier models, each in a fresh context, producing independent structured assessments that are then synthesized across responses.

Each study in the line is self-contained (its own paper, preprint, and reproducibility artifacts) while sharing the council methodology and infrastructure.

## Studies

| Study | Focus | Status |
|-------|-------|--------|
| MTCA-1 | Content-class analysis across 5 public-domain texts / 4 lineages | Complete; writeup in progress |
| MTCA-2 | Validated methodology applied to a contemporary consented specimen | Planned |

## Repository layout

```text
mtca-research/
├── README.md                     # this file — program overview
├── LICENSE                       # Apache 2.0
├── .gitattributes                # forces binary handling for artifacts (hash stability)
├── .github/workflows/
│   └── verify-integrity.yml      # CI: verifies MANIFEST.sha256 on every push
│
└── mtca-1/
    ├── README.md                 # MTCA-1 study specifics
    ├── MANIFEST.sha256           # authoritative byte-level integrity anchors
    ├── ARTIFACT_HASHES.json      # provenance-ID ↔ integrity-hash crosswalk
    ├── notebooks/                # Stage 1–8 notebooks
    ├── stage1/                   # foundational document (research question, nulls, ethics)
    ├── corpus/
    │   ├── raw/                   # 5 source texts (public domain + synthetic)
    │   └── frozen/               # corpus v1.0, v1.1 (frozen, hashed)
    ├── stage3_design/            # frame design + execution plan
    ├── stage6_execution/         # full council dataset (2000 responses + index)
    ├── stage7_synthesis/         # quantitative findings
    ├── stage8_council/           # qualitative judge assessments
    └── manifests/                # per-stage summary manifests
```

*(Stage 5, the 40-call pilot, is intentionally excluded — superseded by the full Stage 6 execution.)*

## Reproducibility

**Two-role hashing model.** Frozen-artifact *filenames* embed a **design-time provenance identifier** — a content hash computed during the freeze step that binds related artifacts into one version chain (e.g., Stage 3 design `6380e711…` links the design file, its execution plan, and every Stage 6 response generated under it). These filename identifiers are **not** byte-integrity checksums (corpus v1.0 is the lone self-verifying exception).

**Authoritative integrity** lives in `mtca-1/MANIFEST.sha256`, verifiable on any platform:

```bash
cd mtca-1
sha256sum -c MANIFEST.sha256
```

The provenance-ID ↔ byte-hash mapping for every hash-named artifact is recorded in `mtca-1/ARTIFACT_HASHES.json`. Corpus v1.1 canonical integrity hash: `e8e998c9099e0fa6dd0d3f98ae5ae49af3fc826c9a2c8c51a7eff19b4a439a53`.

**Continuous verification.** `.github/workflows/verify-integrity.yml` runs `sha256sum -c` on every push and pull request, so a green check certifies that committed bytes match the manifest on a clean clone.

**Reproduction path:** load the frozen corpus and frame prompts → execute against the five council models using the archived design and execution plan → verify response bytes against `MANIFEST.sha256`. Any divergence indicates either model drift (updated model versions) or a reproduction error — both informative.

## Methodology principles

- **Frozen artifacts at every stage**, hash-anchored and archived.
- **Pre-registered nulls** — failure conditions defined before execution; null results are valid findings.
- **Language discipline** — all claims framed as model behavior under specified methodology, never as properties of the source texts.
- **AI-augmented research disclosure** — where AI assists analysis, synthesis, or drafting, roles are documented and the researcher adjudicates.
- **Reflexivity tracking** — researcher decisions and corrections logged alongside artifacts.

## Program lineage

- **HF-IQR (V1–V3)** established and refined the multi-model council methodology for AI critique-behavior analysis; V3 characterized position-defense and calibration patterns across five frontier models, including a ceiling-effect null on the primary endpoint.
- **QPU Drift Collector** established the reproducibility conventions used across IRMB studies — frozen designs, SHA256 anchoring, open release under Apache 2.0.
- **MTCA-1** applies the council methodology to a new content class with a frame-sensitivity experimental design.

## Citation
Davis, B. (2026). MTCA Research Program: Multi-model AI reasoning studies on
non-propositional content classes. Hudson Forge Technologies LLC.
https://github.com/billyrdavis1985-bot/mtca-research

Individual studies carry their own citations in their directories.

## License

Apache 2.0. See `LICENSE`.

---

> *Experiment. Measure. Refine. Repeat.*
> — Hudson Forge Technologies · IRMB Research Program
