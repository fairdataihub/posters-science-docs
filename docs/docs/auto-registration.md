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

Tens of thousands of scientific posters are already published across open repositories. As of early 2026, Zenodo hosts over 17,000 poster records and Figshare hosts over 7,000. These posters are already publicly available, but they are scattered across different platforms with inconsistent metadata. Auto-registration brings them together into a single searchable registry.

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

Extracting structured metadata from a poster using AI constitutes a derivative work. The platform checks each poster's license before processing. If the license does not clearly grant permission to redistribute derivatives, no content is extracted from the poster file. Only repository metadata is retained.

### Included licenses

Posters published under the following licenses permit derivative works. For these posters, the platform performs full PDF extraction (structured text, captions, research field), collects repository metadata, and generates a thumbnail.

| Category | Licenses |
|----------|----------|
| Public domain | CC0-1.0 |
| CC Attribution | CC-BY-4.0, CC-BY-3.0, CC-BY-2.5, CC-BY-2.0, CC-BY-1.0 |
| CC Attribution-ShareAlike | CC-BY-SA-4.0, CC-BY-SA-3.0, CC-BY-SA-2.5, CC-BY-SA-2.0 |
| CC Attribution-NonCommercial | CC-BY-NC-4.0, CC-BY-NC-3.0, CC-BY-NC-2.5, CC-BY-NC-2.0 |
| CC Attribution-NonCommercial-ShareAlike | CC-BY-NC-SA-4.0, CC-BY-NC-SA-3.0, CC-BY-NC-SA-2.5, CC-BY-NC-SA-2.0 |
| Software (permissive) | MIT, Apache-2.0, BSD-2-Clause, BSD-3-Clause, ISC, Unlicense, MPL-2.0 |
| Software (copyleft) | GPL-3.0, GPL-2.0, LGPL-3.0, LGPL-2.1 |
| Zenodo non-SPDX | other-open, other-pd |

### Excluded licenses

Posters under the following licenses do not grant permission to create or redistribute derivatives. No content is extracted from the poster file for these posters. Only repository metadata is retained (identifiers, authors, title, dates, publisher, license, funding, conference).

| Category | Licenses | Reason |
|----------|----------|--------|
| No-Derivatives | CC-BY-ND, CC-BY-NC-ND (all versions) | ND explicitly prohibits derivative works |
| Restrictive | All Rights Reserved, In Copyright | No redistribution permitted |
| Unresolved | Copyright not evaluated, Copyright undetermined | Cannot confirm permission |
| Unknown terms | other-at, other-closed, other-nc, other | No defined license terms to evaluate |
| Missing | No license specified | Cannot confirm permission; treated as restrictive |

### New licenses

Licenses not listed in either category are added to a waiting list for manual review before any extraction is performed.

::: info
The full license policy with implementation details is maintained in the [extraction pipeline repository](https://github.com/fairdataihub/poster-repo-to-json/blob/main/docs/LICENSE_POLICY.md).
:::

## Registry coverage

As of early 2026, the registry contains over 24,000 posters from automated collection, in addition to posters submitted directly through the platform. This makes Posters.science one of the largest searchable indexes of scientific posters available.
