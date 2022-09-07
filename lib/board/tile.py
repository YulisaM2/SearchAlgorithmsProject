from typing import Optional, Dict

class Tile:
    def __init__(self, value: Optional[int]):
        self.value = value
    
    def get_value(self) -> Optional[int]:
        return self.value
    
    def reprJSON(self) -> Dict:
        return dict(value=self.value)

def new_empty_tile() -> Tile:
    return Tile(None)

def new_tile(value: int) -> Tile:
    return Tile(value)

def new_tile_from_json(dict: Dict) -> Tile:
    return Tile(dict["value"])
