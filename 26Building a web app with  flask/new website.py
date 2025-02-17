from flask import Flask,render_template
import requests

app = Flask(__name__)

api_key = 'd14f4656cef943fb88821658badd6700'

url = f'https://newsapi.org/v2/everything?q=apple&from=2025-02-14&to=2025-02-14&sortBy=popularity&apiKey={api_key}'


@app.route('/')
def home():
    response = requests.get(url)
    data = response.json()
    articles = data['articles']
    return render_template('index.html',our_articles=articles)




if __name__ == '__main__':
    app.run(debug=True)
