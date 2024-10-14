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
    def request_to_get_backlogs(self, si_agent_backlog_request):
        pass
    
    @abstractmethod
    def request_to_get_file_list(self, si_agent_file_list_request):
        pass
    
    @abstractmethod
    def request_to_get_file_content(self, si_agent_file_content_request):
        pass
    
    @abstractmethod
    def request_to_get_test_reports(self, si_agent_test_reports_request):
        pass
    
    @abstractmethod
    def request_to_get_code_review(self, si_agent_code_review_request):
        pass
    

