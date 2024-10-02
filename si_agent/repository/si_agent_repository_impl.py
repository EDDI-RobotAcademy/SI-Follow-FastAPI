import asyncio
import json
import queue

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
