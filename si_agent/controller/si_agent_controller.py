from fastapi import APIRouter, Depends, status
from starlette.responses import JSONResponse

from si_agent.controller.request_form.si_agent_idle_request_form import SIAgentIdleRequestForm
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
