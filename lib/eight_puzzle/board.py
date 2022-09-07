from typing import Tuple, Dict, List
import json

from ..problem.state import State as ABCState
from ..board.board import Board as EntityBoard, new_solved_board as new_solved_entity_board
from ..board.tile import Tile as EntityTile, new_tile_from_json

class Board(ABCState):
    """Board is an n-size eight puzzle board."""

    def __init__(self, board: EntityBoard):
        """Construct a new eight puzzle board"""
        self.board = board

    def serialize(self) -> str:
        """Serialize this board."""
        return json.dumps(self.reprJSON(), cls=ComplexEncoder)
    
    def get_tile(self, position_row: int, position_col: int) -> EntityTile:
        """Return the tile at the specified position."""
        return self.board.get_tile(position_row, position_col)
    
    def swap(self, position_1: Tuple[int, int], position_2: Tuple[int, int]) -> str:
        """Swap two tiles at the specified positions.
        
        Returns none if successful, else error message."""
        return self.board.swap(position_1, position_2)
    
    def get_empty_position(self) -> Tuple[int, int]:
        """Get the position for the empty tile."""
        return self.board.get_empty_position()
    
    def get_size(self) -> int:
        """Get the size of the board."""
        return self.board.get_size()
    
    def reprJSON(self) -> Dict:
        return dict(board=self.board)

def new_solved_board(size: int) -> Board:
    """Construct a new solved board."""
    return Board(new_solved_entity_board(size))

def new_tiles_from_json(arr: List) -> List[List[EntityTile]]:
    return list(map(lambda r : list(map(lambda t : new_tile_from_json(t), r)), arr))

def new_board_from_json(d: Dict) -> Board:
    return Board(EntityBoard(d["board"]["size"], new_tiles_from_json(d["board"]["tiles"]), (d["board"]["empty_position"][0], d["board"]["empty_position"][1])))

def new_board_from_state_serial(serial: str) -> Board:
    """Construct a new board from serial state."""
    board_dict = json.loads(serial)
    return new_board_from_json(board_dict)

class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj,'reprJSON'):
            return obj.reprJSON()
        else:
            return json.JSONEncoder.default(self, obj)
