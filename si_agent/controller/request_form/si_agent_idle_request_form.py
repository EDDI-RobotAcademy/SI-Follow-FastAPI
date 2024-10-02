from pydantic import BaseModel

from si_agent.service.request.si_agent_idle_request import SIAgentIdleRequest


class SIAgentIdleRequestForm(BaseModel):
    userToken: str

    def toSIAgentIdleRequest(self) -> SIAgentIdleRequest:
        return SIAgentIdleRequest(userToken=self.userToken)
