from pydantic import BaseModel

from llama_si_agent.service.request.llama_si_agent_file_content_request import LlamaSIAgentFileContentRequest


class LlamaSIAgentFileContentRequestForm(BaseModel):
    user_token: str
    project_name: str
    file_name: str

    def toSIAgentFileContentRequest(self) -> LlamaSIAgentFileContentRequest:
        return LlamaSIAgentFileContentRequest(user_token=self.user_token, project_name=self.project_name, file_name=self.file_name)
