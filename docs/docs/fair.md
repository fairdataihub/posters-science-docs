---
lang: en-US
title: FAIR Principles for Posters
description: How Posters.science applies the FAIR principles to scientific posters
head:
  - - meta
    - name: og:image
      content: https://kalai.fairdataihub.org/api/generate?title=Posters.science%20Documentation&description=FAIR%20Principles%20for%20Posters&app=posters-science&org=fairdataihub
---

# :globe_with_meridians: FAIR Principles for Posters

The [FAIR principles](https://www.go-fair.org/fair-principles/) were introduced in 2016 to guide the management of digital research objects so they are optimally reusable. While the FAIR movement has focused primarily on data and more recently on software, the principles apply equally to scientific posters. Posters.science is built around making posters FAIR by default.

## :mag: Findable

A research object is findable when it has a persistent identifier, is described by rich metadata, and is indexed in a searchable resource.

Posters shared through Posters.science receive:

- A **DOI** assigned through Zenodo or Figshare, providing a globally unique, persistent identifier.
- **Structured metadata** following the [Poster JSON Schema](./schema), which includes the title, authors, affiliations, keywords, conference, funding, and more.
- **Indexing** in the Posters.science registry, which supports full-text search, filtered search, and AI-powered discovery.

## :unlock: Accessible

A research object is accessible when it can be retrieved using its identifier through a standard protocol, and when metadata remains available even if the object itself is no longer accessible.

Posters published through the platform are:

- Stored in open repositories (Zenodo, Figshare) that use standard HTTPS access.
- Available without authentication for open-access posters.
- Described by metadata that persists independently of the poster file itself.

## :handshake: Interoperable

A research object is interoperable when it uses shared vocabularies and standard formats that other systems can understand.

Poster metadata in Posters.science:

- Follows the **DataCite Metadata Schema** (v4.7), the same standard used across millions of DOI-registered research outputs.
- Uses **ORCID** identifiers for authors and **ROR** identifiers for institutions, both widely adopted in scholarly infrastructure.
- Is stored as **JSON**, a format that any programming language or analysis tool can read.
- Maps to repository-native formats (Zenodo, Figshare) without loss, so metadata transfers cleanly between systems.

## :recycle: Reusable

A research object is reusable when it has a clear license, detailed provenance, and meets community standards.

Posters shared through Posters.science:

- Include an explicit **license** (defaulting to CC BY 4.0).
- Carry **provenance metadata**: who created the poster, when it was presented, at which conference, and under what funding.
- Follow a **community-developed schema** designed in collaboration with DataCite and UC3, with public feedback and semantic versioning.
- Contain **machine-readable content** (extracted text, structured sections), making them usable for text mining, meta-analysis, and AI-based discovery.

## :seedling: Why this matters for posters

Most scientific posters today fail all four FAIR criteria. They are not assigned identifiers, not described by structured metadata, not stored in interoperable formats, and not shared with licenses. Posters.science is designed to change this by building FAIR compliance into the sharing process itself, rather than asking researchers to do it manually.
