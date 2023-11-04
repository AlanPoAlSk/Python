from dojos_and_ninjas_app.config.mysqlconnection import connectToMySQL


class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        
        query = 'SELECT * FROM dojos'
        
        results = connectToMySQL('dojo_and_ninjas_schema').query_db(query)
        
        all_dojos = []
        
        for row in results :
            new_class = cls(row)
            all_dojos.append(new_class)
            
        return all_dojos
    
    
    @classmethod
    def get_one(cls,id):
        
        data = {'id': id}
        
        query = 'SELECT * FROM dojos WHERE id = %(id)s'
        
        results = connectToMySQL('dojo_and_ninjas_schema').query_db(query,data)
        
        if results:
            new_dojo = cls(results[0])
            return new_dojo
        else :
            return False
    
    
    @classmethod
    def create_dojo(cls,form):
        
        query = """
            INSERT INTO dojos (name)
            VALUES
            (%(dojo_id)s,%(dojo_name)s)
        """
        
        id_of_created_row = connectToMySQL('dojo_and_ninjas_schema').query_db(query,form)
        return id_of_created_row
    
    
