from abc import ABC, abstractmethod
from typing import List, Optional


class SIAgentService(ABC):
    @abstractmethod
    def requestToCheckSIAgentIdle(self, siAgentIdleRequest):
        pass


    @abstractmethod
    def request_to_get_current_phase(self, si_agent_current_phase_request):
        pass
    
    @abstractmethod
    def request_to_get_backlogs(self, siAgentIdleRequest):
        pass
    
    @abstractmethod
    def request_to_get_file_list(self, si_agent_file_list_request):
        pass
    

