import os
import asyncio
import json
import queue

import aiohttp

from gpu_management.repository.gpu_management_repository import GPUManagementRepository
from template.include.socket_server.utility.color_print import ColorPrinter

class GPUManagementRepositoryImpl(GPUManagementRepository):
    async def check_gpu_server_available(self, userDefinedReceiverFastAPIChannel, api_url):
        
        # TODO temporary code. must fix for more stability 
        async with aiohttp.ClientSession() as session:
            async with session.post(
                url=f"http://{os.getenv('HOST')}:{os.getenv('FASTAPI_PORT')}/request-ai-command",
                json={
                    "command": 3737,
                    "data": [api_url]
                }
            ) as res:
                print(res.status)
                await asyncio.sleep(1)
                
                
        temporaryQueueList = []

        loop = asyncio.get_event_loop()
        try:
            while True:
                receivedResponseFromSocketClient = await loop.run_in_executor(
                    None, userDefinedReceiverFastAPIChannel.get, False
                )
                data = json.loads(receivedResponseFromSocketClient)

                if data.get("api_url") == api_url and "status" in data.keys():
                    status = data.get("status")
                    break

                temporaryQueueList.append(receivedResponseFromSocketClient)

        except queue.Empty:
            ColorPrinter.print_important_message("아직 데이터를 처리 중이거나 요청한 데이터가 없습니다")
            return "gpu status information doesn't exist."

        for item in temporaryQueueList:
            await loop.run_in_executor(None, userDefinedReceiverFastAPIChannel.put, item)

        return status
