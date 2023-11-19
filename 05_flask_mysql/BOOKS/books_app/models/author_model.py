from books_app.config.mysqlconnection import connectToMySQL

from books_app.models import book_model





class Author():
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.fav_books = []
        
        
    @classmethod
    def show_all(cls):
    
        query = """
            SELECT * FROM authors
        """
        results = connectToMySQL('books_authors_db').query_db(query)
        all_authors = []
        
        for row in results :
            new_class = cls(row)
            all_authors.append(new_class)
            
        return all_authors
    
    @classmethod
    def show_one(cls,data):
        query = """
            SELECT * FROM authors
            LEFT JOIN favorites ON favorites.author_id = authors.id
            LEFT JOIN books ON favorites.book_id = books.id
            WHERE authors.id = %(id)s
        """
        results = connectToMySQL('books_authors_db').query_db(query,data)
        if results:
            author = cls(results[0])
            for row in results:
                
                book_data = {
                    "id" : row["books.id"],
                    "title" : row["title"],
                    "num_of_pages" : row["num_of_pages"],
                    "created_at" : row["books.created_at"],
                    "updated_at" : row["books.updated_at"]
                }
                author.fav_books.append( book_model.Book( book_data ) )
            return author
    
    
    @classmethod
    def create_author(cls,form):
        
        query = """
            INSERT INTO authors (name)
            VALUES 
            (%(name)s)
        """
        
        return connectToMySQL('books_authors_db').query_db(query,form)
    
    
    
    @classmethod
    def connect_books_to_authors(cls,data):
        query = """
            SELECT * FROM authors
            LEFT JOIN favorites ON favorites.author_id = authors.id
            LEFT JOIN books ON favorites.book_id = books.id
            WHERE author_id = %(id)s
        """
        
        results = connectToMySQL('books_authors_db').query_db(query,data)
        if results:
            author = cls(results[0])
            for row in results:
                
                book_data = {
                    "id" : row["books.id"],
                    "title": row["title"],
                    "num_of_pages" : row["num_of_pages"],
                    "created_at" : row["books.created_at"],
                    "updated_at" : row["books.updated_at"]
                }
                author.fav_books.append( book_model.Book( book_data ) )
            return author