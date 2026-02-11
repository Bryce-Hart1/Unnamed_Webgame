from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import createMap as CM # When using something from create map us CM
import mapData as Mdata # same here
import user





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