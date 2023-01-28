from minefield import Minefield
from sweeper import Sweeper

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    minefield = Minefield()

    minefield.place_mines()

    minefield.draw_minefield()

    sweeper = Sweeper()

    for mine in minefield.mines:
        print(mine)

    sweeper.sweep_tile(minefield, x_coordinate=4, y_coordinate=3)

