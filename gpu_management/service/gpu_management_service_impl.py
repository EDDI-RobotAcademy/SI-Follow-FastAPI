from gpu_management.service.gpu_management_service import GPUManagementService
from gpu_management.service.request.gpu_server_status_check_request import CheckGPUAvailableRequest
from gpu_management.repository.gpu_management_repository_impl import GPUManagementRepositoryImpl
from template.include.socket_server.utility.color_print import ColorPrinter
from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl


class GPUManagementServiceImpl(GPUManagementService):

    def __init__(self, userDefinedQueueRepository: UserDefinedQueueRepositoryImpl):
        self.__gpuManagementRepository = GPUManagementRepositoryImpl()
        self.__userDefinedQueueRepository = userDefinedQueueRepository

    async def check_gpu_server_available(self, check_gpu_available_request: CheckGPUAvailableRequest):
        userDefinedReceiverFastAPIChannel = self.__userDefinedQueueRepository.getUserDefinedSocketReceiverFastAPIChannel()
        ColorPrinter.print_important_message("requestToCheckGPUAvailable()")
        return await self.__gpuManagementRepository.check_gpu_server_available(
            userDefinedReceiverFastAPIChannel,
            check_gpu_available_request.to_api_url()
        )
