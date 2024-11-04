from fastapi import APIRouter, Depends, status
from starlette.responses import JSONResponse

from llama_si_agent.controller.request_form.llama_si_agent_idle_request_form import LlamaSIAgentIdleRequestForm
from llama_si_agent.controller.request_form.llama_si_agent_file_list_request_form import LlamaSIAgentFileListRequestForm
from llama_si_agent.controller.request_form.llama_si_agent_current_phase_request_form import LlamaSIAgentCurrentPhaseRequestForm
from llama_si_agent.controller.request_form.llama_si_agent_backlog_request_form import LlamaSIAgentBacklogRequestForm
from llama_si_agent.controller.request_form.llama_si_agent_test_reports_request_form import LlamaSIAgentTestReportsRequestForm
from llama_si_agent.controller.request_form.llama_si_agent_code_review_request_form import LlamaSIAgentCodeReviewRequestForm
from llama_si_agent.controller.request_form.llama_si_agent_file_content_request_form import LlamaSIAgentFileContentRequestForm
from llama_si_agent.service.llama_si_agent_service_impl import LlamaSIAgentServiceImpl
from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl

llamaSIAgentRouter = APIRouter()

async def injectSIAgentService() -> LlamaSIAgentServiceImpl:
    return LlamaSIAgentServiceImpl(UserDefinedQueueRepositoryImpl.getInstance())

@llamaSIAgentRouter.post("/llama-check-si-agent-idle")
async def requestToCheckSIAgentIdle(siAgentIdleRequestForm: LlamaSIAgentIdleRequestForm,
                                    siAgentService: LlamaSIAgentServiceImpl =
                                    Depends(injectSIAgentService)):

    isIdle = await siAgentService.requestToCheckSIAgentIdle(
        siAgentIdleRequestForm.toSIAgentIdleRequest())

    return JSONResponse(content={"isIdle": isIdle}, status_code=status.HTTP_200_OK)


@llamaSIAgentRouter.post("/llama-check-current-phase")
async def request_to_get_current_phase(si_agent_current_phase_request_form: LlamaSIAgentCurrentPhaseRequestForm,
                                    siAgentService: LlamaSIAgentServiceImpl =
                                    Depends(injectSIAgentService)):

    current_phase = await siAgentService.request_to_get_current_phase(
        si_agent_current_phase_request_form.to_si_agent_current_phase_request())

    return JSONResponse(content={"phase": current_phase}, status_code=status.HTTP_200_OK)


@llamaSIAgentRouter.post("/llama-get-backlogs")
async def request_to_get_current_phase(si_agent_backlog_request_form: LlamaSIAgentBacklogRequestForm,
                                    siAgentService: LlamaSIAgentServiceImpl =
                                    Depends(injectSIAgentService)):

    backlog = await siAgentService.request_to_get_backlogs(
        si_agent_backlog_request_form.to_si_agent_current_phase_request())

    return JSONResponse(content={"backlog": backlog}, status_code=status.HTTP_200_OK)


@llamaSIAgentRouter.post("/llama-get-file-list")
async def request_to_get_file_list(siAgentFileListRequestForm: LlamaSIAgentFileListRequestForm,
                                    siAgentService: LlamaSIAgentServiceImpl =
                                    Depends(injectSIAgentService)):

    file_list = await siAgentService.request_to_get_file_list(
        siAgentFileListRequestForm.toSIAgentFileListRequest())

    return JSONResponse(content={"file_list": file_list}, status_code=status.HTTP_200_OK)


@llamaSIAgentRouter.post("/llama-get-file-content")
async def request_to_get_file_content(siAgentFileContentRequestForm: LlamaSIAgentFileContentRequestForm,
                                    siAgentService: LlamaSIAgentServiceImpl =
                                    Depends(injectSIAgentService)):

    file_content = await siAgentService.request_to_get_file_content(
        siAgentFileContentRequestForm.toSIAgentFileContentRequest())

    return JSONResponse(content={"file_content": file_content}, status_code=status.HTTP_200_OK)


@llamaSIAgentRouter.post("/llama-get-test-reports")
async def request_to_get_test_reports(si_agent_test_reports_request_form: LlamaSIAgentTestReportsRequestForm,
                                    siAgentService: LlamaSIAgentServiceImpl =
                                    Depends(injectSIAgentService)):

    test_reports = await siAgentService.request_to_get_test_reports(
        si_agent_test_reports_request_form.to_si_agent_test_reports_request())

    return JSONResponse(content={"test_reports": test_reports}, status_code=status.HTTP_200_OK)


@llamaSIAgentRouter.post("/llama-get-code-review")
async def request_to_get_code_reviews(si_agent_code_review_request_form: LlamaSIAgentCodeReviewRequestForm,
                                    siAgentService: LlamaSIAgentServiceImpl =
                                    Depends(injectSIAgentService)):

    code_review = await siAgentService.request_to_get_code_review(
        si_agent_code_review_request_form.to_si_agent_code_review_request())

    return JSONResponse(content={"code_review": code_review}, status_code=status.HTTP_200_OK)
