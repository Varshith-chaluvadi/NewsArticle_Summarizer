from transformers import pipeline
from newspaper import Article
from flask import Flask, request, jsonify
from flask_cors import CORS
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin

app = Flask(__name__)
CORS(app)

summarizer = pipeline(model="sshleifer/distilbart-cnn-12-6")

MAX_CHAR_LENGTH = 4000


def extract_text_from_url(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        article_text = article.text

        soup = None

        if not article_text.strip():
            response = requests.get(url, timeout=20)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            paragraphs = [p.get_text() for p in soup.find_all("p") if p.get_text().strip()]
            article_text = ' '.join(paragraphs)
        else:
            soup = BeautifulSoup(article.html, 'html.parser')

        image_urls = []
        if soup:
            for img in soup.find_all("img"):
                src = img.get("src")
                if src and not src.startswith("data:"):
                    src = urljoin(url, src)
                    image_urls.append(src)

        return article_text, image_urls
    except Exception as e:
        return "", []


@app.route("/", methods=["GET"])
def health():
    return jsonify({"status": "ok", "message": "News Article Summarizer API"})


@app.route("/summarize", methods=["POST"])
def summarize_article():
    data = request.get_json(silent=True)
    if not data or "url" not in data:
        return jsonify({"error": "Missing 'url' in request body."}), 400

    url = data["url"].strip()
    if not url:
        return jsonify({"error": "Empty URL provided."}), 400

    try:
        article_text, images = extract_text_from_url(url)
        if len(article_text.strip()) > 100:
            truncated_text = article_text[:MAX_CHAR_LENGTH]
            summary = summarizer(
                truncated_text,
                max_length=150,
                min_length=30,
                do_sample=False
            )
            return jsonify({
                "summary": summary[0]["summary_text"],
                "images": images
            })
        else:
            return jsonify({"error": "Article text is too short to summarize."}), 422
    except Exception as e:
        return jsonify({"error": f"Error processing URL: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860, debug=True)
