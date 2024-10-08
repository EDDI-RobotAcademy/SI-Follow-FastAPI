from pydantic import BaseModel

from si_agent.service.request.si_agent_current_phase_request import SIAgentCurrentPhaseRequest


class SIAgentCurrentPhaseRequestForm(BaseModel):
    user_token: str
    project_name: str

    def to_si_agent_current_phase_request(self) -> SIAgentCurrentPhaseRequest:
        return SIAgentCurrentPhaseRequest(user_token=self.user_token, project_name=self.project_name)
