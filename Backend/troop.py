#we should maybe have a parent class with troop type, and then all classes underneath just inherit this class

class troop:
    def __init__(self, name : str):
        self.name = name #dont know exactly how I want to do attacks yet.
        self.damage = 0
        self.health = 0
