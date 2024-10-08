from pydantic import BaseModel

from si_agent.service.request.si_agent_code_review_request import SIAgentCodeReviewRequest


class SIAgentCodeReviewRequestForm(BaseModel):
    user_token: str
    project_name: str

    def to_si_agent_code_review_request(self) -> SIAgentCodeReviewRequest:
        return SIAgentCodeReviewRequest(user_token=self.user_token, project_name=self.project_name)
