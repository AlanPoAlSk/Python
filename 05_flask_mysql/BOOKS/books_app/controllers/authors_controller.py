from flask import render_template , redirect , request

from books_app import app


from books_app.models.author_model import Author
from books_app.models.book_model import Book



@app.route('/authors')
def all_authors():
    authors = Author.show_all()
    
    return render_template('authorsec.html', authors = authors)


@app.route('/authors/create', methods = ['POST'])
def create_author():
    Author.create_author(request.form)
    
    return redirect('/authors')

@app.route('/authors/<int:id>')
def author_book(id):
    data = {
        'id': id
    }
    author = Author.show_one(data)
    book = Book.connect_author_to_books(data)
    
    return render_template('author_favorite.html', author = author ,book = book )

