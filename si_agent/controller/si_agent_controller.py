from fastapi import APIRouter, Depends, status
from starlette.responses import JSONResponse

from si_agent.controller.request_form.si_agent_idle_request_form import SIAgentIdleRequestForm
from si_agent.controller.request_form.si_agent_file_list_request_form import SIAgentFileListRequestForm
from si_agent.controller.request_form.si_agent_current_phase_request_form import SIAgentCurrentPhaseRequestForm
from si_agent.controller.request_form.si_agent_backlog_request_form import SIAgentBacklogRequestForm
from si_agent.controller.request_form.si_agent_test_reports_request_form import SIAgentTestReportsRequestForm
from si_agent.service.si_agent_service_impl import SIAgentServiceImpl
from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl

siAgentRouter = APIRouter()

async def injectSIAgentService() -> SIAgentServiceImpl:
    return SIAgentServiceImpl(UserDefinedQueueRepositoryImpl.getInstance())

@siAgentRouter.post("/check-si-agent-idle")
async def requestToCheckSIAgentIdle(siAgentIdleRequestForm: SIAgentIdleRequestForm,
                                    siAgentService: SIAgentServiceImpl =
                                    Depends(injectSIAgentService)):

    isIdle = await siAgentService.requestToCheckSIAgentIdle(
        siAgentIdleRequestForm.toSIAgentIdleRequest())

    return JSONResponse(content={"isIdle": isIdle}, status_code=status.HTTP_200_OK)


@siAgentRouter.post("/check-current-phase")
async def request_to_get_current_phase(si_agent_current_phase_request_form: SIAgentCurrentPhaseRequestForm,
                                    siAgentService: SIAgentServiceImpl =
                                    Depends(injectSIAgentService)):

    current_phase = await siAgentService.request_to_get_current_phase(
        si_agent_current_phase_request_form.to_si_agent_current_phase_request())

    return JSONResponse(content={"phase": current_phase}, status_code=status.HTTP_200_OK)


@siAgentRouter.post("/get-backlogs")
async def request_to_get_current_phase(si_agent_backlog_request_form: SIAgentBacklogRequestForm,
                                    siAgentService: SIAgentServiceImpl =
                                    Depends(injectSIAgentService)):

    backlog = await siAgentService.request_to_get_backlogs(
        si_agent_backlog_request_form.to_si_agent_current_phase_request())

    return JSONResponse(content={"backlog": backlog}, status_code=status.HTTP_200_OK)


@siAgentRouter.post("/get-file-list")
async def request_to_get_file_list(siAgentFileListRequestForm: SIAgentFileListRequestForm,
                                    siAgentService: SIAgentServiceImpl =
                                    Depends(injectSIAgentService)):

    file_list = await siAgentService.request_to_get_file_list(
        siAgentFileListRequestForm.toSIAgentFileListRequest())

    return JSONResponse(content={"file_list": file_list}, status_code=status.HTTP_200_OK)


@siAgentRouter.post("/get-test-reports")
async def request_to_get_test_reports(si_agent_test_reports_request_form: SIAgentTestReportsRequestForm,
                                    siAgentService: SIAgentServiceImpl =
                                    Depends(injectSIAgentService)):

    test_reports = await siAgentService.request_to_get_test_reports(
        si_agent_test_reports_request_form.to_si_agent_test_reports_request())

    return JSONResponse(content={"test_reports": test_reports}, status_code=status.HTTP_200_OK)
