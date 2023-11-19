from books_app.config.mysqlconnection import connectToMySQL

from books_app import app

from books_app.models import author_model



class Book():
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.authors_fav_books =  []
        
        
        
        
        
        
        
    @classmethod
    def show_books(cls):
    
        query = """
            SELECT * FROM books
        """
        results = connectToMySQL('books_authors_db').query_db(query)
        all_books = []
        
        for row in results :
            new_class = cls(row)
            all_books.append(new_class)
            
        return all_books
    
    
    @classmethod
    def show_one_book(cls,data):
        query = """
            SELECT * FROM books
            LEFT JOIN favorites ON favorites.book_id = books.id
            LEFT JOIN authors ON favorites.author_id = authors.id
            WHERE book_id = %(id)s
        """
        results = connectToMySQL('books_authors_db').query_db(query,data)
        if results:
            author = cls(results[0])
            for row in results:
                
                author_data = {
                    "id" : row["authors.id"],
                    "name" : row["name"],
                    "created_at" : row["authors.created_at"],
                    "updated_at" : row["authors.updated_at"]
                }
                author.authors_fav_books.append( author_model.Author( author_data ) )
            return author
    
    @classmethod
    def create_book(cls,form):
        
        query = """
            INSERT INTO books (title , num_of_pages)
            VALUES 
            (%(title)s , %(num_of_pages)s)
        """
        
        return connectToMySQL('books_authors_db').query_db(query,form)
    
    @classmethod
    def connect_author_to_books(cls,data):
        query = """
            SELECT * FROM books
            LEFT JOIN favorites ON favorites.book_id = books.id
            LEFT JOIN authors ON favorites.author_id = authors.id
            WHERE books.id = %(id)s
        """
        
        results = connectToMySQL('books_authors_db').query_db(query,data)
        if results:
            book = cls(results[0])
            for row in results:
                
                author_data = {
                    "id" : row["authors.id"],
                    "name" : row["name"],
                    "created_at" : row["authors.created_at"],
                    "updated_at" : row["authors.updated_at"]
                }
                book.authors_fav_books.append( author_model.Author( author_data ) )
            return book