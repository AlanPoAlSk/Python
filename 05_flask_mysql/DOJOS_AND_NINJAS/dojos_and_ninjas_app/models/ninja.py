from dojos_and_ninjas_app.config.mysqlconnection import connectToMySQL
from dojos_and_ninjas_app.models.dojo import Dojo


class Ninja:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']
        
        
        
    @classmethod
    def get_all(cls):
        
        query = 'SELECT * FROM ninjas'
        
        results = connectToMySQL('dojo_and_ninjas_schema').query_db(query)
        
        all_ninjas = []
        
        for row in results :
            new_class = cls(row)
            all_ninjas.append(new_class)
            
        return all_ninjas
    
    
    @classmethod
    def get_one(cls,id):
        
        data = {'id': id}
        
        query = 'SELECT * FROM ninjas WHERE id = %(id)s'
        
        results = connectToMySQL('dojo_and_ninjas_schema').query_db(query,data)
        
        if results:
            new_ninja = cls(results[0])
            return new_ninja
        else :
            return False
        
    
    @classmethod
    def get_all_by_city(cls,dojo_id):
        
        data = {"dojo_id": dojo_id}
        
        query = """
            SELECT * FROM ninjas
            JOIN dojos ON dojos.id = ninjas.dojo_id
            WHERE ninjas.dojo_id = %(dojo_id)s
        """
        results = connectToMySQL('dojo_and_ninjas_schema').query_db(query,data)
        all_ninjas = []
        for ninja in results:
            new_ninja = cls(ninja)
            
            dojo_data = {
                **ninja,
                "id" : ninja["dojos.id"],
            }
            new_dojo = Dojo(dojo_data)
            new_ninja.ninja = new_dojo

            all_ninjas.append(new_ninja)

        return all_ninjas
        
    
    @classmethod
    def create_ninja(cls,form):
        
        query = """
            INSERT INTO ninjas (dojo_id, first_name, last_name , age)
            VALUES
            (%(dojo_id)s,%(first_name)s,%(last_name)s,%(age)s)
        """
        
        id_of_created_row = connectToMySQL('dojo_and_ninjas_schema').query_db(query,form)
        return id_of_created_row