---
lang: en-US
title: Reviewing Metadata
description: How to review and edit extracted poster metadata
head:
  - - meta
    - name: og:image
      content: https://kalai.fairdataihub.org/api/generate?title=Posters.science%20Documentation&description=Reviewing%20Metadata&app=posters-science&org=fairdataihub
---

# Reviewing Metadata

After your poster is uploaded and processed, Posters.science presents the extracted metadata for your review. This step ensures that the information describing your poster is accurate before it gets published.

::: info
The metadata review page is only accessible after uploading a poster while signed in. See [Uploading Your Poster](./upload) for the first step.
:::

![Metadata Review Page](/metadata-page.png)

## How to review metadata

The metadata editor is organized into three sections. The first section is expanded by default. The other two are collapsed to keep the page manageable, but they contain fields that may have been auto-filled during extraction. We recommend expanding all sections to review the full set of metadata before continuing.

### Required fields (expanded by default)

These fields are always visible:

- **Title**: The poster title.
- **Description**: A summary or abstract of the poster. If your poster includes an abstract section, the platform extracts it automatically.
- **Authors**: Names, given/family name, name type (personal or organizational), affiliations, and ORCID iDs for each author. The platform looks up author identifiers in the [ORCID registry](https://orcid.org) and institutional identifiers in the [ROR registry](https://ror.org) to help fill these in.
- **Keywords**: Subject terms extracted from the poster.
- **Conference**: The name, location, dates, and acronym of the conference where the poster was presented.

### Optional fields (collapsed by default)

Click to expand this section. It contains fields that may already be filled in:

- **Language**: Auto-detected from the poster text. Verify that the detected language is correct.
- **Domain / Field of Study**: Auto-classified based on poster content.
- **Related identifiers**: DOIs and URLs found in the poster text and PDF link annotations, with their relationship type and resource type. Review these to confirm they are relevant references.
- **Funding**: Grants and funding sources mentioned on the poster. The platform cross-references these against funder databases.

### Poster content (collapsed by default)

Click to expand this section. It contains the full text extracted from your poster:

- **Sections**: The poster text broken into titled sections (e.g., Introduction, Methods, Results). Review to confirm the section boundaries and text are correct.
- **Image captions**: Captions for figures found on the poster.
- **Table captions**: Captions for tables found on the poster.

::: warning
Fields in collapsed sections may contain auto-filled values from the extraction pipeline (such as language, domain, and related identifiers). These values will be included in your poster record even if you do not expand the section to review them. We recommend checking all sections before proceeding.
:::

### License

The license is selected during the publishing step, not in the metadata editor. It defaults to Creative Commons Attribution 4.0 (CC BY 4.0).

## Editing fields

Click on any field to edit it. You can:

- Correct misspellings or formatting issues from the extraction.
- Add authors or affiliations that the AI missed.
- Fill in conference details if they were not printed on the poster.
- Remove related identifiers that are not relevant.
- Fix incorrectly detected language or domain.

When you are finished, click `Save Changes` to store your edits. You can then continue to the publishing step or come back later.

::: warning
If you close the browser without clicking `Save Changes`, your edits will be lost.
:::
