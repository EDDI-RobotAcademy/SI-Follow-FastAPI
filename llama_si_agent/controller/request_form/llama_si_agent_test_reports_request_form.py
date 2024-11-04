from pydantic import BaseModel

from llama_si_agent.service.request.llama_si_agent_test_reports_request import LlamaSIAgentTestReportsRequest


class LlamaSIAgentTestReportsRequestForm(BaseModel):
    user_token: str
    project_name: str

    def to_si_agent_test_reports_request(self) -> LlamaSIAgentTestReportsRequest:
        return LlamaSIAgentTestReportsRequest(user_token=self.user_token, project_name=self.project_name)
