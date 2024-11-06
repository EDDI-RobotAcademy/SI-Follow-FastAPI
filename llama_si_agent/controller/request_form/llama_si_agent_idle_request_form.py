from pydantic import BaseModel

from llama_si_agent.service.request.llama_si_agent_idle_request import LlamaSIAgentIdleRequest


class LlamaSIAgentIdleRequestForm(BaseModel):
    userToken: str

    def toSIAgentIdleRequest(self) -> LlamaSIAgentIdleRequest:
        return LlamaSIAgentIdleRequest(userToken=self.userToken)
