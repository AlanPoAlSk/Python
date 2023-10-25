import pets

class Ninja:
    def __init__ (self,first_name,last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
    
    def walk(self,energy):
        self.energy = energy
        pets.baobao.play('health')
        
    
    def feed(self, food):
        self.food = food
        print("Dinner Time!!! Who wants some chicken???")
        pets.baobao.eat('energy', 'health')
        
    
    def bath(self,water):
        self.water = water
        pets.baobao.noise('sound')
        print("Now I have to dry miself -.- , thank you. . .")



ninja1 = Ninja('Bob', 'bobbie', 'bones', 'chicken', 'Baobao')


ninja1.feed('chicken')
ninja1.walk('energy')
ninja1.bath('water')