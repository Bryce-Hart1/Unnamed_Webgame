


class user:
    def __init__(self, userName : str):
        self.name = userName
        self.color = "DEF"
        self.res_people = 0
        self.res_wood = 0
        self.res_metal = 0
        self.res_gold = 0
        self.res_oil = 0
        self.res_silcon = 0
        self.res_uranium = 0
        self.chunksOwned = [] # list of chunks
        self.baseOrigin
    def setOrigin(x : int, y : int):
        pass

    def gainedChunk():
        pass

    def lostChunk():
        pass
    
    def incrementResource(self, resource : str, amount : int):
        resource.lower()

        if resource == 'people' : 
            self.res_people += amount
            return
        elif resource == 'wood' : 
            self.res_wood += amount
        elif resource == 'metal':
            self.res_metal += amount
        elif resource == 'oil' : 
            self.res_oil += amount
        elif resource == 'gold' : 
            self.res_gold += amount
        elif resource == 'silcon' : 
            self.res_silcon += amount
        elif resource == 'uranium' :
            self.res_uranium += amount
        else: 
            print("incrementResource not found value: {}", resource)

            
