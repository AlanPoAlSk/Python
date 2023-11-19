from books_app import app

from books_app.controllers import books_controller
from books_app.controllers import authors_controller

if __name__=="__main__":  
    app.run(debug=True)