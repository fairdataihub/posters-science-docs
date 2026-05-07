---
lang: en-US
title: Ecosystem
description: Related projects and repositories in the Posters.science ecosystem
head:
  - - meta
    - name: og:image
      content: https://kalai.fairdataihub.org/api/generate?title=Posters.science%20Documentation&description=Ecosystem&app=posters-science&org=fairdataihub
---

# Ecosystem

Posters.science is built from several open source components. Each project has its own repository and can be used independently.

## Core platform

| Project | Description |
|---------|-------------|
| [posters-science](https://github.com/fairdataihub/posters-science) | The main web platform for sharing and discovering posters. Built with Nuxt 3, Vue 3, and TypeScript. |
| [poster-json-schema](https://github.com/fairdataihub/poster-json-schema) | The JSON schema for machine-actionable scientific posters. Based on DataCite 4.7 with poster-specific extensions. |
| [poster-json-examples](https://github.com/fairdataihub/poster-json-examples) | Manually annotated poster JSON files used for validation and testing. |

## Extraction and classification

| Project | Description |
|---------|-------------|
| [poster2json](https://github.com/fairdataihub/poster2json) | CLI and Python library for extracting structured metadata from poster PDFs and images using LLMs. |
| [posters-science-extraction-api](https://github.com/fairdataihub/posters-science-extraction-api) | The API service that powers metadata extraction on the platform. |
| [poster-sentry](https://github.com/fairdataihub/poster-sentry) | A multimodal classifier that distinguishes scientific posters from other document types. |
| [poster-sentry-training](https://github.com/fairdataihub/poster-sentry-training) | Training data and scripts for reproducing the PosterSentry classifier. |

## Research and documentation

| Project | Description |
|---------|-------------|
| [poster-sharing-reuse-paper-code](https://github.com/fairdataihub/poster-sharing-reuse-paper-code) | Code and analysis for the research paper on poster sharing and reuse. |
| [posters-science-survey](https://github.com/fairdataihub/posters-science-survey) | Survey instruments used to study poster sharing practices. |
| [posters-science-dev-docs](https://github.com/fairdataihub/posters-science-dev-docs) | Developer documentation for the platform's architecture, deployment, and monitoring. |
| [posters-science-docs](https://github.com/fairdataihub/posters-science-docs) | This documentation site. |

## Contributing

All projects welcome contributions. Each repository includes its own contributing guidelines. If you are not sure where to start, open an issue on the main [posters-science](https://github.com/fairdataihub/posters-science/issues) repository.
