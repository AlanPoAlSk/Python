class User :
    def __init__ (self,first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_point = 0
        
    
    def display_info(self , info):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_point)
        
        
    def enroll(self):
        if self.gold_card_point == False:
            self.is_rewards_member= True
            self.gold_card_point = 200
            
        
    
    def spend_points(self, amount):
        self.gold_card_point = self.gold_card_point - amount
        return self.gold_card_point
    
    
alan = User ('Alan','Skrzecz','alan@alan.com', 32)
bob = User ('Bob','Robb', 'bob@robb.com', 23)
jack = User ('Jack', "Daniels", 'jack@daniels.com' , 40)

alan.display_info('info')
bob.display_info('info')
jack.display_info('info')

alan.enroll()
bob.enroll()
jack.enroll()

bob.spend_points(50)
jack.spend_points(80)

alan.display_info('info')
bob.display_info('info')
jack.display_info('info')

alan.enroll()
alan.display_info('info')