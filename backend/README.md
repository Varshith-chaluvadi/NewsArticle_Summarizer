---
title: News Article Summarizer
emoji: 📰
colorFrom: indigo
colorTo: purple
sdk: docker
app_port: 7860
pinned: false
---

# 📰 News Article Summarizer API

Flask API that summarizes news articles using DistilBART.

## Endpoint

**POST** `/summarize`

```json
{
  "url": "https://example.com/news/article"
}
```

**Response:**
```json
{
  "summary": "A concise summary of the article...",
  "images": ["https://example.com/image1.jpg"]
}
```
