from pydantic import BaseModel


class LlamaSIAgentTestReportsRequest(BaseModel):
    user_token: str
    project_name: str

    def to_user_token(self) -> str:
        return self.user_token
    
    def to_project_name(self) -> str:
        return self.project_name
