import createMap
import random

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