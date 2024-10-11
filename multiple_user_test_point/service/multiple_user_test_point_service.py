from abc import ABC, abstractmethod
from typing import List, Optional


class MultipleUserTestPointService(ABC):
    @abstractmethod
    def requestToCheckMultipleUserTestPoint(self, userTestPointRequest):
        pass

