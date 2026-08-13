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

The machine actionable version of the registry, the poster records as JSON, is archived
periodically on Zenodo for bulk download. If you want to analyse posters at scale, train on
them, or mirror the registry, this is how to get the data without scraping the site.

The archive is published as **five corpora rather than one**. Each poster carries its own
license, and a deposit's license is an offer to whoever downloads it, so a single archive
could not honour every poster inside it. Splitting the release means each corpus is shared
under a license that aligns with the licenses of the posters it contains. Every poster
appears in at most one corpus, so nothing is duplicated across them.

## The corpora

| Corpus | Released under | Posters | Version | Released | DOI |
|--------|----------------|---------|---------|----------|-----|
| 1. CC0 | CC0-1.0 | 1,599 | 2026-08-13 | 2026-08-13 | [10.5281/zenodo.21924695](https://doi.org/10.5281/zenodo.21924695) |
| 2. CC-BY-4.0 | CC-BY-4.0 | 28,727 | 2026-08-13 | 2026-08-13 | [10.5281/zenodo.21924848](https://doi.org/10.5281/zenodo.21924848) |
| 3. CC-BY-SA 4.0 | CC-BY-SA-4.0 | 313 | 2026-08-13 | 2026-08-13 | [10.5281/zenodo.21925147](https://doi.org/10.5281/zenodo.21925147) |
| 4. CC-BY-NC 4.0 | CC-BY-NC-4.0 | 364 | 2026-08-13 | 2026-08-13 | [10.5281/zenodo.21925170](https://doi.org/10.5281/zenodo.21925170) |
| 5. CC-BY-NC-SA 4.0 | CC-BY-NC-SA-4.0 | 120 | 2026-08-13 | 2026-08-13 | [10.5281/zenodo.21925181](https://doi.org/10.5281/zenodo.21925181) |

Each poster keeps its own license in its record, and that per-poster license is what governs
reuse of that poster. The corpus level license reflects the most restrictive license among
the posters it carries.

A small number of posters ship in no corpus at all, because the value in their rights field
is one we cannot evaluate yet. They remain in the registry and are searchable and citable on
the site.

## What is in a record

Every record carries the **repository metadata** its home repository published: title,
creators and affiliations, DOI and other identifiers, dates, publisher, subjects, language,
conference details, funding references, and the poster's own license.

Most records additionally carry **poster extracted metadata**, meaning the structured
metadata and content read out of the poster file itself. Producing that is a derivative
work, so it is included only where the poster's license permits redistributing derivatives.
Where it does not, the record ships with repository metadata only. Each record states which
kind it is.

For the fields and their meanings, see [The Poster Schema](/docs/schema). For how each
license is evaluated and which corpus it maps to, see
[Auto-Registration](/docs/auto-registration#how-posters-are-redistributed).

## Citing a corpus

Each corpus has its own DOI, so you can cite the exact release you used. If you use
individual posters rather than a corpus as a whole, cite the posters themselves, as every
record carries its own DOI.
