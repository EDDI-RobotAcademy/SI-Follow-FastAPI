from pydantic import BaseModel

from llama_si_agent.service.request.llama_si_agent_current_phase_request import LlamaSIAgentCurrentPhaseRequest


class LlamaSIAgentCurrentPhaseRequestForm(BaseModel):
    user_token: str
    project_name: str

    def to_si_agent_current_phase_request(self) -> LlamaSIAgentCurrentPhaseRequest:
        return LlamaSIAgentCurrentPhaseRequest(user_token=self.user_token, project_name=self.project_name)
