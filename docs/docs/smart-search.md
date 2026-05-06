---
lang: en-US
title: Smart Search
description: AI-powered natural language search for scientific posters
head:
  - - meta
    - name: og:image
      content: https://kalai.fairdataihub.org/api/generate?title=Posters.science%20Documentation&description=Smart%20Search&app=posters-science&org=fairdataihub
---

# :bulb: Smart Search

Smart Search lets you ask questions about the poster registry in plain language. Instead of picking keywords and filters, you describe what you are looking for and the platform finds relevant posters and summarizes what it finds.

<!-- ![Smart Search](/smart-search.png) -->

## :hammer_and_wrench: How to use Smart Search

1. Go to the [Discover](https://posters.science/discover) page and toggle to **Smart Search**.
2. Type a question or description of what you are looking for.
3. The platform returns a summary response along with links to the most relevant posters.

## :speech_balloon: Example queries

Smart Search understands questions like:

- "What research on Alzheimer's disease was presented at ARVO 2025?"
- "Show me posters about CRISPR gene editing from Stanford."
- "Are there any posters on machine learning for drug discovery funded by the NIH?"
- "What are the latest findings on cardiac tissue engineering?"

You can ask about specific topics, authors, institutions, conferences, funding sources, or combinations of these.

## :gear: How it works

Smart Search uses a retrieval-augmented generation (RAG) pipeline:

1. **Your query is analyzed** to identify key concepts, entities, and intent.
2. **Relevant posters are retrieved** using vector similarity search across the registry. Each poster's metadata is stored as a numerical embedding that captures its meaning.
3. **A response is generated** by a language model that reads the retrieved poster content and produces a summary with references to specific posters.

The system expands medical and scientific terminology automatically. If you search for "heart attack," it also considers posters about "myocardial infarction" and related terms.

::: info
Smart Search works best for exploratory questions where you want to understand what exists in the registry. For targeted lookups where you already know the author or conference, the [standard search](./search) with filters is faster.
:::

## :dart: Accuracy

Smart Search aims for precision in the posters it recommends. Each referenced poster in the response links directly to its record, so you can always verify the source. The generated summary is based only on poster content in the registry; it does not fabricate or speculate beyond what the posters contain.
