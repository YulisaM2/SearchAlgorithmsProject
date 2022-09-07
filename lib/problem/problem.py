from abc import ABC, abstractmethod
from typing import List, Tuple

from .state import State
from .action import Action

class Problem(ABC):
    """Problem is an abstract problem to be solved by an agent"""

    @abstractmethod
    def initial_state(self) -> State:
        """initial_state returns the initial state of the problem"""
        pass

    @abstractmethod
    def actions(self) -> List[Action]:
        """actions returns the list of possible actions"""
        pass

    @abstractmethod
    def transition_model(self, state: State, action: Action) -> State:
        """transition_model returns the successor state of the application of the action on the state"""
        pass

    @abstractmethod
    def is_goal(self, state: State) -> bool:
        """is_goal checks if the passed state is a goal state"""
        pass

    @abstractmethod
    def step_cost(self, state: State, action: Action) -> int:
        """step_cost returns the cost of applying an action to a state"""
        pass
