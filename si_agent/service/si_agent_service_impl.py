from si_agent.repository.si_agent_repository_impl import SIAgentRepositoryImpl
from si_agent.service.request.si_agent_idle_request import SIAgentIdleRequest
from si_agent.service.si_agent_service import SIAgentService
from template.include.socket_server.utility.color_print import ColorPrinter
from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl


class SIAgentServiceImpl(SIAgentService):

    def __init__(self, userDefinedQueueRepository: UserDefinedQueueRepositoryImpl):
        self.__siAgentRepository = SIAgentRepositoryImpl()
        self.__userDefinedQueueRepository = userDefinedQueueRepository

    async def requestToCheckSIAgentIdle(self, siAgentIdleRequest: SIAgentIdleRequest):
        userDefinedReceiverFastAPIChannel = self.__userDefinedQueueRepository.getUserDefinedSocketReceiverFastAPIChannel()
        ColorPrinter.print_important_message("requestToCheckSIAgentIdle()")
        return await self.__siAgentRepository.checkSIAgentIdle(
            userDefinedReceiverFastAPIChannel,
            siAgentIdleRequest.toUserToken()
        )
        
    async def request_to_get_current_phase(self, siAgentIdleRequest: SIAgentIdleRequest):
        userDefinedReceiverFastAPIChannel = self.__userDefinedQueueRepository.getUserDefinedSocketReceiverFastAPIChannel()
        ColorPrinter.print_important_message("request_to_get_current_phase()")
        return await self.__siAgentRepository.get_current_phase(
            userDefinedReceiverFastAPIChannel,
            siAgentIdleRequest.toUserToken()
        )

    async def request_to_get_backlogs(self, siAgentIdleRequest: SIAgentIdleRequest):
        userDefinedReceiverFastAPIChannel = self.__userDefinedQueueRepository.getUserDefinedSocketReceiverFastAPIChannel()
        ColorPrinter.print_important_message("request_to_get_backlogs()")
        return await self.__siAgentRepository.get_backlogs(
            userDefinedReceiverFastAPIChannel,
            siAgentIdleRequest.toUserToken()
        )