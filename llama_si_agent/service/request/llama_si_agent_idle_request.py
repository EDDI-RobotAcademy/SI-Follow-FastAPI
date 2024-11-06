from pydantic import BaseModel


class LlamaSIAgentIdleRequest(BaseModel):
    userToken: str

    def toUserToken(self) -> str:
        return self.userToken
