from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "News Article Summarizer is running!"

if __name__ == "__main__":
    app.run()