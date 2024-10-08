from abc import ABC, abstractmethod
from typing import List, Optional


class SIAgentRepository(ABC):
    @abstractmethod
    async def checkSIAgentIdle(self, userDefinedReceiverFastAPIChannel, userToken):
        pass
    
    @abstractmethod
    async def get_current_phase(self, userDefinedReceiverFastAPIChannel, userToken, project_name):
        pass
    
    @abstractmethod
    async def get_backlogs(self, userDefinedReceiverFastAPIChannel, user_token, project_name):
        pass
    
    @abstractmethod
    async def get_file_list(self, userDefinedReceiverFastAPIChannel, user_token, project_name):
        pass
    
    @abstractmethod
    async def get_test_reports(self, userDefinedReceiverFastAPIChannel, user_token, project_name):
        pass