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

The schema is based on the [DataCite Metadata Schema](https://schema.datacite.org/) (version 4.7), the same standard used to describe over 10 million DOI-registered research objects worldwide. This means poster metadata can be mapped to DataCite records and Zenodo deposits without losing information.

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

## Versioning

The schema follows [semantic versioning](https://semver.org/). The current version is **v0.2**. Each release is archived on Zenodo with its own DOI, and the schema repository maintains a [changelog](https://github.com/fairdataihub/poster-json-schema/blob/main/CHANGELOG.md) documenting every change.

::: info
The schema is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), which means you can use and adapt it for your own purposes with attribution.
:::
