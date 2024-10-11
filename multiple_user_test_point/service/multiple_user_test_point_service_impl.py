from multiple_user_test_point.repository.multiple_user_test_point_repository_impl import \
    MultipleUserTestPointRepositoryImpl
from multiple_user_test_point.service.request.user_test_point_request import UserTestPointRequest
from template.include.socket_server.utility.color_print import ColorPrinter

from multiple_user_test_point.service.multiple_user_test_point_service import MultipleUserTestPointService
from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl


class MultipleUserTestPointServiceImpl(MultipleUserTestPointService):

    def __init__(self, userDefinedQueueRepository: UserDefinedQueueRepositoryImpl):
        self.__multipleUserTestPointRepository = MultipleUserTestPointRepositoryImpl()
        self.__userDefinedQueueRepository = userDefinedQueueRepository

    async def requestToCheckMultipleUserTestPoint(self, userTestPointRequest: UserTestPointRequest):
        userDefinedReceiverFastAPIChannel = self.__userDefinedQueueRepository.getUserDefinedSocketReceiverFastAPIChannel()
        ColorPrinter.print_important_message("requestToCheckMultipleUserTestPoint()")
        return await self.__multipleUserTestPointRepository.checkUserTestPointIdle(
            userDefinedReceiverFastAPIChannel,
            userTestPointRequest.toUserToken()
        )

