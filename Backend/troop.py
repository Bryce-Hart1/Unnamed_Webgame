#we should maybe have a parent class with troop type, and then all classes underneath just inherit this class

class troop:
    def __init__(self, name : str):
        self.name = name #dont know exactly how I want to do attacks yet.
        self.damage = 0
        self.health = 0










class infantry(troop):
    def __init__(self, name : str):
        pass

class smallSky(troop):
    def __init__(self, name):
        pass

class bigSky(troop):
    pass


class smallWater(troop):
    pass 

class bigWater(troop):
    pass

class smallLand(troop):
    pass

class bigLand(troop):
    pass


#special troops 
class spyPlane:
    pass

class subMarine:
    pass