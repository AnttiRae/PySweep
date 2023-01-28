from mine import Mine
import functools
import random


class Minefield:
    width, height, number_of_mines = 5, 5, 5
    mines = []

    def __init__(self, width=5, height=5, number_of_mines=5):
        self.width = width
        self.height = height
        self.number_of_mines = number_of_mines

    #  place X amount of mines on field on random locations
    def place_mines(self):
        for mine in range(self.number_of_mines):
            coordinates = list([random.randint(0, 5), random.randint(0, 5)])
            self.mines.append(Mine(coordinates))

    def draw_minefield(self):
        print('* | A B C D E F G H ')
        for i in range(self.width):
            print(i, end=' | ')

            for j in range(self.height):
                print('#', end=' ')
            print()
