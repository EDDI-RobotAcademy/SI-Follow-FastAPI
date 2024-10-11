from fastapi import APIRouter, Depends, status
from starlette.responses import JSONResponse

from multiple_user_test_point.controller.request_form.multiple_user_test_point_request_form import \
    MultipleUserTestPointRequestForm
from multiple_user_test_point.service.multiple_user_test_point_service_impl import MultipleUserTestPointServiceImpl
from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl

multipleUserTestPointRouter = APIRouter()

async def injectMultipleUserTestPointService() -> MultipleUserTestPointServiceImpl:
    return MultipleUserTestPointServiceImpl(UserDefinedQueueRepositoryImpl.getInstance())

@multipleUserTestPointRouter.post("/check-user-request-idle")
async def requestToCheckMultipleUserTestPoint(multipleUserTestPointRequestForm: MultipleUserTestPointRequestForm,
                                              multipleUserTestPointService: MultipleUserTestPointServiceImpl =
                                              Depends(injectMultipleUserTestPointService)):

    isIdle = await multipleUserTestPointService.requestToCheckMultipleUserTestPoint(
        multipleUserTestPointRequestForm.toUserTestPointRequest())

    return JSONResponse(content={"isIdle": isIdle}, status_code=status.HTTP_200_OK)
