---
lang: en-US
title: Auto-Registration
description: How Posters.science indexes posters from external repositories
head:
  - - meta
    - name: og:image
      content: https://kalai.fairdataihub.org/api/generate?title=Posters.science%20Documentation&description=Auto-Registration&app=posters-science&org=fairdataihub
---

# Auto-Registration

Not every poster in the Posters.science registry was submitted through the platform. The registry also includes posters that researchers have already shared on Zenodo and Figshare. The platform finds these posters automatically and adds them to the searchable index.

## Why auto-register?

Tens of thousands of scientific posters are already published across open repositories. As of early 2026, Zenodo hosts over 24,000 poster records and Figshare hosts over 7,000. These posters are already publicly available, but they are scattered across different platforms with inconsistent metadata. Auto-registration brings them together into a single searchable registry.

## How it works

The platform uses an open source scraper called [poster-repo-scraper](https://github.com/fairdataihub/poster-repo-scraper) to collect poster records from external repositories:

1. **Zenodo**: The scraper queries the Zenodo REST API for records tagged with the `poster` resource type. It pages through results by date range to collect the full catalog.

2. **Figshare**: The scraper searches Figshare for items with the `poster` item type, collecting metadata and optionally fetching download statistics.

3. **DataCite**: The scraper queries the DataCite API to discover additional platforms publishing poster-type DOIs, which helps identify sources beyond Zenodo and Figshare.

For each record, the scraper collects the title, authors, description, DOI, keywords, license, conference metadata, and file links.

## Filtering

Not every record tagged as a "poster" in a repository is actually a scientific poster. Some are slide decks, abstracts, or other document types that were categorized incorrectly.

To handle this, collected records pass through [PosterSentry](https://github.com/fairdataihub/poster-sentry), a classifier trained to distinguish scientific posters from other document types. Records that do not pass classification are excluded from the registry.

## Update frequency

The scraper runs periodically to pick up new poster records. When a new poster appears on Zenodo or Figshare, it is typically indexed in the Posters.science registry within a few days.

::: info
Auto-registered posters display their original repository source (Zenodo or Figshare) in the registry. The platform links back to the original record so you can always access the poster from its primary home.
:::

## License policy

Extracting structured metadata from a poster using AI constitutes a derivative work. The platform checks each poster's license before processing. If the license does not clearly grant permission to redistribute derivatives, no poster extracted metadata is produced. Only repository metadata is retained.

### Included licenses

Posters published under the following licenses permit derivative works. For these posters the platform produces poster extracted metadata, meaning the structured metadata and content read out of the poster file itself (section text, captions, research field), alongside the repository metadata, and generates a thumbnail.

| Category | Licenses |
|----------|----------|
| Public domain | CC0-1.0, CC-PDDC, other-pd, ODC-PDDL |
| CC Attribution | CC-BY-4.0, CC-BY-3.0 (incl. ported, e.g. 3.0-US), CC-BY-2.5, CC-BY-2.0, CC-BY-1.0 |
| CC Attribution-ShareAlike | CC-BY-SA-4.0, CC-BY-SA-3.0, CC-BY-SA-2.5, CC-BY-SA-2.0 |
| CC Attribution-NonCommercial | CC-BY-NC-4.0, CC-BY-NC-3.0, CC-BY-NC-2.5, CC-BY-NC-2.0 |
| CC Attribution-NonCommercial-ShareAlike | CC-BY-NC-SA-4.0, CC-BY-NC-SA-3.0, CC-BY-NC-SA-2.5, CC-BY-NC-SA-2.0 |
| Software (permissive) | MIT, Apache-2.0, BSD-2-Clause, BSD-3-Clause, ISC, Unlicense, MPL-2.0 |
| Software (copyleft) | GPL-3.0, GPL-2.0, LGPL-3.0, LGPL-2.1, AGPL |

Copyleft licenses (the GPL family) permit extraction, but they require any derivative to be distributed under the same license. Because we do not publish a GPL-licensed corpus, those posters are included as repository metadata only in our published corpora. See [How posters are redistributed](#how-posters-are-redistributed) below.

### Excluded licenses

Posters under the following licenses do not grant permission to create or redistribute derivatives. No poster extracted metadata is produced for these posters. Only repository metadata is retained (identifiers, authors, title, dates, publisher, license, funding, conference), and no thumbnail is generated.

| Category | Licenses | Reason |
|----------|----------|--------|
| No-Derivatives | CC-BY-ND, CC-BY-NC-ND (all versions) | ND explicitly prohibits derivative works |
| Restrictive | All Rights Reserved, In Copyright (including "Educational Use Permitted" and "Rights-Holder Unlocatable" variants) | No redistribution permitted |
| Unresolved | Copyright not evaluated, Copyright undetermined, notspecified | Cannot confirm permission |
| Unknown terms | other-at, other-closed, other-nc, other, other-open | No defined license terms to evaluate |
| Read-only grants | zenodo-freetoread-1.0 | Grants reading only, with no derivative or redistribution right |
| Missing | No license specified | Cannot confirm permission; treated as restrictive |

### New licenses

Licenses not listed in either category are added to a waiting list for manual review before any extraction is performed. Two things commonly land there:

- **Open licenses we have not catalogued yet** (for example ODC-PDDL, AFL-3.0, Etalab-2.0, ODC-BY). These are reviewed and added to the appropriate category.
- **Values that are not licenses at all.** A small number of deposits carry a grant code, a project title, or a contact message in the rights field. These are treated as "no license specified" and reported to the source repository as a metadata error.

## How posters are redistributed

The full registry is published on Zenodo as **five license-separated corpora**. Each poster appears in exactly one, chosen by its own license. For the record counts, versions and DOIs, see [Bulk Corpus](/docs/bulk-corpus).

A deposit's license is an offer to whoever downloads it, so each corpus carries a license that everything inside it can legitimately be shared under. The deciding question for each poster is whether its license allows an adaptation to be released under different terms:

- **Permissive licenses allow it.** Public domain (CC0), plain CC Attribution, and the permissive software licenses (MIT, BSD, Apache-2.0) can be shared under CC-BY-4.0, provided the original copyright and permission notices travel with the record. They do.
- **ShareAlike and copyleft do not.** CC-BY-SA and CC-BY-NC-SA require adaptations under the same license, so they get their own corpora. GPL-family licenses require the same and have no Creative Commons equivalent, so those posters carry repository metadata only.

| Corpus | Released under | Contains | DOI |
|--------|----------------|----------|-----|
| 1. CC0 | CC0-1.0 | Public domain posters, plus the repository-metadata-only records for excluded licenses | [10.5281/zenodo.21924695](https://doi.org/10.5281/zenodo.21924695) |
| 2. CC-BY-4.0 | CC-BY-4.0 | CC Attribution posters (all versions) and permissive software licenses | [10.5281/zenodo.21924848](https://doi.org/10.5281/zenodo.21924848) |
| 3. CC-BY-SA 4.0 | CC-BY-SA-4.0 | ShareAlike posters | [10.5281/zenodo.21925147](https://doi.org/10.5281/zenodo.21925147) |
| 4. CC-BY-NC 4.0 | CC-BY-NC-4.0 | NonCommercial posters | [10.5281/zenodo.21925170](https://doi.org/10.5281/zenodo.21925170) |
| 5. CC-BY-NC-SA 4.0 | CC-BY-NC-SA-4.0 | NonCommercial ShareAlike posters | [10.5281/zenodo.21925181](https://doi.org/10.5281/zenodo.21925181) |

ShareAlike and NonCommercial restrict different things: ShareAlike governs how you must license anything you build from a poster, while NonCommercial governs whether you may use it commercially. A poster carrying both therefore belongs in neither the ShareAlike nor the NonCommercial corpus, and gets its own.

Each record keeps its own license in `rightsList`, and that per-poster license is what governs reuse of that poster. The corpus level license reflects the most restrictive license among the posters whose content it carries.

Every poster appears in exactly one corpus, so nothing is duplicated across them. A poster sits in the corpus for its own license and carries its poster extracted metadata where we hold it, or its repository metadata alone where we do not. Excluded licenses have no corpus of their own, so those repository-metadata-only records travel with the CC0 corpus.

Metadata for every poster is openly licensed regardless of the poster's own terms, because repository deposit metadata from Zenodo and Figshare is itself CC0. That is why excluded posters can still be listed, searched, and cited, just without their poster extracted metadata or thumbnail.

::: info
The full license policy with implementation details is maintained in the [extraction pipeline repository](https://github.com/fairdataihub/poster-repo-to-json/blob/main/docs/LICENSE_POLICY.md).
:::

## Registry coverage

As of early 2026, the registry contains over 24,000 posters from automated collection, in addition to posters submitted directly through the platform. This makes Posters.science one of the largest searchable indexes of scientific posters available.
