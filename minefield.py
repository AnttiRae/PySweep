from tile import Tile
import random


class Minefield:
    width, height, number_of_mines = 5, 5, 5
    tiles = []

    def __init__(self, width=5, height=5, number_of_mines=5):
        self.width = width
        self.height = height
        self.number_of_mines = number_of_mines

    def generate_tiles(self):
        for i in range(self.width):
            print('generating row of tiles')
            for j in range(self.height):
                print('generating tile')
                self.tiles.append(Tile([i, j]))

    # place X amount of mines on field on random locations
    def place_mines(self):
        if len(self.tiles) == 0:
            return
        tiles_to_mine = random.sample(self.tiles, self.number_of_mines)
        for tile in tiles_to_mine:
            tile.mine = True

    def draw_minefield(self):
        print('  | 0 1 2 3 4 5 6 7 ')
        for i in range(self.width):
            print(i, end=' | ')

            for j in range(self.height):
                print('#', end=' ')
            print()
