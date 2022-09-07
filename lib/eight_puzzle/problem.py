import random
from typing import List, Tuple

from ..problem.problem import Problem as ABCProblem;
from ..problem.action import Action as ABCAction;
from ..problem.action import State as ABCState;

from .board import Board, new_board_from_state_serial, new_solved_board
from .action import Up, Right, Down, Left

class Problem(ABCProblem):
    """Problem is an EightPuzzle problem to be solved by an agent"""

    def __init__(self, goal: Board, initial_board: Board):
        """Construct a new Problem."""
        self.goal: Board = goal
        self.initial_board: Board = initial_board
        self.actions: List[ABCAction] = [
            Up(),
            Right(),
            Down(),
            Left(),
        ]

    def initial_state(self) -> ABCState:
        """Return the initial state of the problem."""
        return self.initial_board
    
    def actions(self) -> List[ABCAction]:
        """Return the list of possible actions."""
        return self.actions
    
    def transition_model(self, state: ABCState, action: ABCAction) -> ABCState:
        """Return the successor state of the application of the action on the state."""
        return action.apply(new_board_from_state_serial(state.serialize()))
    
    def is_goal(self, state: ABCState) -> bool:
        """Check if the state is a goal state."""
        return state.serialize() == self.goal.serialize()
    
    def step_cost(self, state: ABCState, action: ABCAction) -> int:
        """Return the cost of applying an action to a state."""
        return 1

def new_random_problem(size: int, seed: int, min_actions: int, max_actions: int) -> Problem:
    """Construct a random problem."""
    this_board = new_solved_board(size)

    actions: List[ABCAction] = [
        Up(),
        Right(),
        Down(),
        Left(),
    ]

    random.seed(seed)

    n_steps = random.randrange(min_actions, max_actions)

    for _step_no in range(n_steps):
        this_action = random.choice(actions)
        successor_board = this_action.apply(this_board)

        if successor_board is None:
            continue

        this_board = successor_board

    return Problem(new_solved_board(size), this_board)
