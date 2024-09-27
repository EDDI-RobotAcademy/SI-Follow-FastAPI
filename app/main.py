import os
import sys

import colorama
import uvicorn

from dotenv import load_dotenv

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template'))
from template.task_manager.manager import TaskManager

from template.deep_learning.controller.deep_learning_controller import deepLearningRouter

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template', 'include', 'socket_server'))
from template.include.socket_server.initializer.init_domain import DomainInitializer

DomainInitializer.initEachDomain()

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

app.include_router(deepLearningRouter)

if __name__ == "__main__":
    colorama.init(autoreset=True)

    TaskManager.createSocketServer()
    uvicorn.run(app, host=os.getenv('HOST'), port=int(os.getenv('FASTAPI_PORT')))
