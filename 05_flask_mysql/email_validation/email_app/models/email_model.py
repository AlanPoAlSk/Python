from email_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:
    def __init__(self,data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
        
        
        
    @classmethod
    def create(cls,form):
        
        query =  """
            INSERT INTO emails (email)
            VALUES 
            (%(email)s)
        """
            
        return connectToMySQL('email_schema').query_db(query,form)
    
    
    @classmethod
    def show(cls):
        
        query = """
            SELECT * FROM emails
        """
        
        results = connectToMySQL('email_schema').query_db(query)
        
        all_email = []
        
        for row in results :
            new_class = cls(row)
            all_email.append(new_class)
            
        return all_email
    
    @classmethod
    def delete(cls,id): 
        
        data = {"id": id}
        
        query = """
            DELETE FROM emails
            WHERE id =%(id)s;
        """
        connectToMySQL('email_schema').query_db(query, data)
        
        
    @staticmethod
    def validate(form):
        
        
        query = 'SELECT * FROM emails WHERE email = %(email)s'
        results= connectToMySQL('email_schema').query_db(query,form)
        
        if not EMAIL_REGEX.match(form['email']):
            flash(' ------------> Invalid Email <------------ -------> Please Insert a Valid Email')
            return False
        else :
            if len(results) == 1:
                flash(' Email already in the system!')
                return False
            else :
                flash('Congratulations! Your email was successfully added to our system!')
        return True