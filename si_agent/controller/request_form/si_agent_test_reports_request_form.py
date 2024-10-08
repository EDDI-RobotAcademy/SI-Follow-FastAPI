from pydantic import BaseModel

from si_agent.service.request.si_agent_test_reports_request import SIAgentTestReportsRequest


class SIAgentTestReportsRequestForm(BaseModel):
    user_token: str
    project_name: str

    def to_si_agent_test_reports_request(self) -> SIAgentTestReportsRequest:
        return SIAgentTestReportsRequest(user_token=self.user_token, project_name=self.project_name)
