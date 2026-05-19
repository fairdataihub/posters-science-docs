---
lang: en-US
title: The Poster Schema
description: Understanding the poster JSON schema
head:
  - - meta
    - name: og:image
      content: https://kalai.fairdataihub.org/api/generate?title=Posters.science%20Documentation&description=The%20Poster%20Schema&app=posters-science&org=fairdataihub
---

# The Poster Schema

Every poster shared through Posters.science is described by a structured JSON file that follows the [Poster JSON Schema](https://github.com/fairdataihub/poster-json-schema). This schema defines what metadata fields exist, what they mean, and how they should be formatted.

## Why a schema?

Scientific posters have historically been treated as unstructured PDFs. Without standardized metadata, a poster is hard to search, cite, or analyze at scale. The Poster JSON Schema gives each poster a machine-readable description that makes it discoverable and interoperable with other research systems.

The schema was developed in collaboration with the [University of California Curation Center (UC3)](https://uc3.cdlib.org/) and [DataCite](https://datacite.org/), and has gone through multiple rounds of expert feedback.

## Built on DataCite

The schema is based on the [DataCite Metadata Schema](https://schema.datacite.org/) (version 4.7), the same standard used to describe over 150 million DOI-registered research objects worldwide. This means poster metadata can be mapped to DataCite records and Zenodo deposits without losing information.

The DataCite core provides fields for:

| Field | Description |
|-------|-------------|
| `titles` | Poster title |
| `creators` | Author names, affiliations, ORCID iDs |
| `descriptions` | Abstract or summary |
| `subjects` | Keywords |
| `dates` | Presentation date, publication date |
| `rights` | License information |
| `fundingReferences` | Grants and funding agencies |
| `relatedIdentifiers` | DOIs of related papers or datasets |

## Poster-specific extensions

On top of the DataCite core, the schema adds fields specific to scientific posters:

- **Conference**: Name, acronym, location, dates, and conference identifiers. This captures where the poster was presented.
- **Research field**: The broad domain of the work (e.g., "Ophthalmology," "Bioengineering").
- **Content**: The actual text content of the poster, organized into titled sections with body text.
- **Image captions**: Descriptions of figures and images that appear on the poster.
- **Table captions**: Descriptions of tables on the poster.
- **Ethics approvals**: IRB or ethics committee certifications mentioned on the poster.

## How fields are populated

Each field in the poster schema is populated by one or more sources. Some are extracted from the poster by the AI pipeline, some are assigned automatically by the platform, and some are filled in or edited by the user in the metadata review step.

### Fields you can review and edit

These fields are presented in the metadata editor. They may be pre-filled by the extraction pipeline, but you can always change them.

| Field | How it is pre-filled |
|-------|----------------------|
| Title | Extracted from the poster |
| Description / abstract | Extracted from the poster |
| Authors (name, given name, family name) | Extracted from the poster |
| Author name type (personal or organizational) | Not pre-filled; you select it |
| Author ORCID iDs | Looked up via the ORCID registry based on extracted names |
| Author affiliations and ROR IDs | Extracted from the poster; ROR IDs looked up from affiliation names |
| Keywords | Extracted from the poster |
| Conference (name, location, dates, acronym, URL) | Extracted from the poster if conference info is present |
| Related identifiers | Extracted from DOIs and URLs found in the poster text and PDF link annotations |
| Related identifier type, relation type, resource type | Auto-classified from the identifier format; editable |
| Funding (funder name, award number, funder ID) | Extracted from the poster text; cross-referenced against funder databases |
| Language | Auto-detected from the poster text |
| Domain / field of study | Auto-classified based on poster content |
| Poster content sections | Extracted section titles and body text from the poster |
| Image and table captions | Extracted from the poster |

::: tip
Some of these fields are inside collapsible sections labeled "Optional" or "Auto-extracted" in the metadata editor. Open these sections to review auto-filled values like language, domain, related identifiers, and poster content before continuing.
:::

### Fields set automatically (not shown in the editor)

These fields are managed by the platform. They do not appear in the metadata editor.

| Field | What the platform does |
|-------|------------------------|
| DOI | Assigned when the poster is published to Zenodo |
| Publisher | Set to "Zenodo" when archiving to Zenodo |
| Publication year | Derived from the publication date |
| Dates | "Issued" date recorded when the poster is published to a repository |
| Resource type | Set to "Poster" |
| Format | Set based on the uploaded file type (PDF, PNG, etc.) |
| Version | Defaults to "1" for new deposits |
| License | Selected during the publishing step (not in the metadata editor) |
| Identifier type | Auto-classified as DOI or URL based on the identifier string |
| Description type | Set to "Abstract" by default |
| Scheme metadata (ORCID scheme, ROR scheme, etc.) | Auto-populated when identifiers are present |

## Date types

The schema supports several date types from the DataCite standard. For posters shared through Posters.science, only a few are used in practice:

| Date type | When it is recorded |
|-----------|---------------------|
| Issued | When the poster is published and made publicly available (on Zenodo, Figshare, etc.) |
| Submitted | When the poster was uploaded to the repository |
| Presented | The date the poster was presented at a conference (derived from conference dates when available) |

The schema also allows other DataCite date types (Accepted, Available, Collected, Copyrighted, Coverage, Created, Updated, Valid, Withdrawn) for future use and interoperability, but these are not currently populated by the platform.

## Versioning

The schema follows [semantic versioning](https://semver.org/). The current version is **[v0.2](https://doi.org/10.5281/zenodo.20125306)**. Each release is archived on Zenodo with its own DOI, and the schema repository maintains a [changelog](https://github.com/fairdataihub/poster-json-schema/blob/main/CHANGELOG.md) documenting every change.

::: info
The schema is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), which means you can use and adapt it for your own purposes with attribution.
:::
