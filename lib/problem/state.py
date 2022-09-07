from abc import ABC, abstractmethod

class State(ABC):
    """State is the state of a problem"""

    @abstractmethod
    def serialize(self) -> str:
        """serialize returns the serialized state"""
        pass
