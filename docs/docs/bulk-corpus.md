---
lang: en-US
title: Bulk Corpus
description: Downloadable license-separated corpora of the Posters.science registry
head:
  - - meta
    - name: og:image
      content: https://kalai.fairdataihub.org/api/generate?title=Posters.science%20Documentation&description=Bulk%20Corpus&app=posters-science&org=fairdataihub
---

# Bulk Corpus

The Posters.science registry is published for bulk download as **five corpora**, separated by license. If you want to analyse posters at scale, train on them, or mirror the registry, this is how to get the data without scraping the site.

Every poster appears in exactly one corpus, chosen by its own license. Nothing is duplicated across them.

## What a record contains

This is the part that matters most before you download.

Every record carries **repository deposit metadata**: the information the poster's home repository (Zenodo, Figshare, or another registry) published alongside it:

> title, creators and affiliations, DOI and other identifiers, publication date, publisher, subjects, language, conference details, funding references, and the poster's own license

This metadata is openly licensed regardless of the poster's terms, because deposit metadata from Zenodo and Figshare is itself CC0.

Some records **additionally** carry content read out of the poster file itself:

> section titles and section text, image captions, table captions, the submitted abstract, the research field, and a thumbnail image

Extracting that content produces a derivative work, so it is only included where the poster's license permits redistributing derivatives. Where it does not, the record ships with repository metadata alone.

Every record states which kind it is:

```json
"metadataOnly": true   // repository metadata only
"metadataOnly": false  // repository metadata + content extracted from the poster
```

::: tip
If your use case only needs bibliographic data such as counting posters, mapping conferences, analysing authorship then every record in every corpus is usable. If you need poster text, filter on `metadataOnly: false`.
:::

## How the corpora are licensed

A corpus license is an offer to whoever downloads it, so each corpus carries a license that everything inside it can legitimately be shared under. That is why the split exists: ShareAlike posters cannot be redistributed under plain CC-BY, and NonCommercial posters cannot be redistributed under a license that permits commercial use.

