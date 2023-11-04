
from dojo_survey_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
        
        
    @classmethod
    def create_post(cls,form):
        
        query = """
            INSERT INTO dojos (name , location , language , comment)
            VALUES
            (%(name)s,%(location)s,%(language)s,%(comment)s)
        """
        
        return connectToMySQL('dojo_survey_schema').query_db(query,form)
    
    
    @classmethod
    def show(cls):
        
        query = 'SELECT * FROM dojos ORDER BY dojos.id DESC LIMIT 1;'
        
        results = connectToMySQL('dojo_survey_schema').query_db(query)
        return Dojo(results[0])
    
    
    @staticmethod
    def validate_post(post):
        is_valid = True 
        if len(post['name']) < 2:
            flash("<Your name must contain at least 2 characters.>")
            is_valid = False
        if (post['location']) == '':
            flash("<Please, select a Location>")
            is_valid = False
        if (post['language']) == '':
            flash("<Please, select a Language>")
            is_valid = False
        if len(post['comment']) < 2:
            flash("<Your comment must contain at least 2 characters>")
            is_valid = False
        return is_valid