from pydantic import BaseModel

from si_agent.service.request.si_agent_file_content_request import SIAgentFileContentRequest


class SIAgentFileContentRequestForm(BaseModel):
    user_token: str
    project_name: str
    file_name: str

    def toSIAgentFileContentRequest(self) -> SIAgentFileContentRequest:
        return SIAgentFileContentRequest(user_token=self.user_token, project_name=self.project_name, file_name=self.file_name)
