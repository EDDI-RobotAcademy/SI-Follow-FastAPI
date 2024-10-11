from pydantic import BaseModel


class UserTestPointRequest(BaseModel):
    userToken: str

    def toUserToken(self) -> str:
        return self.userToken
