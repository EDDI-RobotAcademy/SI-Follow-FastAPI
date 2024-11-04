from si_agent.repository.si_agent_repository_impl import SIAgentRepositoryImpl
from si_agent.service.request.si_agent_idle_request import SIAgentIdleRequest
from si_agent.service.request.si_agent_file_list_request import SIAgentFileListRequest
from si_agent.service.request.si_agent_file_content_request import SIAgentFileContentRequest
from si_agent.service.request.si_agent_current_phase_request import SIAgentCurrentPhaseRequest
from si_agent.service.request.si_agent_backlog_request import SIAgentBacklogRequest
from si_agent.service.request.si_agent_test_reports_request import SIAgentTestReportsRequest
from si_agent.service.request.si_agent_code_review_request import SIAgentCodeReviewRequest
from si_agent.service.si_agent_service import SIAgentService
from template.include.socket_server.utility.color_print import ColorPrinter
from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl
from si_agent.api.django_http_client import DjangoHTTPClient
import asyncio

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
        
    async def request_to_get_current_phase(self, si_agent_current_phase_request: SIAgentCurrentPhaseRequest):
        userDefinedReceiverFastAPIChannel = self.__userDefinedQueueRepository.getUserDefinedSocketReceiverFastAPIChannel()
        ColorPrinter.print_important_message("request_to_get_current_phase()")
        return await self.__siAgentRepository.get_current_phase(
            userDefinedReceiverFastAPIChannel,
            si_agent_current_phase_request.to_user_token(),
            si_agent_current_phase_request.to_project_name()
        )

    async def request_to_get_backlogs(self, si_agent_backlog_request: SIAgentBacklogRequest):
        userDefinedReceiverFastAPIChannel = self.__userDefinedQueueRepository.getUserDefinedSocketReceiverFastAPIChannel()
        ColorPrinter.print_important_message("request_to_get_backlogs()")
        backlog = await self.__siAgentRepository.get_backlogs(
            userDefinedReceiverFastAPIChannel,
            si_agent_backlog_request.to_user_token(),
            si_agent_backlog_request.to_project_name()
        )

        # Django로 데이터 전송
        asyncio.create_task(DjangoHTTPClient.post("/ai_result/backlogs", {
            "user_token": si_agent_backlog_request.to_user_token(),
            "project_name": si_agent_backlog_request.to_project_name(),
            "backlog": backlog
        }))
        return backlog

    async def request_to_get_file_list(self, si_agent_file_list_request: SIAgentFileListRequest):
        userDefinedReceiverFastAPIChannel = self.__userDefinedQueueRepository.getUserDefinedSocketReceiverFastAPIChannel()
        ColorPrinter.print_important_message("request_to_get_file_list()")
        file_list = await self.__siAgentRepository.get_file_list(
            userDefinedReceiverFastAPIChannel,
            si_agent_file_list_request.to_user_token(),
            si_agent_file_list_request.to_project_name()
        )

        # Django로 데이터 전송
        asyncio.create_task(DjangoHTTPClient.post("/ai_result/file-list", {
            "user_token": si_agent_file_list_request.to_user_token(),
            "project_name": si_agent_file_list_request.to_project_name(),
            "file_list": file_list
        }))
        return file_list

    async def request_to_get_file_content(self, si_agent_file_content_request: SIAgentFileContentRequest):
        userDefinedReceiverFastAPIChannel = self.__userDefinedQueueRepository.getUserDefinedSocketReceiverFastAPIChannel()
        ColorPrinter.print_important_message("request_to_get_file_content()")
        file_content = await self.__siAgentRepository.get_file_content(
            userDefinedReceiverFastAPIChannel,
            si_agent_file_content_request.to_user_token(),
            si_agent_file_content_request.to_project_name(),
            si_agent_file_content_request.to_file_name()
        )

        # Django로 데이터 전송
        asyncio.create_task(DjangoHTTPClient.post("/ai_result/file-content", {
            "user_token": si_agent_file_content_request.to_user_token(),
            "project_name": si_agent_file_content_request.to_project_name(),
            "file_name": si_agent_file_content_request.to_file_name(),
            "file_content": file_content
        }))
        return file_content

    async def request_to_get_test_reports(self, si_agent_test_reports_request: SIAgentTestReportsRequest):
        userDefinedReceiverFastAPIChannel = self.__userDefinedQueueRepository.getUserDefinedSocketReceiverFastAPIChannel()
        ColorPrinter.print_important_message("request_to_get_test_reports()")
        test_reports = await self.__siAgentRepository.get_test_reports(
            userDefinedReceiverFastAPIChannel,
            si_agent_test_reports_request.to_user_token(),
            si_agent_test_reports_request.to_project_name()
        )

        # Django로 데이터 전송
        asyncio.create_task(DjangoHTTPClient.post("/ai_result/test-reports", {
            "user_token": si_agent_test_reports_request.to_user_token(),
            "project_name": si_agent_test_reports_request.to_project_name(),
            "test_reports": test_reports
        }))
        return test_reports

    async def request_to_get_code_review(self, si_agent_code_review_request: SIAgentCodeReviewRequest):
        userDefinedReceiverFastAPIChannel = self.__userDefinedQueueRepository.getUserDefinedSocketReceiverFastAPIChannel()
        ColorPrinter.print_important_message("request_to_get_code_review()")
        code_review = await self.__siAgentRepository.get_code_reviews(
            userDefinedReceiverFastAPIChannel,
            si_agent_code_review_request.to_user_token(),
            si_agent_code_review_request.to_project_name()
        )

        # Django로 데이터 전송
        asyncio.create_task(DjangoHTTPClient.post("/ai_result/code-review", {
            "user_token": si_agent_code_review_request.to_user_token(),
            "project_name": si_agent_code_review_request.to_project_name(),
            "code_review": code_review
        }))
        return code_review
