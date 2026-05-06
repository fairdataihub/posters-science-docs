---
lang: en-US
title: Publishing to a Repository
description: How to publish your poster to Zenodo or Figshare
head:
  - - meta
    - name: og:image
      content: https://kalai.fairdataihub.org/api/generate?title=Posters.science%20Documentation&description=Publishing%20to%20a%20Repository&app=posters-science&org=fairdataihub
---

# :package: Publishing to a Repository

The final step in sharing your poster is choosing where to publish it. Posters.science connects to trusted research repositories so your poster gets a permanent home and a citable DOI.

## :hammer_and_wrench: How to publish

1. After reviewing your metadata, click `Continue to Publishing`.
2. Select a repository: **Zenodo** or **Figshare**.
3. Review the summary of what will be deposited.
4. Click `Publish`.

The platform creates a record in your chosen repository that includes:

- Your original poster file (PDF, image, or presentation).
- A structured metadata file (`poster.json`) following the [Poster JSON Schema](./schema).
- All metadata fields mapped to the repository's native format.

::: info
Publishing is a one-way action. Once the record is created in Zenodo or Figshare, it receives a DOI and becomes publicly accessible. You can update metadata after publication, but the DOI is permanent.
:::

## :globe_with_meridians: Zenodo

[Zenodo](https://zenodo.org) is a general-purpose open repository operated by CERN. It accepts any research output, assigns DOIs through DataCite, and guarantees long-term preservation.

When you publish to Zenodo through Posters.science:

- Your poster is deposited in the [Posters.science community on Zenodo](https://zenodo.org/communities/posters-science).
- The metadata is mapped to Zenodo's deposit format, including authors, affiliations, conference details, and funding.
- A DOI is assigned automatically.

## :bar_chart: Figshare

[Figshare](https://figshare.com) is a repository for research outputs including figures, datasets, and posters. It also assigns DOIs and provides usage metrics like views and downloads.

When you publish to Figshare:

- Your poster is uploaded as a public item with the `Poster` item type.
- Metadata is mapped to Figshare's fields, including authors, categories, and tags.
- A DOI is assigned automatically.

## :arrow_down: Downloading instead

If you prefer not to publish to a repository right away, you can download a poster package to your local machine. The package includes your poster file and the structured `poster.json` metadata file. You can use this package to deposit the poster yourself later or share it through other channels.

## :link: After publishing

Once your poster is published:

- The record appears in the Posters.science registry and becomes searchable.
- You receive a DOI that you can add to your CV, reference in papers, or include in grant reports.
- The poster's metadata is available in machine-readable format for indexing and discovery.
