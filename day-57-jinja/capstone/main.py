from flask import Flask, render_template, url_for
import requests

app = Flask(__name__)
ENDPOINT = 'https://api.npoint.io/c790b4d5cab58020d391'
result = requests.get(ENDPOINT).json()


@app.route('/')
def home():
    return render_template("index.html", contents=result)


@app.route('/<page>/')
def get_pages(page):
    page_content = result[int(page) - 1]
    return render_template("post.html", content=page_content)

if __name__ == "__main__":
    app.run(debug=True)
