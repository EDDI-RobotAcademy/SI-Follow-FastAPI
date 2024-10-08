from pydantic import BaseModel


class CheckGPUAvailableRequest(BaseModel):
    api_url: str

    def to_api_url(self) -> str:
        return self.api_url
