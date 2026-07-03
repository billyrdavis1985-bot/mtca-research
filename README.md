# MTCA Research Program

**Mixed-Tier Corpus Analysis** studies within the IRMB (Integrated Reasoning Methodology Base) research program at Hudson Forge Technologies LLC.

## Overview

The MTCA program studies how frontier AI systems reason about non-propositional, identity-regulating, therapeutically-framed content. This is a class of text — first-person affirmations, therapeutic intentions, spiritual assertions, behavioral commitments — that resists standard empirical evaluation but is increasingly common as both training data and input in real-world AI systems.

The program uses the IRMB multi-model council methodology: multiple frontier models in fresh contexts producing independent assessments, followed by structured synthesis across responses. Each study in the MTCA line uses this methodology as its instrument.

## Program structure

The program is organized as a single repository containing multiple studies, each with its own paper, preprint, and reproducibility artifacts. Studies share the underlying methodology infrastructure (frame prompts, council dispatchers, synthesis code) while producing independent research contributions.

| Study | Focus | Status | Paper |
|-------|-------|--------|-------|
| MTCA-1 | Content-class analysis using 5 public-domain texts across 4 lineages | Complete, writeup in progress | (forthcoming) |
| MTCA-2 | Application of validated methodology to a contemporary consented specimen | Planned | (forthcoming) |

## Repository layout

```text
mtca-research/
├── README.md                    # this file
├── LICENSE                      # Apache 2.0
├── CITATION.cff                 # citation metadata
│
├── methodology/                 # shared infrastructure across studies
│   ├── README.md
│   ├── council_dispatchers.py   # unified provider dispatch layer
│   ├── frame_prompts.md         # frozen frame templates with SHA256
│   └── reproducibility_notes.md
│
├── mtca-1/                      # first study
│   ├── README.md
│   ├── paper/
│   ├── notebooks/               # Stage 1-10 notebooks
│   ├── corpus/                  # frozen v1.1 corpus
│   ├── stage3_design/           # frame design + execution plan
│   ├── stage5_pilot/            # pilot responses
│   ├── stage6_execution/        # full 2000-response dataset
│   ├── stage7_synthesis/        # quantitative findings
│   └── stage8_council/          # qualitative judge assessments
│
└── mtca-2/                      # placeholder for future study
    └── README.md
```

## Methodology principles

All MTCA studies commit to:

- **Frozen artifacts at each stage.** Every design decision, prompt, and dataset gets SHA256-hashed and archived. Studies can be reproduced against exact versions.
- **Pre-registered nulls.** What counts as a failed or uninteresting outcome is defined before execution. Null results are valid findings.
- **Language discipline.** All claims are framed as model behavior under specified methodology, not as properties of the source texts. See individual study Stage 1 documents.
- **AI-augmented research disclosure.** Where AI tools are used in analysis, synthesis, or drafting, the roles are documented and the researcher adjudicates.
- **Reflexivity tracking.** Researcher decisions, corrections, and adjudications are logged alongside artifacts.
- **Reproducibility.** Frozen corpus SHAs, frame prompt SHAs, execution plan SHAs, and synthesis SHAs form a verifiable chain from raw texts to published findings.

## Program lineage

The MTCA program builds on prior IRMB work:

- **HF-IQR (V1, V2, V3)** established and refined the multi-model council methodology for AI critique behavior analysis. V3 (published 2026) characterized position-defense and calibration patterns across five frontier models including a ceiling-effect null on the primary endpoint.
- **QPU Drift Collector** (published 2026) established the reproducibility conventions used across IRMB studies — frozen designs, SHA256 anchoring, open-source release under Apache 2.0.
- **MTCA-1** applies the council methodology to a new content class — non-propositional therapeutic text — with a new experimental structure focused on frame sensitivity.

## Reproducibility

Every study in this program can be reproduced end-to-end from the artifacts in this repository:

1. Load the frozen corpus (SHA256 hash in study README)
2. Load the frozen frame prompts (SHA256 hashes in `methodology/frame_prompts.md`)
3. Load the frozen execution plan (SHA256 hash in study README)
4. Execute against the five council models using the dispatchers in `methodology/`
5. Verify response SHAs match the archived responses

Any deviation in the reproduced results indicates either model drift (updated model versions producing different outputs) or a bug in the reproduction. Both are informative.

## Citation

When citing this program:
Davis, B. (2026). MTCA Research Program: Multi-model AI reasoning studies on
non-propositional content classes. Hudson Forge Technologies LLC.
https://github.com/billyrdavis1985-bot/mtca-research

Individual studies have their own citations in their respective directories.

## License

Apache 2.0. See `LICENSE` for details.

## Research philosophy

> *Experiment. Measure. Refine. Repeat.*
>
> — Billy Davis | Hudson Forge Technologies | IRMB Research Program
