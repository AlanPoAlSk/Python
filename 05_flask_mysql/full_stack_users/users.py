

from mysqlconnection import connectToMySQL



class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
        
        
        
    @classmethod
    def get_all(cls):
        
        query = 'SELECT * FROM user'
        
        results = connectToMySQL('user_schema').query_db(query)
        
        all_users = []
        
        for row in results :
            new_class = cls(row)
            all_users.append(new_class)
            
        return all_users
    
    @classmethod
    def get_one(cls,id):
        
        data = {'id': id}
        
        query = 'SELECT * FROM user WHERE id = %(id)s'
        
        results = connectToMySQL('user_schema').query_db(query,data)
        
        if results:
            new_user = cls(results[0])
            return new_user
        else :
            return False
        
        
    
    @classmethod
    def create(cls, data):
        
        query = """
            INSERT INTO user
            (first_name, last_name, email)
            VALUES (%(first_name)s,%(last_name)s,%(email)s);
        """
        
        id_of_created_row = connectToMySQL('user_schema').query_db(query,data)
        return id_of_created_row
    
    @classmethod
    def show(cls,data):
    
        query = """
            SELECT * FROM user;
        """
        results = connectToMySQL('user_schema').query_db(query,data)
        return results
    
    @classmethod
    def edit(cls,form):
        query = """
            UPDATE  user
            SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s
            WHERE id = %(id)s;
        """
        results = connectToMySQL('user_schema').query_db(query,form)
        return results
    
    
    @classmethod
    def delete(cls,id):
        query = """
            DELETE FROM user
            WHERE id =%(id)s;
        """
        data = {"id": id}
        return connectToMySQL('user_schema').query_db(query, data)