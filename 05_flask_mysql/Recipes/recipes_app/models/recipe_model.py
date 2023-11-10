from recipes_app.config.mysqlconnection import connectToMySQL
from flask import flash
from recipes_app import app
from recipes_app.models import user_model

class Recipe:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.date = data['date']
        self.under_30_minutes = data['under_30_minutes']
        self.instructions = data['instructions']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        
        
        
    @classmethod
    def create(cls,form):
        
        
        query = """
            INSERT INTO recipes (name, description,date, under_30_minutes, instructions ,user_id)
            VALUES (%(name)s,%(description)s,%(date)s,%(under_30_minutes)s,%(instructions)s ,%(user_id)s);
        """
        
        return connectToMySQL('recipes_db').query_db(query,form)
    
    
    @classmethod
    def get_one(cls,data):
        
        
        
        query = """
            SELECT * FROM recipes JOIN users ON recipes.user_id = users.id
            WHERE recipes.id = %(id)s;
        """

        results = connectToMySQL('recipes_db').query_db(query,data)
        if results:
            row = results[0]
            this_recipe= cls(row)
            user_data = {
                **row,
                'id' :row['users.id'],
                    'created_at' : row['users.created_at'],
                    'updated_at' : row['users.updated_at']
            }
            this_user = user_model.User(user_data)
            this_recipe.post = this_user
            return this_recipe
        return False
        
    @classmethod
    def show_all(cls):
        
        query = """
            SELECT * FROM recipes 
            JOIN users ON  recipes.user_id = users.id; 
        """
        results = connectToMySQL('recipes_db').query_db(query)
        all_recipes = []
        
        if results:
            for row in results :
                this_recipe = cls(row)
                user_data = {
                    **row,
                    'id' :row['users.id'],
                    'created_at' : row['users.created_at'],
                    'updated_at' : row['users.updated_at']
                }
                
                this_user = user_model.User(user_data)
                this_recipe.post = this_user
                all_recipes.append(this_recipe)
        return all_recipes
    
    @staticmethod
    def is_valid(data):
        valid = True
        if len(data['name']) < 1:
            flash('name is required', 'name_err')
            valid = False
        if len(data['description']) < 1:
            flash('description is required', 'desc_err')
            valid = False
        if len(data['date']) < 1:
            flash('date is required', 'date_err')
            valid = False
        if 'under_30_minutes' not in data:
            flash('under 30 minutes is required', 'und_err')
            valid = False
        if len(data['instructions']) <1 :
            flash('instructions are required', 'inst_err')
            valid = False
        return valid    
            
    @classmethod
    def delete(cls,data):
        
        query = """
            DELETE FROM recipes
            WHERE id = %(id)s
        """
        return connectToMySQL('recipes_db').query_db(query,data)
    
    
    @classmethod
    def save(cls,data):
        
        
        query = """
            UPDATE recipes 
            SET 
            name = %(name)s,
            description = %(description)s,
            date = %(date)s,
            under_30_minutes = %(under_30_minutes)s,
            instructions = %(instructions)s
            WHERE recipes.id = %(id)s;
        """
        
        return connectToMySQL('recipes_db').query_db(query,data)
