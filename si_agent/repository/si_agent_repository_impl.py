import os
import asyncio
import json
import queue

import aiohttp

from si_agent.repository.si_agent_repository import SIAgentRepository
from template.include.socket_server.utility.color_print import ColorPrinter

class SIAgentRepositoryImpl(SIAgentRepository):
    async def checkSIAgentIdle(self, userDefinedReceiverFastAPIChannel, userToken):
        temporaryQueueList = []
        userTokenFound = False

        # TODO: 좀 더 스마트한 테스트 방식이 필요함
        # userDefinedReceiverFastAPIChannel.put(json.dumps({"userToken": "token1"}))
        # userDefinedReceiverFastAPIChannel.put(json.dumps({"userToken": "token2"}))
        # userDefinedReceiverFastAPIChannel.put(json.dumps({"userToken": "test"}))

        loop = asyncio.get_event_loop()

        try:
            while True:
                receivedResponseFromSocketClient = await loop.run_in_executor(
                    None, userDefinedReceiverFastAPIChannel.get, False
                )
                data = json.loads(receivedResponseFromSocketClient)

                if data.get("userToken") == userToken:
                    userTokenFound = True
                    break

                temporaryQueueList.append(receivedResponseFromSocketClient)

        except queue.Empty:
            ColorPrinter.print_important_message("아직 데이터를 처리 중이거나 요청한 데이터가 없습니다")
            return userTokenFound

        for item in temporaryQueueList:
            await loop.run_in_executor(None, userDefinedReceiverFastAPIChannel.put, item)

        return userTokenFound

    async def get_current_phase(self, userDefinedReceiverFastAPIChannel, user_token, project_name):
        
        # TODO temporary code. must fix for more stability 
        async with aiohttp.ClientSession() as session:
            async with session.post(
                url=f"http://{os.getenv('HOST')}:{os.getenv('FASTAPI_PORT')}/request-ai-command",
                json={
                    "command": 77,
                    "data": [user_token, project_name]
                }
            ) as res:
                await asyncio.sleep(1)
        ColorPrinter.print_important_message("hihihihihihihi")
        temporaryQueueList = []

        loop = asyncio.get_event_loop()

        try:
            while True:
                receivedResponseFromSocketClient = await loop.run_in_executor(
                    None, userDefinedReceiverFastAPIChannel.get, False
                )
                ColorPrinter.print_important_message("upupupupupupupup")
                data = json.loads(receivedResponseFromSocketClient)
                
                ColorPrinter.print_important_message(f"outside: {data}")
                if data.get("user_token") == user_token and data.get("project_name") == project_name and "phase" in data:
                    ColorPrinter.print_important_message("inside")
                    current_phase = data["phase"]
                    ColorPrinter.print_important_message(f"phase: {current_phase}")
                    break

                temporaryQueueList.append(receivedResponseFromSocketClient)

        except queue.Empty:
            ColorPrinter.print_important_message("아직 데이터를 처리 중이거나 요청한 데이터가 없습니다")
            return ["phase information doesn't exist."]

        for item in temporaryQueueList:
            await loop.run_in_executor(None, userDefinedReceiverFastAPIChannel.put, item)

        return current_phase
    
    async def get_backlogs(self, userDefinedReceiverFastAPIChannel, user_token, project_name):
        
        # TODO temporary code. must fix for more stability 
        async with aiohttp.ClientSession() as session:
            async with session.post(
                url=f"http://{os.getenv('HOST')}:{os.getenv('FASTAPI_PORT')}/request-ai-command",
                json={
                    "command": 7733,
                    "data": [user_token, project_name]
                }
            ) as res:
                await asyncio.sleep(1)
                
                
        temporaryQueueList = []

        loop = asyncio.get_event_loop()

        try:
            while True:
                receivedResponseFromSocketClient = await loop.run_in_executor(
                    None, userDefinedReceiverFastAPIChannel.get, False
                )
                data = json.loads(receivedResponseFromSocketClient)

                if data.get("user_token") == user_token and data.get("project_name") == project_name and "backlog" in data:
                    backlog = data["backlog"]
                    break

                temporaryQueueList.append(receivedResponseFromSocketClient)

        except queue.Empty:
            ColorPrinter.print_important_message("아직 데이터를 처리 중이거나 요청한 데이터가 없습니다")
            return ["backlog information doesn't exist."]

        for item in temporaryQueueList:
            await loop.run_in_executor(None, userDefinedReceiverFastAPIChannel.put, item)

        return backlog
    
    async def get_file_list(self, userDefinedReceiverFastAPIChannel, user_token, project_name):
        
        # TODO temporary code. must fix for more stability 
        async with aiohttp.ClientSession() as session:
            async with session.post(
                url=f"http://{os.getenv('HOST')}:{os.getenv('FASTAPI_PORT')}/request-ai-command",
                json={
                    "command": 7373,
                    "data": [user_token, project_name]
                }
            ) as res:
                await asyncio.sleep(1)
                
                
        temporaryQueueList = []

        loop = asyncio.get_event_loop()

        try:
            while True:
                receivedResponseFromSocketClient = await loop.run_in_executor(
                    None, userDefinedReceiverFastAPIChannel.get, False
                )
                data = json.loads(receivedResponseFromSocketClient)

                if data.get("user_token") == user_token and "file_list" in data and data.get("project_name") == project_name:
                    file_list = data["file_list"]
                    break

                temporaryQueueList.append(receivedResponseFromSocketClient)

        except queue.Empty:
            ColorPrinter.print_important_message("아직 데이터를 처리 중이거나 요청한 데이터가 없습니다")
            return ["file list information doesn't exist."]

        for item in temporaryQueueList:
            await loop.run_in_executor(None, userDefinedReceiverFastAPIChannel.put, item)

        return file_list
    
    async def get_file_content(self, userDefinedReceiverFastAPIChannel, user_token, project_name, file_name):
        # TODO temporary code. must fix for more stability 
        async with aiohttp.ClientSession() as session:
            async with session.post(
                url=f"http://{os.getenv('HOST')}:{os.getenv('FASTAPI_PORT')}/request-ai-command",
                json={
                    "command": 7773,
                    "data": [user_token, project_name, file_name]
                }
            ) as res:
                await asyncio.sleep(2)
                
        temporaryQueueList = []

        loop = asyncio.get_event_loop()

        try:
            while True:
                receivedResponseFromSocketClient = await loop.run_in_executor(
                    None, userDefinedReceiverFastAPIChannel.get, False
                )
                data = json.loads(receivedResponseFromSocketClient)

                if data.get("user_token") == user_token and "file_content" in data and data.get("project_name") == project_name and data.get("file_name") == file_name:
                    file_content = data["file_content"]
                    break

                temporaryQueueList.append(receivedResponseFromSocketClient)

        except queue.Empty:
            ColorPrinter.print_important_message("아직 데이터를 처리 중이거나 요청한 데이터가 없습니다")
            return ["file content doesn't exist."]

        for item in temporaryQueueList:
            await loop.run_in_executor(None, userDefinedReceiverFastAPIChannel.put, item)

        return file_content
    
    async def get_test_reports(self, userDefinedReceiverFastAPIChannel, user_token, project_name):
        
        # TODO temporary code. must fix for more stability 
        async with aiohttp.ClientSession() as session:
            async with session.post(
                url=f"http://{os.getenv('HOST')}:{os.getenv('FASTAPI_PORT')}/request-ai-command",
                json={
                    "command": 3733,
                    "data": [user_token, project_name]
                }
            ) as res:
                await asyncio.sleep(1)
                
                
        temporaryQueueList = []

        loop = asyncio.get_event_loop()

        try:
            while True:
                receivedResponseFromSocketClient = await loop.run_in_executor(
                    None, userDefinedReceiverFastAPIChannel.get, False
                )
                data = json.loads(receivedResponseFromSocketClient)

                if data.get("user_token") == user_token and "test_reports" in data and data.get("project_name") == project_name:
                    test_reports = data["test_reports"]
                    break

                temporaryQueueList.append(receivedResponseFromSocketClient)

        except queue.Empty:
            ColorPrinter.print_important_message("아직 데이터를 처리 중이거나 요청한 데이터가 없습니다")
            return ["test reports information doesn't exist."]

        for item in temporaryQueueList:
            await loop.run_in_executor(None, userDefinedReceiverFastAPIChannel.put, item)

        return test_reports
    
    async def get_code_reviews(self, userDefinedReceiverFastAPIChannel, user_token, project_name):
        
        # TODO temporary code. must fix for more stability 
        async with aiohttp.ClientSession() as session:
            async with session.post(
                url=f"http://{os.getenv('HOST')}:{os.getenv('FASTAPI_PORT')}/request-ai-command",
                json={
                    "command": 7377,
                    "data": [user_token, project_name]
                }
            ) as res:
                await asyncio.sleep(1)
                
                
        temporaryQueueList = []

        loop = asyncio.get_event_loop()

        try:
            while True:
                receivedResponseFromSocketClient = await loop.run_in_executor(
                    None, userDefinedReceiverFastAPIChannel.get, False
                )
                data = json.loads(receivedResponseFromSocketClient)

                if data.get("user_token") == user_token and "code_review" in data and data.get("project_name") == project_name:
                    code_review = data["code_review"]
                    break

                temporaryQueueList.append(receivedResponseFromSocketClient)

        except queue.Empty:
            ColorPrinter.print_important_message("아직 데이터를 처리 중이거나 요청한 데이터가 없습니다")
            return ["code review information doesn't exist."]

        for item in temporaryQueueList:
            await loop.run_in_executor(None, userDefinedReceiverFastAPIChannel.put, item)

        return code_review