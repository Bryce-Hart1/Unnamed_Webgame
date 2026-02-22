from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import createMap as CM # When using something from create map us CM
import mapData as Mdata # same here
import user as userf
from enum import Enum
from pydantic import BaseModel

class gameStates(Enum):
    IN_LOBBY = 1
    IN_GAME = 2
    GAME_OVER = 3
    END_OF_GAME_RESULTS = 4
    END_INSTANCE = 5 #end game instance and take it out of the list

active_games = [] #store all games that are going on right now here


#returns the size of active games, and that will be the id for the current game
#this id will simply just be the spot in the vector that the id is at.
def setGameId():
    return len(active_games)




#Calling this creates a new game object.
def createNewGame():
    return game()


#takes this game out of scope by taking in the value in the list where it is stored
def endThisGame(thisGame : int):
    active_games.remove(thisGame)
    return


#defines a single game instance. can be multiple at one time.
#we need setters so game variables can be easily updated
class game:
    MAX_PLAYERS = 8 #if this is reached, no one else can join

    def __init__(self):
        self.id = setGameId()
        self.currentGameState = gameStates.IN_LOBBY
        self.currentGameCode = Mdata.createGameCode()
        self.users = [] #maybe when constructor is called we could already put the host in this? (right now i have implemented a workaround)
        self.map = CM.generateMap()


    def userJoined(self, person : userf.user):
        if(self.currentGameState != gameStates.IN_LOBBY):
            pass
            #tell the user that they cannot join, game is in progress
        if(len(self.users) == self.MAX_PLAYERS):
            pass
            #tell the user they cant join max player limit has been reached, or just black out join button, or both!
        #this should not have logic related to the individual, rather just the user as it relates to this game instance
        #for example, base origin, and checking what player number they are in this list
        return
        

    def userLeft(self, usersId : str):
        if self.users.index(usersId) == 0: #user is host, assign new host, and if no one is left to assign host to end this game
            if len(self.users) == 1:
                #end game 
                pass
            else:
                setattr(self.users, 'isTheHost', True)

        self.users.remove(usersId)
        return

    def thisGameHasStarted(self):
        self.currentGameState = gameStates.IN_GAME
        return
    

#if someone has a clever idea to make this the same as a user importing object, dont. I want more functionality for starting a game later
class NewGameRequest(BaseModel):
    host_name : str
    host_color : str
    host_top : str
    host_bottom : str
        

#================================Server stuff========================================
#server related functions go below here
app = FastAPI()


# Allow frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)





#user requested new game
@app.post("/startGame")
def pressedCreateNewGame(request : NewGameRequest):
    currentGame = createNewGame()
    host = userf.user(NewGameRequest.host_name, True, NewGameRequest.host_color, NewGameRequest.host_top, NewGameRequest.host_bottom)
    currentGame.userJoined(host) #add host as the first list of users


    return {}

    



@app.get("/")
def check_message():
    return {"message": "server running"}