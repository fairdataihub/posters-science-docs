---
lang: en-US
title: Metadata Extraction
description: How Posters.science extracts metadata from scientific posters
head:
  - - meta
    - name: og:image
      content: https://kalai.fairdataihub.org/api/generate?title=Posters.science%20Documentation&description=Metadata%20Extraction&app=posters-science&org=fairdataihub
---

# Metadata Extraction

When you upload a poster, the platform reads it and extracts structured metadata automatically. This page explains what happens during that process and why the results are generally accurate enough to publish with minimal editing.

## The extraction pipeline

Extraction happens in two stages:

1. **Text extraction**: The raw text is pulled from your poster file. For PDFs, a tool called [pdfplumber](https://github.com/jsvine/pdfplumber) reads the embedded text layer and reconstructs the reading order across multi-column layouts. For images (PNG and JPEG), a vision model reads the visible content using OCR.

2. **Structured extraction**: The raw text is passed to a large language model (LLM) that identifies and organizes the information into schema fields: title, authors, affiliations, abstract, funding, conference details, and more.

The LLM is given detailed instructions about what to look for and how to format the results. It uses examples of correctly extracted posters to guide its output.

## The language model

Posters.science uses [poster2json](https://github.com/fairdataihub/poster2json), an open source tool built specifically for this task. The extraction model is optimized for the layout and language patterns found on scientific posters, which differ from journal articles or web pages.

The model runs on local GPU hardware maintained by the FAIR Data Innovations Hub. No poster content is sent to third-party AI services.

::: info
The extraction tool and its validation results are published openly. You can review the methodology and performance data in the [poster2json repository](https://github.com/fairdataihub/poster2json).
:::

## External database lookups

After the initial extraction, the platform cross-references extracted values against external databases to improve accuracy:

- **ORCID**: Author names are matched against the [ORCID registry](https://orcid.org) to find researcher identifiers.
- **ROR**: Institutional affiliations are matched against the [Research Organization Registry](https://ror.org) to standardize organization names.
- **NIH Reporter and NSF**: Funding information is checked against the [NIH Reporter](https://reporter.nih.gov/) and [NSF Award Search](https://www.nsf.gov/awardsearch/) to verify grant numbers and funder names.
- **Crossref**: Related publications mentioned on the poster are looked up via [Crossref](https://www.crossref.org/) to resolve DOIs.

These lookups help improve the accuracy of the values presented during [metadata review](./metadata).

## Accuracy

The extraction tool is validated against a set of manually annotated posters covering different research domains, layouts, and languages. The validation measures:

- **Word capture**: What percentage of the text on the poster was successfully read.
- **Field accuracy**: How well the extracted fields match the ground truth annotations.
- **Number capture**: Whether numerical values (grant numbers, dates, statistics) were correctly extracted.

Current validation results show a pass rate of 95% (19 of 20 posters) across the test set. Details and per-poster results are available in the [poster2json evaluation documentation](https://github.com/fairdataihub/poster2json/blob/main/docs/evaluation.md).
