from abc import ABC, abstractmethod


class IdolAbstract(ABC):
    @abstractmethod
    def create_idol(self):
        pass

    @abstractmethod
    def delete_idol(self, idol_id):
        pass

    @abstractmethod
    def view_all(self):
        pass

    @abstractmethod
    def update_idol(self, idol_id):
        pass
