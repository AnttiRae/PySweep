from minefield import Minefield
from sweeper import Sweeper

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    minefield = Minefield()

    minefield.place_mines()

    minefield.draw_minefield()

    sweeper = Sweeper(minefield)

    for mine in minefield.mines:
        print(mine)

    sweeper.main_menu()
