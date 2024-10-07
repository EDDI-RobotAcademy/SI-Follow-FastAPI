from abc import ABC, abstractmethod
from typing import List, Optional


class SIAgentService(ABC):
    @abstractmethod
    def requestToCheckSIAgentIdle(self, siAgentIdleRequest):
        pass


    @abstractmethod
    def request_to_get_current_phase(self, siAgentIdleRequest):
        pass
    
