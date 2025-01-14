from .colors import bcolors

class Tile:
    coordinates = []
    mine = False
    popped = False
    number = 0

    def __init__(self, coordinates: list, mine: bool = False):
        self.coordinates = coordinates
        self.mine = mine

    def __str__(self):
        if not self.popped:
            return f"{bcolors.OKGREEN}#{bcolors.ENDC}"
        elif self.popped and self.mine:
            return f"{bcolors.OKBLUE}X{bcolors.ENDC}"
        else:
            return f"{bcolors.WARNING}{str(self.number)}{bcolors.ENDC}"

    def pop_tile(self):
        self.popped = True

    def calculate_tile_number(self, minefield):
        number_of_mines = 0
        tiles_to_find = [
            [self.coordinates[0]+1, self.coordinates[1]],
            [self.coordinates[0], self.coordinates[1]+1],
            [self.coordinates[0]+1, self.coordinates[1]+1],
            [self.coordinates[0]-1, self.coordinates[1]],
            [self.coordinates[0], self.coordinates[1]-1],
            [self.coordinates[0]-1, self.coordinates[1]-1],
            [self.coordinates[0]+1, self.coordinates[1]-1],
            [self.coordinates[0]-1, self.coordinates[1]+1]
        ]
        for tile in minefield.tiles:
            for i in range(len(tiles_to_find)):
                if tile.coordinates == tiles_to_find[i] and tile.mine:
                    number_of_mines += 1
                    break
        self.number = number_of_mines
