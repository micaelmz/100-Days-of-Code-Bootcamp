from flask import Flask
from html_tags import bold, emphasis, underline

app = Flask(__name__)

@app.route('/')
@bold
@emphasis
@underline
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(debug=True)
