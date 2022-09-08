from typing import List, Tuple, Dict
from copy import deepcopy
import numpy as np

from .tile import Tile, new_empty_tile, new_tile

class Board:
    def __init__(self, size: int, tiles: List[List[Tile]], empty_position: Tuple[int, int]):
        self.size = size
        self.tiles = tiles
        self.empty_position = empty_position
    
    def get_tile(self, position_row: int, position_col: int) -> Tile:
        if position_row < 0 or position_row >= self.size or position_col < 0 or position_col >= self.size:
            return None
        
        return self.tiles[position_row][position_col]
    
    def swap(self, position_1: Tuple[int, int], position_2: Tuple[int, int]) -> str:
        if position_1[0] < 0 or position_1[0] >= self.size or position_2[0] < 0 or position_2[1] >= self.size:
            return "expected position coordinates < " + self.size

        temp = self.tiles[position_2[0]][position_2[1]]
        self.tiles[position_2[0]][position_2[1]] = self.tiles[position_1[0]][position_1[1]]
        self.tiles[position_1[0]][position_1[1]] = temp

        if self.tiles[position_1[0]][position_1[1]].get_value() is None:
            self.empty_position = (position_1[0], position_1[1])
        elif self.tiles[position_2[0]][position_2[1]].get_value() is None:
            self.empty_position = (position_2[0], position_2[1])
        else:
            print("ERROR: moved something that wasn't the empty tile!")
        
        return None
    
    def get_empty_position(self) -> Tuple[int, int]:
        return self.empty_position
    
    def get_size(self) -> int:
        return self.size
    
    def reprJSON(self) -> Dict:
        return dict(size=self.size, tiles=self.tiles, empty_position=self.empty_position)
    
    def display(self) -> str:
        result = []
        for row_tile in self.tiles:
            row_res = []
            for tile in row_tile:
                value = tile.get_value()
                if value is None:
                    row_res.append("0")
                    continue
                row_res.append(str(value))
            result.append(", ".join(row_res))
        return "\n".join(result)
    
    def to_np_matrix(self):
        l = list(map(lambda tile_row : list(map(lambda tile : tile.get_value() if tile.get_value() is not None else np.empty, tile_row)), self.tiles))
        return np.mat(l)

def new_solved_board(size: int) -> Board:
    tiles: List[Tile] = []

    for iRow in range(size):
        tile_row = []

        for jCol in range(size):
            if iRow == 0 and jCol == 0:
                tile_row.append(new_empty_tile())
                continue

            tile_row.append(new_tile(iRow * size + jCol))
        
        tiles.append(tile_row)
    
    return Board(size, tiles, (0, 0))
