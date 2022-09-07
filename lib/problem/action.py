from abc import ABC, abstractmethod

from .state import State

class Action(ABC):
    """Action is a possible thing to do to reach a solution based on a problem state"""

    @abstractmethod
    def serialize(self) -> str:
        """serialize returns the serialized action"""
        pass

    @abstractmethod
    def apply(self, state: State) -> State:
        """applies this action on the specified state and returns the successor"""
        pass
