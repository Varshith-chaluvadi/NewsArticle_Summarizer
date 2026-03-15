from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    summary = None
    error = None
    images = []

    if request.method == "POST":
        article_url = request.form.get("article_url")

        if not article_url:
            error = "Please provide a valid URL."
        else:
            # temporary placeholder
            summary = "Summary will appear here after processing the article."

    return render_template(
        "index.html",
        summary=summary,
        error=error,
        images=images
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)