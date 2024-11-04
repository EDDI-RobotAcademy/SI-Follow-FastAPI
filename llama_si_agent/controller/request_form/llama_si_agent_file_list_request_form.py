from pydantic import BaseModel

from llama_si_agent.service.request.llama_si_agent_file_list_request import LlamaSIAgentFileListRequest


class LlamaSIAgentFileListRequestForm(BaseModel):
    user_token: str
    project_name: str

    def toSIAgentFileListRequest(self) -> LlamaSIAgentFileListRequest:
        return LlamaSIAgentFileListRequest(user_token=self.user_token, project_name=self.project_name)
