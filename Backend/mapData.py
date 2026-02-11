import createMap

def printMap(map):
    for item in map:
        print(item + ", ")

def main():
    myMapTest = createMap.generateMap()
    for chunk in myMapTest:
        print(createMap.chunk.displayResources() + "\n")