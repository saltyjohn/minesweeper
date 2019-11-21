"""main.py runs the game."""

from components.MineField import MineField
from utils.utils import display_board, clean_input
from utils.ui import print_header, start_menu

MODE = {"easy": (0.1, 5), "medium": (0.2, 7), "hard": (0.3, 9)}


def play_game():
    """Function runs game loop within main loop."""
    density, size = MODE["hard"]
    minefield = MineField(density=density, size=size)
    minefield.create_board()

    player_moves = []

    while True:
        display_board(minefield)

        # Player turn options
        usr_move = clean_input("[F]lag, [S]elect or [Q]uit: ")

        # Placing these here to keep the player from selecting
        #   the row and col before redoing the move...
        if usr_move == "q":
            break  # quit session
        elif usr_move not in {"f", "s"}:
            print(f"\nSorry, but {usr_move} is not a recognized command...\n")
            continue

        usr_row = clean_input("Choose the row: ")
        usr_col = clean_input("Choose the column: ")
        print()

        # Subtract 1 to account for row/col number labels
        x = int(usr_col) - 1
        y = int(usr_row) - 1

        # Keep track of moves and warn player double guesses
        move_coords = (x, y)
        if move_coords in player_moves:
            print(
                f"The location, [Row: {usr_row}, Col: {usr_col}],"
                f" has already been selected!\n"
            )
            continue
        else:
            player_moves.append(move_coords)

        if usr_move == "f":
            # TODO: this might not to be stored in a variable....
            minefield.select_square(x, y, flag=True)
            continue
        elif usr_move == "s":
            next_move = minefield.select_square(x, y)
            if next_move:
                continue
            else:
                display_board(minefield)
                print(f"Square ({usr_row}, {usr_col}) was a bomb...")
                break


def main():
    # TODO: settings menu (no. of mines, size of field, etc)
    cmd = start_menu()

    # Main Game Loop
    while True:
        print()
        if cmd == "n":
            play_game()
            break
        elif cmd == "q":
            break
        else:
            print(f'\nSorry, the command "{cmd}"" does not exist...')
            cmd = start_menu()

    print("\nSee you later!")


if __name__ == "__main__":
    print_header()
    main()
    print()
