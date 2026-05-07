---
lang: en-US
title: Uploading Your Poster
description: How to upload a poster to Posters.science
head:
  - - meta
    - name: og:image
      content: https://kalai.fairdataihub.org/api/generate?title=Posters.science%20Documentation&description=Uploading%20Your%20Poster&app=posters-science&org=fairdataihub
---

# Uploading Your Poster

The first step in sharing your poster is uploading the file. Posters.science accepts PDFs and images (PNG, JPEG) and handles the rest from there.

## How to upload

1. Sign in to [posters.science](https://posters.science) with your account.
2. Click `Share a Poster` in the navigation bar.
3. Drag and drop your poster file into the upload area, or click to open the file picker.
4. Wait for the upload and processing to complete. This typically takes 10 to 30 seconds depending on file size.

![Share a Poster Page](/share-page.png)

## Supported file formats

Posters.science currently accepts the following formats:

- **PDF** (recommended)
- **PNG**
- **JPEG**

::: tip
PDF is the most common format and generally produces the best extraction results. If you have your poster in multiple formats, PDF is the recommended choice.
:::

## What happens during upload?

When you upload a file, the platform runs two processes:

1. **Text extraction**: For PDFs, the platform uses specialized tools to pull raw text from the document. For images, optical character recognition (OCR) reads the visible text.

2. **AI metadata extraction**: The extracted text is passed to a language model that identifies structured fields like the title, author names, affiliations, conference details, and funding sources.

Once both steps finish, you are taken to the metadata review page where you can check and edit the results.

::: info
Your original file is preserved exactly as uploaded. The extraction process reads from the file but does not modify it.
:::
