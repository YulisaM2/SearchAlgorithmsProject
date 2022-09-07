from ..problem.action import Action as ABCAction
from ..problem.state import State as ABCState

from .board import new_board_from_state_serial

class Up(ABCAction):
    def serialize(self) -> str:
        return "UP"
    
    def apply(self, state: ABCState) -> ABCState:
        thisBoard = new_board_from_state_serial(state.serialize())
        (row, col) = thisBoard.get_empty_position()
        if row <= 0:
            return None
        error_msg = thisBoard.swap((row, col), (row - 1, col))
        if error_msg is not None:
            print(error_msg)
            return None
        return thisBoard

class Right(ABCAction):
    def serialize(self) -> str:
        return "RIGHT"
    
    def apply(self, state: ABCState) -> ABCState:
        thisBoard = new_board_from_state_serial(state.serialize())
        (row, col) = thisBoard.get_empty_position()
        if col >= thisBoard.get_size() - 1:
            return None
        error_msg = thisBoard.swap((row, col), (row, col + 1))
        if error_msg is not None:
            print(error_msg)
            return None
        return thisBoard

class Down(ABCAction):
    def serialize(self) -> str:
        return "DOWN"
    
    def apply(self, state: ABCState) -> ABCState:
        thisBoard = new_board_from_state_serial(state.serialize())
        (row, col) = thisBoard.get_empty_position()
        if row >= thisBoard.get_size() - 1:
            return None
        error_msg = thisBoard.swap((row, col), (row + 1, col))
        if error_msg is not None:
            print(error_msg)
            return None
        return thisBoard

class Left(ABCAction):
    def serialize(self) -> str:
        return "LEFT"
    
    def apply(self, state: ABCState) -> ABCState:
        thisBoard = new_board_from_state_serial(state.serialize())
        (row, col) = thisBoard.get_empty_position()
        if col <= 0:
            return None
        error_msg = thisBoard.swap((row, col), (row, col - 1))
        if error_msg is not None:
            print(error_msg)
            return None
        return thisBoard
