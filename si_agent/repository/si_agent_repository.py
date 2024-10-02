from abc import ABC, abstractmethod
from typing import List, Optional


class SIAgentRepository(ABC):
    @abstractmethod
    async def checkSIAgentIdle(self, userDefinedReceiverFastAPIChannel, userToken):
        pass

