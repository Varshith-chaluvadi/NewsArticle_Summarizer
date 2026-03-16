from flask import Flask, render_template, request
from newspaper import Article
import requests

app = Flask(__name__)

API_URL = "https://api-inference.huggingface.co/models/sshleifer/distilbart-cnn-12-6"

headers = {
    "Authorization": "Bearer YOUR_HUGGINGFACE_API_KEY"
}

def summarize_text(text):
    payload = {"inputs": text[:1000]}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()[0]["summary_text"]


@app.route("/", methods=["GET", "POST"])
def home():
    summary = None
    error = None

    if request.method == "POST":
        article_url = request.form.get("article_url")

        try:
            article = Article(article_url)
            article.download()
            article.parse()

            text = article.text
            summary = summarize_text(text)

        except:
            error = "Could not summarize the article."

    return render_template("index.html", summary=summary, error=error)


if __name__ == "__main__":
    app.run()