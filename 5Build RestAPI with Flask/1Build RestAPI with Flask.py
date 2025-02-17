from flask import Flask
import json

app = Flask(__name__)


with open('books.json','r') as file:
    books = json.load(file)


@app.route('/books/<book_id>')
def get_book(book_id):
    book = books[book_id]
    if book:
        return book
    else:
        return {'Invalid data'}


@app.route('/')
def homepage():
    return 'HomePage'


app.run()