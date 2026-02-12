from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import createMap as CM # When using something from create map us CM
import mapData as Mdata # same here
import user as userf
from enum import Enum

class gameStates(Enum):
    IN_LOBBY = 1
    IN_GAME = 2
    GAME_OVER = 3
    END_OF_GAME_RESULTS = 4
    END_INSTANCE = 5

active_games = [] #store all games that are going on right now here


#returns the size of active games, and that will be the id for the current game
def setGameId():
    return len(active_games)


def createNewGame():
    return game()


#takes this game out of scope by taking in the value in the list where it is stored
def endThisGame(thisGame : int):
    active_games.remove(thisGame)
    return


#defines a single game instance. can be multiple at one time.
#we need setters so game variables can be easily updated
class game:
    def __init__(self):
        MAX_PLAYERS = 8 #if this is reached, no one else can join
        self.id = setGameId()
        self.currentGameState = gameStates.IN_LOBBY
        self.currentGameCode = Mdata.createGameCode()
        self.users = [] #maybe when constructor is called we could already put the host in this? (right now i have implemented a workaround)
        self.map = CM.generateMap()


    def userJoined(self):
        #this should not have logic related to the individual, rather just the user as it relates to this game instance
        #for example, base origin, and checking what player number they are in this list
        pass
        

    def userLeft(self, usersId : str):
        self.users.remove(usersId)
        




#user requested new game
def pressedStartNewGame():
    currentGame = createNewGame()
    currentGame.userJoined(userf.createNewUser())


#server related functions go below here
application = FastAPI()


# Allow frontend connection
application.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




@application.get("/")
def read_root():
    return {"message": "server running"}