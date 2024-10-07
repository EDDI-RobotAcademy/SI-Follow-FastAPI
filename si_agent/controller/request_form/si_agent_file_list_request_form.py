from pydantic import BaseModel

from si_agent.service.request.si_agent_file_list_request import SIAgentFileListRequest


class SIAgentFileListRequestForm(BaseModel):
    user_token: str
    project_name: str

    def toSIAgentFileListRequest(self) -> SIAgentFileListRequest:
        return SIAgentFileListRequest(user_token=self.user_token, project_name=self.project_name)
