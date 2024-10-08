from pydantic import BaseModel

from gpu_management.service.request.gpu_server_status_check_request import CheckGPUAvailableRequest


class CheckGPUAvailableRequestForm(BaseModel):
    api_url: str

    def toCheckGPUAvailableRequest(self) -> CheckGPUAvailableRequest:
        return CheckGPUAvailableRequest(api_url=self.api_url)
