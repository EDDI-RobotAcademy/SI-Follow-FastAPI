import os
import sys

import colorama
import uvicorn

from dotenv import load_dotenv

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from multiple_user_test_point.controller.multiple_user_test_point_controller import multipleUserTestPointRouter
from si_agent.controller.si_agent_controller import siAgentRouter
from user_defined_initializer.init import UserDefinedInitializer

from first_user_defined_function_domain.controller.fudf_controller import firstUserDefinedFunctionDomainRouter
from print_hello.controller.print_hello_controller import printHelloRouter
from gpu_management.controller.gpu_management_controller import gpu_management_router

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template'))
from template.task_manager.manager import TaskManager
from template.system_initializer.init import SystemInitializer

from template.deep_learning.controller.deep_learning_controller import deepLearningRouter
from template.dice.controller.dice_controller import diceResultRouter

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template', 'include', 'socket_server'))
from template.include.socket_server.initializer.init_domain import DomainInitializer

DomainInitializer.initEachDomain()
SystemInitializer.initSystemDomain()
UserDefinedInitializer.initUserDefinedDomain()

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
app.include_router(diceResultRouter)

app.include_router(printHelloRouter)
app.include_router(firstUserDefinedFunctionDomainRouter)

app.include_router(multipleUserTestPointRouter)

app.include_router(siAgentRouter)

app.include_router(gpu_management_router)

if __name__ == "__main__":
    colorama.init(autoreset=True)

    TaskManager.createSocketServer()
    uvicorn.run(app, host=os.getenv('HOST'), port=int(os.getenv('FASTAPI_PORT')))
