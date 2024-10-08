from abc import ABC, abstractmethod
from typing import List, Optional


class GPUManagementService(ABC):
    @abstractmethod
    def check_gpu_server_available(self, siAgentIdleRequest):
        pass
