from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def __init__(self, observer_id, name, website):
        self.id = observer_id
        self.name = name
        self.website = website

    @abstractmethod
    def update(self, subject):
        pass