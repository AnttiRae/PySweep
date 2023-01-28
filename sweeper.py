from minefield import Minefield


class Sweeper:

    @staticmethod
    def sweep_tile(minefield: Minefield, x_coordinate, y_coordinate):
        if len(minefield.mines) == 0:
            return
        coordinates = [x_coordinate, y_coordinate]
        for mine in minefield.mines:
            if coordinates == mine.coordinates:
                print("Bang!")


