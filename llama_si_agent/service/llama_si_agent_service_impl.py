from llama_si_agent.repository.llama_si_agent_repository_impl import LlamaSIAgentRepositoryImpl
from llama_si_agent.service.request.llama_si_agent_idle_request import LlamaSIAgentIdleRequest
from llama_si_agent.service.request.llama_si_agent_file_list_request import LlamaSIAgentFileListRequest
from llama_si_agent.service.request.llama_si_agent_file_content_request import LlamaSIAgentFileContentRequest
from llama_si_agent.service.request.llama_si_agent_current_phase_request import LlamaSIAgentCurrentPhaseRequest
from llama_si_agent.service.request.llama_si_agent_backlog_request import LlamaSIAgentBacklogRequest
from llama_si_agent.service.request.llama_si_agent_test_reports_request import LlamaSIAgentTestReportsRequest
from llama_si_agent.service.request.llama_si_agent_code_review_request import LlamaSIAgentCodeReviewRequest
from llama_si_agent.service.llama_si_agent_service import LlamaSIAgentService
from template.include.socket_server.utility.color_print import ColorPrinter
from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl


class LlamaSIAgentServiceImpl(LlamaSIAgentService):

    def __init__(self, userDefinedQueueRepository: UserDefinedQueueRepositoryImpl):
        self.__siAgentRepository = LlamaSIAgentRepositoryImpl()
        self.__userDefinedQueueRepository = userDefinedQueueRepository

    async def requestToCheckSIAgentIdle(self, siAgentIdleRequest: LlamaSIAgentIdleRequest):
        userDefinedReceiverFastAPIChannel = self.__userDefinedQueueRepository.getUserDefinedSocketReceiverFastAPIChannel()
        ColorPrinter.print_important_message("requestToCheckSIAgentIdle()")
        return await self.__siAgentRepository.checkSIAgentIdle(
            userDefinedReceiverFastAPIChannel,
            siAgentIdleRequest.toUserToken()
        )
        
    async def request_to_get_current_phase(self, si_agent_current_phase_request: LlamaSIAgentCurrentPhaseRequest):
        userDefinedReceiverFastAPIChannel = self.__userDefinedQueueRepository.getUserDefinedSocketReceiverFastAPIChannel()
        ColorPrinter.print_important_message("request_to_get_current_phase()")
        return await self.__siAgentRepository.get_current_phase(
            userDefinedReceiverFastAPIChannel,
            si_agent_current_phase_request.to_user_token(),
            si_agent_current_phase_request.to_project_name()
        )

    async def request_to_get_backlogs(self, si_agent_backlog_request: LlamaSIAgentBacklogRequest):
        userDefinedReceiverFastAPIChannel = self.__userDefinedQueueRepository.getUserDefinedSocketReceiverFastAPIChannel()
        ColorPrinter.print_important_message("request_to_get_backlogs()")
        return await self.__siAgentRepository.get_backlogs(
            userDefinedReceiverFastAPIChannel,
            si_agent_backlog_request.to_user_token(),
            si_agent_backlog_request.to_project_name()
        )
        
    async def request_to_get_file_list(self, si_agent_file_list_request: LlamaSIAgentFileListRequest):
        userDefinedReceiverFastAPIChannel = self.__userDefinedQueueRepository.getUserDefinedSocketReceiverFastAPIChannel()
        ColorPrinter.print_important_message("request_to_get_file_list()")
        return await self.__siAgentRepository.get_file_list(
            userDefinedReceiverFastAPIChannel,
            si_agent_file_list_request.to_user_token(),
            si_agent_file_list_request.to_project_name()
        )
        
    async def request_to_get_file_content(self, si_agent_file_content_request: LlamaSIAgentFileContentRequest):
        userDefinedReceiverFastAPIChannel = self.__userDefinedQueueRepository.getUserDefinedSocketReceiverFastAPIChannel()
        ColorPrinter.print_important_message("request_to_get_file_content()")
        return await self.__siAgentRepository.get_file_content(
            userDefinedReceiverFastAPIChannel,
            si_agent_file_content_request.to_user_token(),
            si_agent_file_content_request.to_project_name(),
            si_agent_file_content_request.to_file_name()
        )
        
    async def request_to_get_test_reports(self, si_agent_test_reports_request: LlamaSIAgentTestReportsRequest):
        userDefinedReceiverFastAPIChannel = self.__userDefinedQueueRepository.getUserDefinedSocketReceiverFastAPIChannel()
        ColorPrinter.print_important_message("request_to_get_test_reports()")
        return await self.__siAgentRepository.get_test_reports(
            userDefinedReceiverFastAPIChannel,
            si_agent_test_reports_request.to_user_token(),
            si_agent_test_reports_request.to_project_name()
        )
        
    async def request_to_get_code_review(self, si_agent_code_review_request: LlamaSIAgentCodeReviewRequest):
        userDefinedReceiverFastAPIChannel = self.__userDefinedQueueRepository.getUserDefinedSocketReceiverFastAPIChannel()
        ColorPrinter.print_important_message("request_to_get_code_review()")
        return await self.__siAgentRepository.get_code_reviews(
            userDefinedReceiverFastAPIChannel,
            si_agent_code_review_request.to_user_token(),
            si_agent_code_review_request.to_project_name()
        )
