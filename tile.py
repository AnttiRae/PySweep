class Tile:
    coordinates = []
    mine = False

    def __init__(self, coordinates: list, mine: bool = False):
        self.coordinates = coordinates
        self.mine = mine

    def __str__(self):
        if self.mine:
            return f'Mine: {self.coordinates}'
        return f'Tile: {self.coordinates}'

    def calculate_tile_number(self):
        if self.mine:
            return
        
