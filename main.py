from minefield import Minefield
from sweeper import Sweeper

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    minefield = Minefield(width=10, height=10, number_of_mines=25)

    minefield.generate_tiles()
    minefield.place_mines()

    minefield.draw_minefield()

    sweeper = Sweeper(minefield)

    # for tile in minefield.tiles:
    #     print(tile.calculate_tile_number(minefield))

    # sweeper.main_menu()
