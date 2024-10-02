from abc import ABC, abstractmethod
from typing import List, Optional


class SIAgentService(ABC):
    @abstractmethod
    def requestToCheckSIAgentIdle(self, siAgentIdleRequest):
        pass

