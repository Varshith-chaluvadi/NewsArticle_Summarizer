# 📰 News Article Summarizer

A Flask-based web application that uses NLP to automatically summarize news articles from any URL. Paste a link, get an instant summary with article images.

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Flask](https://img.shields.io/badge/Flask-3.0-green)
![HuggingFace](https://img.shields.io/badge/HuggingFace-Transformers-yellow)

## 🚀 Features

- Extracts full text from any news article URL
- Generates concise summaries using **DistilBART** NLP model
- Displays article images alongside the summary
- Modern, responsive dark-theme UI
- Handles common scraping and parsing errors gracefully

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.10 | Runtime |
| Flask | Web framework |
| HuggingFace Transformers | Summarization (`distilbart-cnn-12-6`) |
| Newspaper3k | Article extraction |
| BeautifulSoup4 | HTML parsing |
| Gunicorn | Production WSGI server |

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/tharun-7733/News-Article-Summarizer.git
cd News-Article-Summarizer

# Create a virtual environment & activate it
python -m venv venv
source venv/bin/activate    # Mac/Linux
# venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
```

## ▶️ Usage

```bash
# Run the Flask app locally
python news.py
```

Open your browser at **https://news-article-summarizer-gd37.onrender.com** and paste any news article URL to get an instant summary.

## 🌐 Deployment (Render)

1. Push this repo to GitHub
2. Go to [render.com](https://render.com) → **New Web Service**
3. Connect your GitHub repo
4. Settings:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn news:app`
   - **Python Version:** `3.10.14` (set via `runtime.txt`)
5. Click **Deploy**

> **Note:** The model (~1.2 GB) may require a paid tier for sufficient memory.

## 📌 Example

**Input:** Paste any news article URL (e.g., from BBC, CNN, Times of India)

**Output:** A concise paragraph summarizing the key points, along with article images.
