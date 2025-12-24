from abc import ABC, abstractmethod

class IdolAbstract(ABC):
    @abstractmethod
    def show_all_idols(self):
        pass
    
    @abstractmethod
    def create_idol(self):
        pass
    
    @abstractmethod
    def update_idol(self):
        pass
    
    @abstractmethod
    def delete_idol(self):
        pass