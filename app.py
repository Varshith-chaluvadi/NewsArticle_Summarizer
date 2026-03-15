from flask import Flask, render_template, request
from newspaper import Article
from transformers import pipeline

app = Flask(__name__)

# Load summarization model once
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

@app.route("/", methods=["GET", "POST"])
def home():
    summary = None
    error = None
    images = []

    if request.method == "POST":
        article_url = request.form.get("article_url")

        try:
            article = Article(article_url)
            article.download()
            article.parse()

            text = article.text

            if len(text) < 200:
                error = "Article too short to summarize."
            else:
                result = summarizer(text[:1024], max_length=150, min_length=50, do_sample=False)
                summary = result[0]['summary_text']

                images = article.images

        except Exception as e:
            error = "Could not process the article."

    return render_template(
        "index.html",
        summary=summary,
        error=error,
        images=images
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)