The reasoning behind the split is described in [How posters are redistributed](/docs/docs/auto-registration#how-posters-are-redistributed).

Each record also keeps its own license in `rightsList`. **That per-poster license is what governs your reuse of that particular poster.** The corpus license reflects the most restrictive license among the posters whose content it carries.

## The five corpora

Counts as of **August 13th, 2026**.

| Corpus | Released under | Contains | Poster content | Posters |
|--------|----------------|----------|----------------|---------|
| **Corpus 1: CC0** | CC0-1.0 | Public domain posters, plus metadata-only records for every license that does not permit redistributing extracted content | Mixed | 1,599 |
| **Corpus 2: CC-BY** | CC-BY-4.0 | CC Attribution posters (all versions) and permissive software licenses | Yes | 28,727 |
| **Corpus 3: CC-BY-SA** | CC-BY-SA-4.0 | ShareAlike posters | Yes | 313 |
| **Corpus 4: CC-BY-NC** | CC-BY-NC-4.0 | NonCommercial posters | Yes | 364 |
| **Corpus 5: CC-BY-NC-SA** | CC-BY-NC-SA-4.0 | NonCommercial ShareAlike posters | Yes | 120 |

DOIs are *(pending)* until the first release is deposited.

### Corpus 1: CC0

- **Released under:** CC0-1.0
- **Posters:** 1,599

This corpus does two jobs, so it is the only one with a mixed content status.

**790 records carry full content**: posters whose own license is a public domain dedication, so their extracted content can be released under CC0 without qualification.

| License | Posters |
|---------|---------|
| CC0-1.0 | 789 |
| CC-PDDC | 1 |

**809 records are metadata-only.** These are posters whose license does not permit us to redistribute content extracted from the poster file. Their deposit metadata is still CC0, which is why they can travel here and remain listed, searchable and citable.

| Why the content is withheld | Posters |
|-----------------------------|---------|
| No-Derivatives (CC-BY-ND, CC-BY-NC-ND, all versions) | 400 |
| Rights statements (All Rights Reserved, In Copyright, Copyright not evaluated, Copyright undetermined, other-at, other-closed, other-nc) | 249 |
| No license recorded | 124 |
| Copyleft software licenses (GPL, LGPL, AGPL) | 24 |
| `other-open`: Zenodo's "open access" designation, which states no terms to evaluate | 11 |
| Public domain, but no content available to publish | 1 |

::: info
Copyleft software licenses permit extraction, but require any derivative to be distributed under the same license. Because we do not publish a GPL-licensed corpus, those posters are included as metadata only.
:::

### Corpus 2: CC-BY

- **Released under:** CC-BY-4.0
- **Source of content:** Repository metadata and full extraction from the poster file
- **Posters:** 28,727 (28,721 with content, 6 metadata-only)

Posters under licenses that permit an adaptation to be released under different terms, provided the original copyright and permission notices travel with the record. They do, in each record's `rightsList`.

| License | Posters |
|---------|---------|
| CC-BY-4.0 | 28,617 |
| MIT | 57 |
| Apache-2.0 | 22 |
| CC-BY-3.0 (including ported variants such as 3.0-US) | 18 |
| CC-BY-2.0 | 7 |
| other-pd (Zenodo public domain designation) | 4 |
| BSD-2-Clause, BSD-3-Clause | 2 |

The 6 metadata-only records here are posters whose license permits content but for which no extracted content is available.

### Corpus 3: CC-BY-SA

- **Released under:** CC-BY-SA-4.0
- **Source of content:** Repository metadata and full extraction from the poster file
- **Posters:** 313

ShareAlike requires adaptations to be licensed under the same terms, so these posters cannot travel in the CC-BY corpus. `CC-BY-SA-4.0` (312) and `CC-BY-SA-2.0` (1).

### Corpus 4: CC-BY-NC

- **Released under:** CC-BY-NC-4.0
- **Source of content:** Repository metadata and full extraction from the poster file
- **Posters:** 364

NonCommercial posters. `CC-BY-NC-4.0` (359), plus `CC-BY-NC-3.0` (4) and `CC-BY-NC-1.0` (1).

### Corpus 5: CC-BY-NC-SA

- **Released under:** CC-BY-NC-SA-4.0
- **Source of content:** Repository metadata and full extraction from the poster file
- **Posters:** 120

ShareAlike and NonCommercial restrict different things: ShareAlike governs how you must license anything you build from a poster, while NonCommercial governs whether you may use it commercially. A poster carrying both belongs in neither Corpus 3 nor Corpus 4, so it gets its own.

`CC-BY-NC-SA-4.0` (110), `CC-BY-NC-SA-2.0` (7), `CC-BY-NC-SA-1.0` (3).

## Licenses held back from every corpus

A small number of posters ship in **no corpus at all**. This is a different category from the metadata-only records in Corpus 1: those have a license we can evaluate, which tells us to withhold the content. These have a rights value we cannot evaluate, so we make no claim about them either way pending review.

As of August 13th, 2026 this affects **33 posters**:

| Value in the rights field | Posters | Why |
|---------------------------|---------|-----|
| zenodo-freetoread-1.0 | 6 | Grants reading only, with no derivative or redistribution right |
| CC-NC | 6 | Not a valid Creative Commons identifier; the intended license is ambiguous |
| notspecified | 3 | No license declared |
| AFL-3.0, Etalab-2.0, ODC-BY, ODC-PDDL, RPL-1.5, OCCT-PL | 7 | Open licenses awaiting review before being assigned to a corpus |
| EU-EMI, ICEA IST-027819-IP, ICES Custom Licence, Publisher's own licence | 6 | Custom or institutional terms with no published text to evaluate |
| Free text | 5 | The rights field holds a grant code, project title, or contact message rather than a license |

These posters remain in the registry and are searchable and citable on the site. They are simply excluded from bulk download until their terms are resolved. Values in the last two rows are reported back to the source repository as metadata errors.

## Record format

Each corpus is a directory of [NDJSON](https://github.com/ndjson/ndjson-spec) files: one JSON object per line, chunked into numbered files of 1,000 records.

```text
corpus-cc0/1.ndjson
corpus-cc-by/1.ndjson … 29.ndjson
manifest.json
```

Each line has this shape:

```json
{
  "id": 4,
  "posterUrl": "https://posters.science/discover/4",
  "imageUrl": "https://cdn.posters.science/thumbnails/a/zenodo_14223614.jpeg",
  "publishedAt": "2024-11-26T00:00:00.000Z",
  "license": "CC-BY-4.0",
  "metadataOnly": false,
  "posterJson": { }
}
```

| Field | Notes |
|-------|-------|
| `id` | Posters.science registry identifier |
| `posterUrl` | Link to the poster's page on the site |
| `imageUrl` | Thumbnail. **Present only on records with content** |
| `publishedAt` | Publication date from the source repository |
| `license` | The poster's own license, normalised to an SPDX identifier where one exists |
| `metadataOnly` | Whether content was extracted from the poster file |
| `posterJson` | The full record, following [the poster schema](https://posters.science/schemas/) |

`manifest.json` accompanies each release with the generation timestamp, per-corpus record and file counts, and the license distribution.

## Citing the corpus

Each corpus is deposited on Zenodo with its own DOI, so you can cite the exact version you used. DOIs will be listed here once the first release is deposited.

If you use individual posters rather than the corpus as a whole, cite the posters themselves as each record carries its own DOI.
