from .tile import Tile
from .colors import bcolors
import random


class Minefield:
    width, height, number_of_mines = 5, 5, 5
    tiles = []

    def __init__(self, width=5, height=5, number_of_mines=5):
        self.width = width
        self.height = height
        self.number_of_mines = number_of_mines

    def generate_tiles(self):
        self.tiles = []
        for i in range(self.width):
            for j in range(self.height):
                self.tiles.append(Tile([i, j]))

    # place X amount of mines on field on random locations
    def place_mines(self):
        if len(self.tiles) == 0:
            return
        tiles_to_mine = random.sample(self.tiles, self.number_of_mines)
        for tile in tiles_to_mine:
            tile.mine = True

    def calculate_tile_numbers(self):
        for tile in self.tiles:
            tile.calculate_tile_number(self)

    def draw_minefield(self):
        for tile in self.tiles:
            if tile.coordinates[1] == self.width-1:
                print(f' {tile} ')
            elif tile.coordinates[1] == 0:
                print(f"{bcolors.FAIL}{tile.coordinates[0]}|{bcolors.ENDC}", end='')
                print(f' {tile} ', end='')
            else:
                print(f' {tile} ', end='')
        print(f"{bcolors.FAIL}*|", end='')
        for x in range(self.width):
            print(f"-{x}-", end='')
        print(f"{bcolors.ENDC}")



