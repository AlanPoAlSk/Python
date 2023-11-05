from email_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Email:
    def __init__(self,data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
        
        
        
    @classmethod
    def create(cls,form):
        
        query :  """
            INSERT INTO emails (email)
            VALUES 
            (%(email)s)
        """
            
        return connectToMySQL('email_schema').query_db(query,form)
    
    
    @classmethod
    def show(cls):
        
        query : """
            SELECT * FROM emails
        """