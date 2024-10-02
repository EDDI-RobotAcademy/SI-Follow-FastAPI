from pydantic import BaseModel


class SIAgentIdleRequest(BaseModel):
    userToken: str

    def toUserToken(self) -> str:
        return self.userToken
