def print_header(pad=10, title="Minesweeper"):
    print("-" * (2 * pad + len(title) + 2))
    print("-" * pad, title, "-" * pad)
    print("-" * (2 * pad + len(title) + 2))


def start_menu():
    user_options = "\nWelcome! \n\nStart a [N]ew game, or [Q]uit?\n>>> "
    cmd = input(user_options).lower()
    return cmd
