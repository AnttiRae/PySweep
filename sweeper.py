from minefield import Minefield


class Sweeper:
    minefield = Minefield()

    def __init__(self, minefield):
        self.minefield = minefield

    # @staticmethod
    def sweep_tile(self, x_coordinate, y_coordinate):
        if len(self.minefield.mines) == 0:
            return
        coordinates = [x_coordinate, y_coordinate]
        for mine in self.minefield.mines:
            if coordinates == mine.coordinates:
                print("Bang!")
                self.game_over()
            else:
                self.get_user_coordinate_input()

    @staticmethod
    def game_over():
        print('Game over')
        input('Press any key to return to start')

    def main_menu(self):
        print('Welcome to - MineSweeper')
        input('Press any key to start')
        self.get_user_coordinate_input()

    def get_user_coordinate_input(self):
        while True:
            try:
                coordinates = input('Input coordinates: ').split(' ')
                x_coordinate = int(coordinates[0])
                y_coordinate = int(coordinates[1])
                if len(coordinates) > 2:
                    raise ValueError
            except (ValueError, IndexError):
                print("Inputted coordinates invalid, try again!")
                continue
            else:
                break

        self.sweep_tile(x_coordinate, y_coordinate)

