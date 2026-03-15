from flask import Flask, render_template, request
from summarizer import summarize_article   # your summarizer function

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    summary = ""
    if request.method == "POST":
        url = request.form["url"]
        summary = summarize_article(url)
    return render_template("index.html", summary=summary)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)