class MineSquare:
    def __init__(self, is_mine, neighbor_count, coords, display_char="#"):
        self.is_mine = is_mine
        self.neighbor_count = neighbor_count
        self.display_char = display_char
        self.coords = coords

    def __repr__(self):
        return (
            f"{self.__class__.__name__}("
            f"{self.is_mine!r}, {self.neighbor_count!r}, {self.display_char!r})"
        )

    def __str__(self):
        return f"MineSquare showing {self.display_char}"

    def update_char(self, flag=False):
        update_char = None
        if flag:
            update_char = "!"
        else:
            if self.is_mine:
                update_char = "*"
            else:
                update_char = str(self.neighbor_count)

        self.display_char = update_char
