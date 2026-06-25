---
lang: en-US
title: Metrics
description: How the numbers on the Posters.science metrics page are calculated
head:
  - - meta
    - name: og:image
      content: https://kalai.fairdataihub.org/api/generate?title=Posters.science%20Documentation&description=Metrics&app=posters-science&org=fairdataihub
---

# Metrics

The [metrics](https://posters.science/metrics) page gives a public, high-level view of what's in the Posters.science registry. It shows how many posters have been shared, how many researchers and institutions are represented, which licenses and funders show up most often, and more. This page explains how each of those numbers is calculated, what's included, and what's excluded, so you can interpret and validate them with confidence.

All numbers come from the platform's own database of poster records. They are recomputed once a day and the page shows a **Last updated** timestamp so you can see how fresh the snapshot is.

::: info
**One filter applies everywhere:** only posters with status **published** are counted. Drafts and locally downloaded posters are excluded from every metric on this page.
:::

## Platform totals

The two cards at the top of the page split published posters by how they entered the registry:

- **Manually Shared**: posters uploaded directly by researchers through the [upload flow](./upload).
- **Auto-Indexed**: posters that the platform's automated pipeline discovered and indexed from external repositories. See [Auto-Registration](./auto-registration) for how that pipeline works.

Together these two numbers add up to the total number of published posters, which is also the denominator used for the **Open Science adoption** percentages further down the page.

## Posters by Publication Year

The bar chart counts published posters by the **publication year** recorded on each poster's metadata.

- **Included:** publication years from **2000 through the current year**.
- **Excluded:** posters with no publication year, or with a year outside that range.

## Community counters

These animated counters describe the breadth of the community represented in the registry.

### Researchers

The number of **distinct authors** that appear on published posters.

Each author entry is reduced to a single identity using these rules, in order:

1. If the entry has a non-empty **ORCID** identifier, the ORCID is used as the author's identity. The same ORCID across multiple posters is always counted as one researcher, even if the author's name is spelled or abbreviated differently from poster to poster.
2. Otherwise, the entry's **name** is used. Names are compared after trimming whitespace and lowercasing, so casing or spacing differences (for example, `Jane Doe` vs. `jane doe`) collapse to the same researcher.
3. Entries with no ORCID and no usable name are skipped.

Note that when the same person appears on some posters with an ORCID and on others without one, the two appearances cannot always be linked and may still count as two researchers.

### Institutions

The number of **unique institutional affiliations** listed for any author on a published poster.

- Names are compared after trimming whitespace and lowercasing, so `MIT` and `mit ` collapse to one entry.
- **Excluded:** empty strings, names made entirely of digits, and common placeholders: `institution name`, `null`, `unknown`, `none`, `n/a`, `not specified`, `notspecified` (case-insensitive).
- Deduplication uses the **name string only**. ROR identifiers are not currently used to merge entries.

### Languages

The number of **distinct, non-empty language values** across published posters. Languages with a missing or blank value are not counted.

### Unique Funders

The number of distinct **funders** mentioned in poster funding references, after a canonicalization step that merges common name variants.

- **Excluded:** empty funder names and common placeholder values (case-insensitive): `unknown funder`, `unknown`, `not specified`, `notspecified`, `FUNDER`, `not applicable`, `no funding`, `none`, `n/a`.
- **Canonicalization** merges well-known variants so they don't fragment the count. For example:
  - `NSF` and other spellings of *National Science Foundation* are merged into **U.S. National Science Foundation**. Safeguards prevent this merge when the funder is clearly the Swiss, Swedish, or Chinese NSF, or when the mention refers to an event or meeting rather than the funder itself.
  - Variants of *National Institutes of Health* (`NIH`, etc.) are merged into **National Institutes of Health**.
  - Variants of *Environmental Protection Agency* are merged into **U.S. Environmental Protection Agency**.

## Open Science adoption

Three percentages measure how often published posters carry the persistent identifiers that make science findable and reusable. Each is computed as:

> **(matching posters / total published posters) × 100**

The denominator is the total number of published posters (Manually Shared plus Auto-Indexed combined), so you can reproduce each percentage from the platform totals.

- **With a DOI**: posters whose metadata includes a non-empty DOI.
- **With at least 1 ORCID author**: posters where at least one author entry includes an ORCID identifier.
- **With at least 1 ROR institution**: posters where at least one author affiliation carries a non-empty ROR identifier.

## Distribution charts

These charts show how published posters are distributed across licenses, languages, institutions, funders, publishers, and subjects.

### License Distribution (donut)

Licenses are normalized into canonical SPDX-style identifiers before counting, so that variants describing the same license collapse to one slice. Examples of the normalization:

- `cc-by-4`, `cc_by_4.0`, `CC BY 4.0` are normalized to **CC-BY-4.0**.
- `cc0`, `cc-zero`, `public-domain` are normalized to **CC0-1.0**.
- `apache 2`, `apache-2` are normalized to **Apache-2.0**.
- `mit`, `mit-license` are normalized to **MIT**.

**Excluded values:**

- Rights statements and non-license placeholders (case-insensitive): `in copyright`, `copyright not evaluated`, `copyright undetermined`, `all rights reserved`, `unknown`, `n/a`, `none`, `not specified`, `notspecified`.
- The Zenodo "other-*" buckets that don't map to a real license: `other-at`, `other-open`, `other-closed`, `other-pd`, `other-nc`.
- Any value longer than 60 characters, or that looks like prose rather than a license identifier (containing grant numbers, citations, URLs, email addresses, "et al.", copyright dates, etc.). These show up when a free-text acknowledgement was entered into the license field by mistake.

The chart shows the **top 3 licenses**, with everything else aggregated into an **Other** slice.

### Language Distribution (donut)

Language codes are mapped to human-readable names using the ISO 639-1 standard (for example, `en` becomes English, `es` becomes Spanish). The chart shows the **top 3 languages**, with everything else aggregated into an **Other** slice.

### Top Institutions (bar)

The same normalization rules as the [Institutions](#institutions) counter apply (trimmed, lowercased, with placeholder and digit-only entries removed). Each bar represents the number of distinct published posters that list that institution among their author affiliations. The chart shows the **top 10**.

### Top Funders (bar)

The same canonicalization as the [Unique Funders](#unique-funders) counter applies, so variants of the same funder are merged. The chart shows the **top 15** funders by number of distinct published posters that mention them.

### Top Publishers and Repositories (bar)

Publisher names are cleaned before grouping so that small formatting differences don't split the same publisher across multiple bars:

- Trailing country or agency tags such as `(United Kingdom)` or `(EPA)` are stripped.
- Trailing top-level domains (`.com`, `.org`, `.net`, `.io`, `.edu`, `.gov`) are stripped.
- Case-insensitive variants are merged.

The chart shows the **top 10** publishers and repositories.

### Top Subjects and Keywords (word cloud)

Each published poster's list of subjects and keywords is flattened, and the **top 20** subjects by frequency are rendered as a word cloud. Larger words appear more often across the registry.

## Refresh schedule

The numbers on the page come from a **snapshot** that is recomputed once a day at **08:00 UTC** rather than re-running every time the page is loaded. This keeps the page fast and consistent for all visitors, but means that posters published or edited after the most recent snapshot won't be reflected in the metrics until the next run. The **Last updated** timestamp at the bottom of the metrics page shows when the current snapshot was generated.

<!-- ## Validating the numbers yourself

::: info
You can spot-check most of these numbers by browsing the [registry](./search) directly. The discover page lets you filter by **publication year, language, license, institution,** and **funder**, as well as by source (Zenodo, Figshare, user-submitted) and published date. The dropdown values use the same canonicalization and exclusions as the metrics charts, so what you see in a filter dropdown lines up with what contributes to the corresponding chart. Filter options are sorted by **most-cited first**, so the highest-impact values appear at the top.
:::

::: warning
A few things to keep in mind when reading the numbers:

- The **Researchers** counter uses ORCID when available and a case-insensitive name match otherwise. If the same author appears on some posters with an ORCID and on others without one, the two appearances may still count as two researchers.
- **Institution** deduplication uses the affiliation name string. ROR identifiers are recorded on poster records but are not yet used to merge institution entries.
- The **Top Subjects and Keywords** chart shows raw subject strings without normalization, so spelling or casing variants of the same keyword may appear as separate words. Because of that, subjects are not yet offered as a filter on the discover page.
::: -->
