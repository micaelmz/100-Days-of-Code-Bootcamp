import requests
from flask import Flask, render_template, url_for
from random import randint
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def home():
    num = randint(1, 10)
    current_year = datetime.now().year
    return render_template(
        'templates/index.html',
        num=num,
        year=current_year
    )


@app.route('/guess/<name>')
def guess(name):
    age_result = requests.get('https://api.agify.io', params={'name': name}).json()
    gender_result = requests.get('https://api.genderize.io', params={'name': name}).json()
    return render_template(
        'guess.html',
        name=name,
        gender=gender_result['gender'],
        age=age_result['age']
    )

@app.route('/blog')
def get_blog():
    endpoint = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(endpoint).json()
    return render_template('blog.html', posts=response)

if __name__ == '__main__':
    app.run(debug=True)
