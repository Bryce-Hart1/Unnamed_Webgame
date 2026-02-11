import random



class resource:
    def __init__(self, hasMetal : bool, hasWood : bool, hasGold : bool, hasOil : bool, hasSilcon : bool, hasUranium : bool):
        self.Iron = hasMetal
        self.Gold = hasGold
        self.Wood = hasWood
        self.Oil = hasOil
        self.Silcon = hasSilcon
        self.Uranium = hasUranium
    def displayResources(self): 
        print("Iron: {}, Gold: {}, Wood: {}, Oil: {}, Silcon: {}, Uranium", self.Iron,
               self.Gold, self.Gold, self.Wood, self.Oil, self.Silcon, self.Uranium)

    

class chunk:
    def __init__(self, size, ore, type):
        self.ore = ore
        self.size = size
        self.type = type

        
# returns a random precent. For example
# if you want a 50% chance of an event: precent = 50
def getRandomChance(precent):
    roll = random(1,100)
    return (roll < precent)


def pickResource(onWater):
    if(onWater):
        return resource(False, False, False, True, False, False) #temp for now, only returns oil
    if(getRandomChance(25)): #25 precent chance to do this
        return resource(False, True, False, False, False, False) #returns wood as the resource
    if(getRandomChance(25)): #25 percent oil well chance
        return resource(False, False, False, True, False, False)
    #otherwise pick from ores the ground ores and have a chance at generating
    uMine = getRandomChance(10) #10 precent chance to get uranium mine
    sMine = getRandomChance(15) #15 precent chance to get silcon
    mMine = True #always get metal
    gMine = getRandomChance(35)
    return resource(mMine, False, gMine, False, sMine, uMine)

    #currently not finished. We need a way to determine (randomly generated or not) what resources a spot should generate.
    #for example, if we have a water spot, we should not be able to place trees or ores for example, only oil, because this is the only one that makes
    #sense in this spot. Another example is if we have a tree farm, we should not be able to also have metals on this spot. This is still up for discussion,
    #but I dont think we should be able to have multiple mines on one chunk, my thinking its its one of the three (not multiple for a chunk) - Tree OR Oil OR
    # ores, and for water, it should be just oil, but maybe at a higher rate, but we can add that later




#returns a chunk object. For now we could have it hard set for some sort of pattern, but this should generate EVERYTHING relating to the chunk, including type,
# whats underneath, what the surface looks like, etc. I think we should build and flush out this function, but leave the more random generation parts out of it 
# for now. Right now it should just return a chunk object for the map
def generateChunk(remaining):
    

    ores = pickResource(False)
    returnChunk = chunk('r',ores, "Desert") #format

        
#fill a list (Like a vector) with all of the chunks for this map. So say our map is 8 x 8, we have 64 chunks to generate.) Then when we go to print on the
# frontend, we can just take the width sqrt(TOTAL_CHUNKS) and know what the map would be and how to format it. This is considering the map is square,
# which i think it should be. lmk if you have questions
def generateMap():
    myMap = []
    TOTAL_CHUNKS = 64
    for chunk in TOTAL_CHUNKS:
        myMap.append(generateChunk)
    return myMap