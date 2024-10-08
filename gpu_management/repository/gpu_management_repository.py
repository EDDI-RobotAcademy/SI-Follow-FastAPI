from abc import ABC, abstractmethod
from typing import List, Optional


class GPUManagementRepository(ABC):
    @abstractmethod
    async def check_gpu_server_available(self, userDefinedReceiverFastAPIChannel, api_url):
        pass
