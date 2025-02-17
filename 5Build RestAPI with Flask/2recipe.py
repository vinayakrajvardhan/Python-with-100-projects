from flask import Flask
import json


app = Flask(__name__)

with open('books.json','r') as file:
    recipes = json.load(file)


@app.route('/')
def recipes_books():
    return recipes



app.run()

