import random



#gives a cord (inside the chunk), along with a string saying what has been drawn
class drawn: 
    def __init__(self, x : int, y : int, object : str):
        self.X = x
        self.Y = y
        self.object = object


class Resource:
    def __init__(self, hasMetal : bool, hasWood : bool, hasGold : bool, hasOil : bool, hasSilcon : bool, hasUranium : bool):
        self.Iron = hasMetal
        self.Gold = hasGold
        self.Wood = hasWood
        self.Oil = hasOil
        self.Silcon = hasSilcon
        self.Uranium = hasUranium
    def displayResources(self): 
        print(self.Iron, self.Gold, self.Gold, self.Wood, self.Oil, self.Silcon, self.Uranium)

    

class chunk:
    def __init__(self, size : int, resource : Resource, biome : str):
        self.resources = resource
        self.size = size
        self.biome = biome
        self.drawn_positions = []
    

    def chunkAsStr(self):
        return (f"{self.biome} {self.resources.displayResources()}")
        

    #both draw and erase updates ONE TILE in a chunk
    def Draw(self, x : int, y : int, picture : str):
        self.drawnAt.append((drawn(x,y,picture)))
        return
    
    def Erase(self, x : int, y : int):
        #we need a way (eventually because the implementation is tricky) to fill squares with thier original state.
        #my current thnking (so we dont have to have a lookup) is that we have predefined textures for spots. Lets say that there is a 
        # building destroyed at 4,4. Well, we could have a new texture to replace that one. we can either restore it (to say, grass) or 
        #something else, like rubble. 
        pass #pass basically is used for unfilled functions

        
# returns a random precent. For example
# if you want a 50% chance of an event: precent = 50
def getRandomChance(percent):
    roll = random.randint(1,100)
    return (roll <= percent)


def pickResource(onWater):
    if(onWater):
        return Resource(False, False, False, True, False, False) #temp for now, only returns oil
    if(getRandomChance(25)): #25 precent chance to do this
        return Resource(False, True, False, False, False, False) #returns wood as the resource
    if(getRandomChance(25)): #25 percent oil well chance
        return Resource(False, False, False, True, False, False)
    #otherwise pick from ores the ground ores and have a chance at generating
    uMine = getRandomChance(10) #10 precent chance to get uranium mine
    sMine = getRandomChance(15) #15 precent chance to get silcon
    mMine = True #always get metal
    gMine = getRandomChance(35)
    return Resource(mMine, False, gMine, False, sMine, uMine)

    #currently not finished. We need a way to determine (randomly generated or not) what resources a spot should generate.
    #for example, if we have a water spot, we should not be able to place trees or ores for example, only oil, because this is the only one that makes
    #sense in this spot. Another example is if we have a tree farm, we should not be able to also have metals on this spot. This is still up for discussion,
    #but I dont think we should be able to have multiple mines on one chunk, my thinking its its one of the three (not multiple for a chunk) - Tree OR Oil OR
    # ores, and for water, it should be just oil, but maybe at a higher rate, but we can add that later




#returns a chunk object. For now we could have it hard set for some sort of pattern, but this should generate EVERYTHING relating to the chunk, including type,
# whats underneath, what the surface looks like, etc. I think we should build and flush out this function, but leave the more random generation parts out of it 
# for now. Right now it should just return a chunk object for the map
def generateChunk(remaining):
    SET_CHUNK_SIZE = 64
    biomes = ("desert", "grassland") #list of biomes to pick from
    resourcesForChunk
    #first pick biome
    if getRandomChance(50): #50% chance to be land
        resourcesForChunk = pickResource(False)
        returnChunk = chunk(SET_CHUNK_SIZE,resourcesForChunk, "Desert") #format
    else:
        resourcesForChunk = pickResource(True)
        returnChunk = chunk(64)



    return returnChunk

        
#fill a list (Like a vector) with all of the chunks for this map. So say our map is 8 x 8, we have 64 chunks to generate.) Then when we go to print on the
# frontend, we can just take the width sqrt(TOTAL_CHUNKS) and know what the map would be and how to format it. This is considering the map is square,
# which i think it should be. lmk if you have questions
def generateMap():
    myMap = []
    TOTAL_CHUNKS = 64
    for chunk in range(TOTAL_CHUNKS):
        myMap.append(generateChunk(42))
    return myMap