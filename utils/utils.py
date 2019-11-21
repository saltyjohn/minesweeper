def display_board(minefield):
    board = minefield.board
    output = ""

    for row in range(len(board) + 1):
        output_row = ""
        for col in range(len(board) + 1):
            # Top row, column numbering
            if row == 0:
                if col == 0:
                    output_row += "  "
                    continue
                else:
                    output_row += f" {str(col)} "
                    continue
            # First column, row numbering
            if col == 0:
                # no front space to account for left side
                output_row += f"{str(row)} "
                continue

            # Square .shown character
            output_row += f" {board[row - 1][col - 1].display_char} "
        output += f"{output_row}\n"

    print(output)


def clean_input(string):
    cmd = input(string).strip().lower()
    return cmd
