from enum import Enum


#these states are only used when the player is in the game
class userStates(Enum):
    FLOATING = 0 #in lobby or in game over screen, etc. Any time they arent in game
    MAIN_SCREEN = 1
    UPGRADE_SCREEN = 2


class user:
    def __init__(self, userName : str, isHost : bool, color : str, top : str, bottom : str):
        self.name = userName
        self.isTheHost = isHost
        self.personal_color = color
        self.personal_top = top
        self.personal_bottom = bottom
        self.res_people = 0
        self.res_wood = 0
        self.res_metal = 0
        self.res_gold = 0
        self.res_oil = 0
        self.res_silcon = 0
        self.res_uranium = 0
        self.chunksOwned = [] # list of chunks
        self.baseOriginX = -1
        self.baseOriginY = -1
    

    #origin should always set before the game begins, same with color
    def setOrigin(self, x : int, y : int):
        self.baseOriginX = x
        self.baseOriginY = y
        return

    def setColor(self, colorToSet : str):
        self.color = colorToSet

    def gainedChunk():
        #if the player gets a new chunk. This cannot be stoleChunk, as this is from another player
        pass

        
    def stoleChunk():
        pass

    def lostChunk():
        pass
    
    def incrementResource(self, resource : str, amount : int):
        resource.lower()

        if resource == 'people' : 
            self.res_people += amount
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

            
def createNewUser(isFirstPlayer : bool):
    #prompt the frontend to pull up a user creation page. We can talk about what the implementation might be.
    #this implementation should let them set a color (For now allow duplicate colors) and a name
    return user("Bryce", isFirstPlayer, "GREEN")
