from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import createMap as CM # When using something from create map us CM
import mapData as Mdata # same here
import user as userf
from enum import Enum


class possibleGameStates(Enum):
    IN_LOBBY = 1
    IN_GAME = 2
    GAME_OVER = 3


def createGameCode():
    pass

def initalizeMap():
    pass


#defines a single game instance. can be multiple at one time.
#we need setters so game variables can be easily updated
class game:
    def __init__(self):
        self.currentGameState = possibleGameStates.IN_GAME
        self.currentGameCode = createGameCode()
        self.users = [] #maybe when constructor is called we could already put the host in this?

        pass

    def userJoined(self):
        pass

    def userLeft(self, usersId : str):
        pass

    def assignUserColor(self):
        pass
        





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