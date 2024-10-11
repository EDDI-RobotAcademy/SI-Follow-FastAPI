from abc import ABC, abstractmethod
from typing import List, Optional


class MultipleUserTestPointRepository(ABC):
    @abstractmethod
    async def checkUserTestPointIdle(self, userDefinedReceiverFastAPIChannel, userToken):
        pass

