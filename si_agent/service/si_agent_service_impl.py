from si_agent.repository.si_agent_repository_impl import SIAgentRepositoryImpl
from si_agent.service.si_agent_service import SIAgentService
from template.include.socket_server.utility.color_print import ColorPrinter
from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl


class SIAgentServiceImpl(SIAgentService):

    def __init__(self, userDefinedQueueRepository: UserDefinedQueueRepositoryImpl):
        self.__siAgentRepository = SIAgentRepositoryImpl()
        self.__userDefinedQueueRepository = userDefinedQueueRepository

    def requestToCheckSIAgentIdle(self, siAgentIdleRequest):
        userDefinedReceiverFastAPIChannel = self.__userDefinedQueueRepository.getUserDefinedSocketReceiverFastAPIChannel()
        ColorPrinter.print_important_message("requestToCheckSIAgentIdle()")
        return self.__siAgentRepository.checkSIAgentIdle(
            userDefinedReceiverFastAPIChannel,
            siAgentIdleRequest.toUserToken()
        )

