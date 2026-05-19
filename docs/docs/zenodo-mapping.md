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

When you publish a poster through Posters.science, the platform creates a deposit on Zenodo containing your poster file, a structured metadata file (`poster.json`), and a set of metadata fields. Some of these fields come directly from what you provided during [metadata review](./metadata). Others are added or transformed by the platform to meet Zenodo's requirements.

This page explains exactly what gets sent, what the platform adds on your behalf, and what does not transfer to Zenodo.

## How the upload works

The platform writes metadata to Zenodo in two passes. The first pass uses Zenodo's legacy deposit API, which has limited support for structured fields. A second pass then updates the record through the InvenioRDM API with richer data, including separate given/family names, all author affiliations (with ROR IDs), name types, funder names, and typed descriptions. This means the final Zenodo record is more complete than what the legacy API alone would produce.

## Fields you provide

These fields come from the metadata you review and edit before publishing. They are mapped to Zenodo's deposit format with minimal changes.

| Your metadata | What Zenodo receives |
|---------------|----------------------|
| Title | Used as the deposit title |
| Abstract or description | Used as the deposit description. If you provide a submission abstract, it is sent as an additional typed description ("abstract") through the InvenioRDM API. |
| Authors | Names, affiliations, ORCID iDs, and name type (personal or organizational) mapped to Zenodo's creator fields |
| Keywords | Collected into a flat list of keywords |
| Conference name, location, and dates | Mapped to Zenodo's conference metadata fields |
| License | Matched to a Zenodo license identifier (default: CC BY 4.0) |
| Related identifiers | DOIs of related papers or datasets, with their relationship type and resource type |
| Funding | Funder name and award number. Each grant is validated against Zenodo's awards database; see details below. |
| Language | Sent as an ISO 639-3 language code (e.g., "eng") |
| Version | Passed through directly |
| Publication year | Used as the publication date |

## Fields the platform adds

These fields are set automatically by the platform. You do not see or edit them during metadata review.

| Field | What the platform does |
|-------|------------------------|
| Resource type | Set to "poster" on every deposit |
| DOI | Pre-reserved from Zenodo before publishing. The assigned DOI is stored in your poster record on Posters.science. |
| Publication date | An "Issued" date is recorded when the poster is published to Zenodo |
| Publisher | Set to "Zenodo" (since Zenodo is the hosting repository) |
| Poster file | Your original PDF or image, uploaded as the primary file |
| Metadata file | A `poster.json` file following the [Poster JSON Schema](./schema), included alongside your poster file |

## Fields that are modified

Some fields you provide go through formatting or validation before they reach Zenodo.

| Field | What changes |
|-------|-------------|
| Author names | Reformatted to "Family, Given" order if not already in that format. The InvenioRDM pass also sends given name and family name as separate fields. |
| Affiliations | The legacy API sends only the first affiliation per author as a plain string. The InvenioRDM pass then updates with all affiliations, including ROR identifiers where available. |
| Funding | Each grant is validated against Zenodo's awards database. Grants that match a known award use Zenodo's canonical identifier. The InvenioRDM pass also sends funder name (with optional ROR-based funder ID), award number, and award title. Grants with no Zenodo match are still preserved in the poster.json file. |
| Conference dates | Start and end dates are combined into a single date range string (e.g., "2025-10-15 - 2025-10-17"). |

## Fields that stay in poster.json only

These poster-specific fields have no equivalent in Zenodo's metadata format. They are preserved in the `poster.json` file that is deposited alongside your poster, but they do not appear in Zenodo's metadata record.

| Field | Why it is not in Zenodo |
|-------|------------------------|
| Poster content sections | Zenodo has no structured field for section-level poster text |
| Image captions | No equivalent metadata field in Zenodo |
| Table captions | No equivalent metadata field in Zenodo |
| Research field | No direct match in Zenodo's metadata. Included in the poster.json for discovery through the Posters.science registry. |

## Full field-by-field crosswalk

For a detailed technical mapping between the Poster JSON Schema and the Zenodo REST API, including transform rules and implementation notes, see the [crosswalk in the poster-json-schema repository](https://github.com/fairdataihub/poster-json-schema/blob/main/crosswalk/zenodo.md).
