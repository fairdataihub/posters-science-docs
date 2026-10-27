---
lang: en-US
title: Zenodo Deposit Details
description: What metadata Posters.science sends to Zenodo and what it adds on your behalf
head:
  - - meta
    - name: og:image
      content: https://kalai.fairdataihub.org/api/generate?title=Posters.science%20Documentation&description=Zenodo%20Deposit%20Details&app=posters-science&org=fairdataihub
---

# Zenodo Deposit Details

When you publish a poster through Posters.science, the platform creates a record on Zenodo containing your poster file, a structured metadata file (`poster.json`), and a set of metadata fields. Some of these fields come directly from what you provided during [metadata review](./metadata). Others are added or transformed by the platform to meet Zenodo's requirements.

This page explains exactly what gets sent, what the platform adds on your behalf, and what does not transfer to Zenodo.

## How the upload works

The platform uses Zenodo's current API (InvenioRDM) for the whole upload:

1. It creates a draft record on your Zenodo account.
2. It writes all of your metadata to the draft in one step, including separate given and family names, all author affiliations (with ROR IDs), name types, funders and awards.
3. It reserves the DOI.
4. It uploads your poster file and `poster.json`.
5. It publishes the record.

If you publish a new version of a poster that is already on Zenodo, the platform creates a new version of the same Zenodo record, so both versions stay linked there.

## Fields you provide

These fields come from the metadata you review and edit before publishing. They are mapped to Zenodo's format with minimal changes.

| Your metadata | What Zenodo receives |
|---------------|----------------------|
| Title | Used as the record title |
| Description | Used as the record description |
| Submission abstract | Sent as an additional description of type "Abstract" |
| Authors | Given and family names, name type (personal or organizational), ORCID iDs, and all affiliations with their ROR IDs |
| Keywords | Sent as Zenodo keywords (free-text subjects) |
| Conference name, acronym, location, website, and dates | Sent as Zenodo's meeting (conference) details |
| Presentation date | Sent as a date with the description "Poster presentation date" |
| License | Matched to a Zenodo license identifier (default: CC BY 4.0) |
| Related identifiers | DOIs or links of related papers, datasets, or software, with their relationship type and resource type |
| Funding | Funder name and ROR ID, award number, award title, and award link |
| Language | Sent as a three-letter language code (e.g., "eng") |
| Version | The version you choose when publishing (e.g., "2"). If you leave it empty, the platform fills it in ("1" for the first version). |

## Fields the platform adds

These fields are set automatically by the platform. You do not see or edit them during metadata review.

| Field | What the platform does |
|-------|------------------------|
| Resource type | Set to "Poster" on every record |
| Publisher | Set to "Zenodo", since Zenodo is the hosting repository |
| DOI | Reserved from Zenodo before publishing. The assigned DOI is stored in your poster record on Posters.science. |
| Publication date | The year the poster is published to Zenodo |
| Submitted date | The day the poster is shared to Zenodo, with the description "Submitted to Zenodo through Posters.science" |
| Link to Posters.science | A related identifier pointing to the poster's page on Posters.science ("is described by") |
| Previous version | For a new version, a related identifier pointing to the DOI of the version before it ("is new version of") |
| Poster file | Your original PDF or image, uploaded as the primary file |
| Metadata file | A `poster.json` file following the [Poster JSON Schema](./schema), included alongside your poster file |

## Fields that are modified

Some fields you provide go through formatting or validation before they reach Zenodo.

| Field | What changes |
|-------|-------------|
| Author names | Sent as separate given and family names. If only a full name is available in "Family, Given" form, it is split at the comma. |
| ORCID iDs | Checked for a valid format and checksum. An iD that fails the check is left out of the Zenodo record. If an iD cannot be found in the ORCID registry, you see a warning, but publishing continues. |
| Affiliations and funders | If Zenodo does not recognize a ROR ID, the platform sends that metadata again with names only, so the record still publishes. |
| Funding | An award link needs an award number or an award title. If a funding entry has only a link, publishing stops and asks you to complete it. |
| Related identifiers | Relationship and resource types are translated into Zenodo's terms. An identifier Zenodo cannot accept (for example, a DOI that is not in the 10.xxxx/ form) is left out. |
| Conference dates | Start and end dates are combined into a single date range (e.g., "2026-07-14 - 2026-07-16"). |
| Version | A leading "v" is removed ("v2" becomes "2"). |

## Fields that stay in poster.json only

These fields are not part of Zenodo's metadata record. They are preserved in the `poster.json` file that is deposited alongside your poster.

| Field | Why it is not in Zenodo |
|-------|------------------------|
| Poster content sections | Zenodo has no structured field for section-level poster text |
| Image captions | No equivalent metadata field in Zenodo |
| Table captions | No equivalent metadata field in Zenodo |
| Research field | Not sent to Zenodo. Included in the poster.json for discovery through the Posters.science registry. |
| Other identifiers of the poster | Identifiers such as an earlier DOI or an arXiv ID are kept in poster.json but not yet sent to Zenodo |

## Full field-by-field crosswalk

For a detailed technical mapping between the Poster JSON Schema and Zenodo, including transform rules and implementation notes, see the [crosswalk in the poster-json-schema repository](https://github.com/fairdataihub/poster-json-schema/blob/main/crosswalk/zenodo.md).
