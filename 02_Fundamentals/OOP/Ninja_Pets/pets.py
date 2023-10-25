class Pet:
    def __init__(self,name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy



    def sleep(self,plus_energy):
        plus_energy = 25
        self.energy += plus_energy
        
        
    def eat(self,plus_energy, plus_health):
        plus_energy = 5
        plus_health = 10
        self.energy += plus_energy
        self.health += plus_health
        print("Meeeeeee wooof wooof")
        print(f'Energy is now: {self.energy}')
        print(f'Health is now: {self.health}')
        
    
    def play(self,plus_health):
        plus_health = 5
        self.health += plus_health
        print(f'30 minutes walk accomplished. Healt is now: {self.health}')
        
    
    def noise(self,sound):
        self.sound = sound
        print('Baobaaaaaooooo it is Shower Time!!!')
        print('TRAITOOOOOOOOOOOOOR, You said you loved meeeeeeeee')

class Competition(Pet):
    def __init__ (self,name,type,tricks,health,energy,speed, weight):
        super().__init__(name,type,tricks,health,energy)
        self.speed = speed
        self.weight = weight


baobao = Pet('Baobao', 'dog', 'sleep' , 200, 100)
turbo = Competition("Turbo", "competition_dog", "plays_dead" , 300,500,'40mh',33)
print(turbo.speed)