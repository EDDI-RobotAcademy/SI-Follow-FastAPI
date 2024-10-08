from fastapi import APIRouter, Depends, status
from starlette.responses import JSONResponse

from gpu_management.controller.request_form.gpu_server_status_check_request_form import CheckGPUAvailableRequestForm
from gpu_management.service.gpu_management_service_impl import GPUManagementServiceImpl
from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl

gpu_management_router = APIRouter()

async def injectGPUManagementService() -> GPUManagementServiceImpl:
    return GPUManagementServiceImpl(UserDefinedQueueRepositoryImpl.getInstance())

@gpu_management_router.post("/check-gpu-available")
async def requestToCheckSIAgentIdle(checkGPUAvailableRequestForm: CheckGPUAvailableRequestForm,
                                    gpuManagementService: GPUManagementServiceImpl =
                                    Depends(injectGPUManagementService)):

    gpu_status = await gpuManagementService.check_gpu_server_available(
        checkGPUAvailableRequestForm.toCheckGPUAvailableRequest())

    return JSONResponse(content={"available": gpu_status}, status_code=status.HTTP_200_OK)
