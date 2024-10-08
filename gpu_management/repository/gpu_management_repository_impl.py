import asyncio
import json
import queue

from gpu_management.repository.gpu_management_repository import GPUManagementRepository
from template.include.socket_server.utility.color_print import ColorPrinter

class GPUManagementRepositoryImpl(GPUManagementRepository):
    async def check_gpu_server_available(self, userDefinedReceiverFastAPIChannel, api_url):
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
