---
lang: en-US
title: FAQ
description: Frequently asked questions about Posters.science
head:
  - - meta
    - name: og:image
      content: https://kalai.fairdataihub.org/api/generate?title=Posters.science%20Documentation&description=FAQ&app=posters-science&org=fairdataihub
---

# Frequently Asked Questions

## General

### What is Posters.science?

Posters.science is a free, open source platform for sharing and discovering scientific posters. It uses AI to extract metadata from poster files and helps you publish them to Zenodo with a DOI.

### Do I need an account to search for posters?

No. Searching, browsing, and viewing poster records is available to everyone without an account. You only need to create an account to share a poster.

### Is Posters.science free?

Yes. The platform is completely free for researchers. There are no paid tiers, paywalls, or premium features.

### Who builds and maintains this?

Posters.science is developed by the [FAIR Data Innovations Hub](https://fairdataihub.org) at the California Medical Innovations Institute. The project is open source under the MIT license.

## Sharing posters

### What file formats can I upload?

PDF, PNG, and JPEG. PDF is the recommended format because it generally produces the best metadata extraction results.

### How long does it take to share a poster?

Most posters can be shared in under five minutes. The AI extraction handles the metadata, and you review and publish.

### Can I edit the metadata after publishing?

You can update metadata on the poster record in Posters.science. For changes to the Zenodo record, you would need to edit the record directly on Zenodo.

### What license is applied to my poster?

The default is Creative Commons Attribution 4.0 (CC BY 4.0). You can change this during the metadata review step before publishing.

### Can I share a poster I did not author?

Only if you have the necessary rights and permissions from the authors. When you submit a poster, you affirm that you have the authority to share it.

### What if my poster is in a language other than English?

The platform supports posters in multiple languages. The extraction model reads the text as-is. You can specify the language during metadata review.

## Discovering posters

### Where do the posters in the registry come from?

Two sources: posters submitted directly through the platform, and posters automatically indexed from Zenodo and Figshare. See [Auto-Registration](./auto-registration) for details.

### Can I download search results?

Yes. You can export your current search results as a JSON file.

## Technical

### Is my poster content sent to a third-party AI service?

No. The extraction model runs on local GPU hardware maintained by the FAIR Data Innovations Hub. No poster content is sent to external AI providers.

### What is a DOI?

A Digital Object Identifier (DOI) is a unique, permanent link to a research output. When you publish a poster through Posters.science, it receives a DOI from Zenodo that you can use in citations, CVs, and grant reports.

### What is the poster JSON schema?

It is a structured format for describing scientific posters in machine-readable JSON. It is based on the DataCite Metadata Schema with poster-specific extensions for conference details, poster content, and research field. See [The Poster Schema](./schema) for details.

### Can I use the extraction tool independently?

Yes. The extraction tool, [poster2json](https://github.com/fairdataihub/poster2json), is available as an open source Python package that you can install and run on your own machine.
