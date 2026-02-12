import createMap
import random

#this file should actually contain all the data pretaining to the map. Sprites, levels, everything.


def getMapObject(obj : str, ID : int):
    pass #this is up in the air, but i was thinking this stores levels of different objects. then, when we need
    #to print or send this object it has a name.



def printMap(map):
    for item in map:
        print(item + ", ")

#make a random game code that is five digits. Thinking of a weird edge case where 2 lobbies get the same code, even though
#its a one in 26^5 chance
def createGameCode():
    returnStr = ""
    for i in range(5):
        returnStr += chr(random(65,90))
    return returnStr

def initalizeMap():
    pass



def main():
    myMapTest = createMap.generateMap()
    for chunk in myMapTest:
        print(createMap.chunk.displayResources() + "\n")