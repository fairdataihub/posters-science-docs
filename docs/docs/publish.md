---
lang: en-US
title: Publishing to a Repository
description: How to publish your poster to Zenodo
head:
  - - meta
    - name: og:image
      content: https://kalai.fairdataihub.org/api/generate?title=Posters.science%20Documentation&description=Publishing%20to%20a%20Repository&app=posters-science&org=fairdataihub
---

# Publishing to a Repository

The final step in sharing your poster is publishing it. Posters.science connects to [Zenodo](https://zenodo.org), a trusted open repository operated by CERN, so your poster gets a permanent home and a citable DOI.

## How to publish

1. After reviewing your metadata, click `Save Changes and Continue`.
2. Review the summary of what will be deposited.
3. Click `Publish`.

The platform creates a record on Zenodo that includes:

- Your original poster file (PDF or image).
- A structured metadata file (`poster.json`) following the [Poster JSON Schema](./schema).
- All metadata fields mapped to Zenodo's deposit format.

::: info
Publishing is a one-way action. Once the record is created on Zenodo, it receives a DOI and becomes publicly accessible. You can update metadata after publication, but the DOI is permanent. Zenodo allows you to [delete a record within 30 days](https://help.zenodo.org/docs/deposit/manage-records/#delete), but the DOI itself is never reusable.
:::

## Zenodo

When you publish to Zenodo through Posters.science:

- Your poster is deposited in the [Posters.science community on Zenodo](https://zenodo.org/communities/posters-science).
- The metadata is mapped to Zenodo's deposit format, including authors, affiliations, conference details, and funding.
- A DOI is assigned automatically.

## Downloading instead

If you prefer not to publish to a repository right away, you can download a poster package to your local machine. The package includes your poster file and the structured `poster.json` metadata file. You can use this package to deposit the poster yourself later or share it through other channels.

::: warning
When you download without publishing, the `poster.json` file will be incomplete according to the schema because no publisher has been assigned. Fields like DOI and repository identifiers will be missing until the poster is deposited in a repository.
:::

::: warning
Once published through Posters.science, the record cannot be removed by the user. If you need a record taken down, contact the team at [info@fairdataihub.org](mailto:info@fairdataihub.org).
:::

## After publishing

Once your poster is published:

- The record appears in the Posters.science registry and becomes searchable.
- You receive a DOI that you can add to your CV, reference in papers, or include in grant reports.
- The poster's metadata is available in machine-readable format for indexing and discovery.
