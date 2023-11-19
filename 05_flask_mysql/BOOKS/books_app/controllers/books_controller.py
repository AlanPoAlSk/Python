from flask import render_template , redirect , request

from books_app import app


from books_app.models.book_model import Book
from books_app.models.author_model import Author





@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/books')
def all_books():
    books = Book.show_books()
    
    return render_template('booksec.html', books = books)

@app.route('/books/create', methods = ['POST'])
def create_book():
    Book.create_book(request.form)
    
    return redirect('/books')

@app.route('/books/<int:id>')
def book_autjor(id):
    data = {
        'id': id
    }
    author = Author.connect_books_to_authors(data)
    book = Book.show_one_book(data)
    
    return render_template('book_favorite.html', author = author , book = book)
