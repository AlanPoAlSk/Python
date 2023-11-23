from flask import render_template , redirect , request

from books_app import app


from books_app.models.book_model import Book
from books_app.models.author_model import Author




@app.route('/books')
def all_books():
    books = Book.show_books()
    
    return render_template('booksec.html', books = books)

@app.route('/books/create', methods = ['POST'])
def create_book():
    Book.create_book(request.form)
    data = {
        'title': request.form['title'],
        'num_of_pages' : request.form['num_of_pages']
    }
    book_id = Book.create_book(data)
    
    return redirect('/books')

@app.route('/books/<int:id>')
def book_author(id):
    data = {
        'id': id
    }
    unf_authors = Author.not_favorite(data)
    book = Book.show_one_book(data)
    
    return render_template('book_favorite.html', unf_authors = unf_authors , book = book)

@app.route('/author/join', methods= ['POST'])
def join_author():
    data = {
        'author_id': request.form['author_id'],
        'book_id': request.form['book_id']
    }
    Author.favorite_add(data)
    return redirect(f"/books/{request.form['book_id']}")