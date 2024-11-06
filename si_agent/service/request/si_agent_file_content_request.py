from pydantic import BaseModel


class SIAgentFileContentRequest(BaseModel):
    user_token: str
    project_name: str
    file_name: str

    def to_user_token(self) -> str:
        return self.user_token
    
    def to_project_name(self) -> str:
        return self.project_name
    
    def to_file_name(self) ->str:
        return self.file_name
