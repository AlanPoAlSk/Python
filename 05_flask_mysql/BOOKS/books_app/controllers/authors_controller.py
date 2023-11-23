from flask import render_template , redirect , request

from books_app import app


from books_app.models.author_model import Author
from books_app.models.book_model import Book

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/authors')
def all_authors():
    authors = Author.show_all()
    
    return render_template('authorsec.html', authors = authors)


@app.route('/author/create', methods = ['POST'])
def create_author():
    data = {
        'name': request.form['name']
    }
    author_id = Author.create_author(request.form)
    
    return redirect('/authors')

@app.route('/authors/<int:id>')
def author_book(id):
    data = {
        'id': id
    }
    author = Author.show_one(data)
    unf_books = Book.not_favorite_books(data)
    
    return render_template('author_favorite.html', author = author ,unf_books = unf_books )

@app.route('/book/join', methods = ['POST'])
def book_join():
    data = {
        'author_id':request.form['author_id'],
        'book_id':request.form['book_id']
    }
    Author.favorite_add(data)
    return redirect(f"/authors/{request.form['author_id']}")

