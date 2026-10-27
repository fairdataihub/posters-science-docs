---
lang: en-US
title: Figshare Deposit Details (Draft)
description: Draft of the metadata Posters.science plans to send to Figshare and what Figshare can hold
head:
  - - meta
    - name: og:image
      content: https://kalai.fairdataihub.org/api/generate?title=Posters.science%20Documentation&description=Figshare%20Deposit%20Details&app=posters-science&org=fairdataihub
---

# Figshare Deposit Details (Draft)

::: warning Draft
Publishing to Figshare is not available yet. This page describes how it is planned to work, so details may change before it is released. To publish now, use [Zenodo](./zenodo-mapping).
:::

When Figshare publishing is available, the platform will create an item on your own Figshare account containing your poster file, a structured metadata file (`poster.json`), and a set of metadata fields. Figshare holds fewer kinds of metadata than Zenodo, so this page also lists what Figshare has no place for.

## How the upload will work

1. The platform creates a private item of type "Poster" on your Figshare account.
2. It reserves the DOI.
3. It uploads your poster file and `poster.json`.
4. It publishes the item.

If your Figshare account belongs to an institution with its own Figshare portal, the poster is published on that portal. It then uses your institution's DOI prefix, licenses and subject categories, and your institution may review it before it is public.

A new version of your poster is published as a new version of the same Figshare item. Figshare numbers the versions itself (1, 2, 3).

## Fields you provide

| Your metadata | What Figshare receives |
|---------------|------------------------|
| Title | Used as the item title |
| Authors | Given and family names and ORCID iDs |
| Keywords | Sent as Figshare keywords. Figshare needs at least one. |
| Description and submission abstract | Combined into the item description, with the abstract under its own heading |
| Conference name, location, and dates | Written as a first line of the description: "Presented at ..." |
| License | Matched to a license your Figshare account offers |
| Related identifiers | DOIs or links of related papers, datasets, or software, with their relationship type |
| Funding | Linked to a grant in Figshare's funding database when the award number matches exactly one grant, otherwise added as text ("Funder name, award number: award title") |

You will also need to pick at least one **category** (research field) from Figshare's list. Figshare requires it, and the research field Posters.science stores is too broad to choose one for you.

## Fields the platform will add

| Field | What the platform does |
|-------|------------------------|
| Item type | Set to "Poster" |
| DOI | Reserved from Figshare before publishing. The assigned DOI is stored in your poster record on Posters.science. |
| Link to Posters.science | A related link to the poster's page on Posters.science ("is described by") |
| Poster file | Your original PDF or image |
| Metadata file | A `poster.json` file following the [Poster JSON Schema](./schema), included alongside your poster file |

Figshare sets the publisher ("figshare", or your institution's name on a portal) and the publication date itself.

## What Figshare cannot hold

These fields have no place in Figshare's metadata. They are kept in the `poster.json` file deposited with your poster, which is why that file is always included.

| Field | What happens |
|-------|--------------|
| Affiliations | figshare.com has no affiliation field for authors. On an institutional portal, Figshare adds your institution. |
| Author type (person or organization) | Figshare treats every author as a person |
| Language | No language field |
| Presentation date and conference details | No conference fields; included in the description line instead |
| Funder identifiers (ROR) and award links | No field for them |
| Version label | Figshare numbers versions itself, so a version you type (e.g., "2.1") cannot be sent |
| Poster content sections, image captions, table captions | No equivalent fields |

## Licenses

figshare.com offers a short list of licenses: CC BY 4.0, CC0, MIT, GPL, GPL 2.0+, GPL 3.0+ and Apache 2.0. Institutional portals may offer more. How Posters.science will handle a poster under another license, such as CC BY-NC or CC BY-SA, has not been decided yet.

## Full field-by-field crosswalk

For the detailed technical mapping, including open questions, see the [draft Figshare crosswalk in the poster-json-schema repository](https://github.com/fairdataihub/poster-json-schema/blob/main/crosswalk/figshare.md).
