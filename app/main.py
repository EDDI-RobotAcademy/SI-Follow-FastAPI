import os

import colorama
import uvicorn

from dotenv import load_dotenv

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

load_dotenv()

origins = os.getenv("ALLOWED_ORIGINS", "").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    colorama.init(autoreset=True)

    uvicorn.run(app, host=os.getenv('HOST'), port=int(os.getenv('FASTAPI_PORT')))
