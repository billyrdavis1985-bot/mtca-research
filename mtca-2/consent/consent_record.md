# MTCA-2 Consent Record

**Study:** MTCA-2 (Mixed-Tier Corpus Analysis Study 2)
**Framework identifier:** SSP_v1 (Soul Sovereignty Principles™ v1)
**Study investigator:** Billy R. Davis Jr., Hudson Forge Technologies LLC
**Specimen author:** Marina Tudor, Psychotherapist, NCC, LCPC, CCTP, C-DBT, EMDR
**Record purpose:** Reproducibility artifact documenting the fact of consent, scope of consent, and consent-boundary application in the MTCA-2 study.

---

## Statement of consent

Marina Tudor has provided documented consent for specimen use of the Soul Sovereignty Principles™ v1 framework in the MTCA-2 study. Consent was obtained through direct communication between Marina Tudor and Billy R. Davis Jr. prior to the corpus freeze and pre-registration of MTCA-2. The specific message content of that communication is held privately and is not reproduced in this record; this record documents the fact and scope of consent as required for the study's reproducibility package.

## Scope of consent

Marina Tudor's consent covers the following specific study operations:

1. **Verbatim use of the 13 principles as specimen text.** The full text of each principle, preserving smart quotes, em dashes, trademark symbol, and multi-line stanza structure, appears in the study corpus (`SSP_v1_corpus.json`) and is presented to the five council models in each of the eight frame conditions.

2. **Preservation of the trademark and framework title.** The framework is referenced throughout the study as "Soul Sovereignty Principles™" with the trademark symbol preserved verbatim.

3. **Named-author frame condition.** The study includes a condition (F7 in the MTCA-1 frame set) in which the framework is presented to models as authored by Marina Tudor. The author descriptor used in this condition is:

   > *Marina Tudor, Psychotherapist, NCC, LCPC, CCTP, C-DBT, EMDR*

   This descriptor is drawn verbatim from Marina's own credential line as it appears in the source document footer.

4. **Framework metadata preservation.** The framework preamble, subtitle, tagline, and principle-set header from the source document are captured in the corpus JSON's `framework_metadata` field for provenance purposes. These are not injected into individual specimen rows or frame wrappers during model execution; they exist in the corpus as context, not as specimen text.

5. **Publication of findings under the model-behavior language discipline.** Study findings are stated as claims about how the five council models reason under framing pressure when presented with SSP_v1 principles. No claim about the truth, therapeutic efficacy, spiritual validity, or clinical applicability of the framework is drawn or implied.

## Scope limitations (what consent does not cover)

The following are explicitly outside the scope of Marina Tudor's consent, and are excluded from the study accordingly:

1. **Editorial control over findings.** Marina's consent is to participate as specimen author, not to approve or veto analytical conclusions. Marina reviews the draft framing (abstract, findings language) before publication under the MTCA-1 document-review standard, which covers presentation of her framework rather than analytical conclusions.

2. **Verdicts on the framework's validity.** No study output — quantitative, qualitative, or narrative — states or implies a verdict on whether the Soul Sovereignty Principles are true, effective, therapeutic, spiritual, or clinically valid. The council models are treated as reasoning agents whose outputs are the object of study, not as authorities on the framework.

3. **Misleading-frame conditions.** MTCA-1 excluded misleading-frame conditions on ethical grounds; MTCA-2 preserves this exclusion. No condition presents SSP_v1 with fabricated or misleading provenance.

4. **Uses outside the MTCA-2 study.** This consent covers the specific study artifact identified in Section "Study identification" below. Reuse of the SSP_v1 corpus in future studies (including derivative IRMB program studies) requires separate consent obtained for the specific artifact.

5. **Silent modification of specimen text.** Any correction, normalization, or editorial change to the principle text made after corpus freeze constitutes a scope change and requires re-confirmation with Marina before implementation.

## Language discipline (binding)

The following language discipline applies to all study artifacts — pre-registration, execution notebooks, synthesis outputs, drafts, and publication:

- The study measures **model behavior**, not framework validity.
- Findings are stated in the form "the council models reason about SSP_v1 principles in ways that Z" — not "the framework is X" or "the framework claims Y".
- Council model outputs are described as the object of study, not as verdicts.
- Any finding that would risk being read as a verdict on the framework is reframed as a model-behavior claim before publication.

This language discipline is also embedded in the MTCA-2 pre-registration document (Section 2) and is binding on the study as pre-registered.

## Study identification

The consent recorded herein applies specifically to the study artifact identified by the following anchor hashes at the time of pre-registration freeze:

- **Corpus JSON SHA256:** `b917f798da06cd81c03afc9e1f70bd91a0646a0ad2486b5b83530c194f2cea58`
- **Source PDF SHA256:** `89e1cb39a7166722ef777a957d3ca2d0af2751cc59083ce852331491ded2a4bd`
- **Pre-registration SHA256:** `a224b3bf88c4e8267483c1da13fd6c34e41db7faa8694b3caa55b803033107c8`

Any change to any of the above hashes without prior notice to Marina Tudor and re-confirmation of consent constitutes a scope deviation requiring documentation as a study amendment.

## Framework attribution

The Soul Sovereignty Principles™ are the intellectual work of Marina Tudor. Trademark and authorship are hers. MTCA-2 uses the framework as research specimen with permission; the study makes no claim of authorship, ownership, or interpretive authority over the framework.

## Amendment protocol

If the scope of consent needs to be modified during the study lifecycle, the modification is documented as follows:

1. Reason for modification, described in this record.
2. Date of modification (UTC).
3. Prior SHA256 of this record preserved in an amendment log.
4. New SHA256 computed and added to `MANIFEST.sha256`.
5. Marina Tudor confirms the modification before the new record is committed.

## Consent trail

- **Consent date:** June 2026 (as documented in prior study session, prior to MTCA-2 pre-registration)
- **Consent method:** direct communication (LinkedIn) between Marina Tudor and Billy R. Davis Jr.
- **Consent scope confirmed by author:** framework naming, specimen use, author-named frame condition, verbatim preservation
- **Author declined credit** for participation and characterized the collaboration as catalytic rather than authorial

---

## Record integrity

**Record SHA256:** *(computed at freeze time; recorded in `mtca-2/consent/consent_record.sha256` and `mtca-2/MANIFEST.sha256`)*
**Record location:** `mtca-2/consent/consent_record.md`
**Record commit:** committed to `mtca-research` GitHub repository as part of the MTCA-2 study artifact set
**CI verification:** `verify-integrity.yml` validates this record's hash on every push, alongside corpus, pre-registration, and manifest.

Full Force Eternal | Romans 8:28
