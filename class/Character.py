class Character (object):
    def __init__(self, name, health, power, ability):
        self.name = name
        self.health = health
        self.power = power
        self.ability = ability
        
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
        
    def attack(self, other):
        other.health -= self.power
        
    def specialattack(self, other):
        other.health -= self.ability
    
    def defend (self, other):
        self.health -= other.power
    
    def __str__(self):
        return self.name
    