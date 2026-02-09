import random



class ore:
    def __init__(self, hasIron, hasGold):
        self.Iron = hasIron
        self.Gold = hasGold

class chunk:
    def __init__(self, size, ore, type):
        self.ore = ore
        self.size = size
        self.type = type

        
#returns a random precent 
def getRandomPrecent():
    return random(0, 10)


def pickOres(onWater):
    return ore(True, True)


def generateChunk(remaining):
    #chunkOption = {'s', 'm', 'l', 'c', 'w'}
    #chances = random(1,5)
    #if chances > 2:

    ores = pickOres(False)
    returnChunk = chunk('r',ores, "Desert") #format

        
        

#generate chunk order and value (s,m,l,c,w)
# s - small island
# m - med island
# l - large
# c - connected piece
# w - water
def generateMap():
    myMap = []
    for i in range(25):
        myMap.append(generateChunk)
    return myMap


#generate chunk (25x)




