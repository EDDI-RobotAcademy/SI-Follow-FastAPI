from abc import ABC, abstractmethod
from typing import List, Optional


class SIAgentRepository(ABC):
    @abstractmethod
    async def checkSIAgentIdle(self, userDefinedReceiverFastAPIChannel, userToken):
        pass
    
    @abstractmethod
    async def get_current_phase(self, userDefinedReceiverFastAPIChannel, userToken):
        pass
    
    @abstractmethod
    async def get_backlogs(self, userDefinedReceiverFastAPIChannel, userToken):
        pass

