from pydantic import BaseModel

from llama_si_agent.service.request.llama_si_agent_backlog_request import LlamaSIAgentBacklogRequest


class LlamaSIAgentBacklogRequestForm(BaseModel):
    user_token: str
    project_name: str

    def to_si_agent_current_phase_request(self) -> LlamaSIAgentBacklogRequest:
        return LlamaSIAgentBacklogRequest(user_token=self.user_token, project_name=self.project_name)
