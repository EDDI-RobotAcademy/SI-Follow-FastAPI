from pydantic import BaseModel

from multiple_user_test_point.service.request.user_test_point_request import UserTestPointRequest


class MultipleUserTestPointRequestForm(BaseModel):
    userToken: str

    def toUserTestPointRequest(self) -> UserTestPointRequest:
        return UserTestPointRequest(userToken=self.userToken)
