import math
import random
from copy import deepcopy

from .MineSquare import MineSquare


class MineField:
    def __init__(self, density, size, pre_made_matrix=None):
        self.size = size
        self.density = density
        self.pre_made_matrix = pre_made_matrix

    def __repr__(self):
        return (f"{self.__class__.__name__}("
                f"Size: {self.size!r}, Density: {self.density!r})")

    def __str__(self):
        return f"{self.size}x{self.size} {self.__class__.__name__}"

    def create_board(self):
        if self.pre_made_matrix:
            mines_matrix = self.set_pre_made_matrix()
        else:
            mines_matrix = self.create_mines_matrix()

        neighbors = self.neighbors_matrix(mines_matrix)

        # zip mine value & neighbor value into new 2d list
        #   before assigning to MineSquare class
        square_vals = []
        for n in range(self.size):
            zipped_row = list(zip(mines_matrix[n], neighbors[n]))
            square_vals.append(zipped_row)

        board = deepcopy(square_vals)
        for y, row in enumerate(square_vals):
            for x, val in enumerate(row):
                is_mine, neighbor_count = val
                board[y][x] = MineSquare(is_mine, neighbor_count, (x, y))
        self.board = board

    # pre_made_matrix for testing
    def set_pre_made_matrix(self):
        mines_matrix = self.pre_made_matrix
        self.size = len(self.pre_made_matrix)
        return mines_matrix

    def create_mines_matrix(self):
        mines_matrix = []
        # create a 1D list of bools with mine density
        mine_bools = [
            True if n < self.total_mines else False
            for n in range(self.total_sqrs)
        ]
        random.shuffle(mine_bools)

        # extract equal mine_bools sections into 2d mines_matrix
        for n in range(self.size):
            step = n * self.size
            row = mine_bools[step:step + self.size]
            mines_matrix.append(row)

        return mines_matrix

    def neighbors_matrix(self, mines_matrix):
        neighbors = deepcopy(mines_matrix)

        for x, y in matrix_pos_gen(self.size):
            neighbor_count = 0
            for dx, dy in neighbor_coord_gen():
                if outside_range(self.size, [dx + x, dy + y]):
                    continue
                else:
                    # converting bool -> int is like adding 0 or 1
                    neighbor_count += int(mines_matrix[dy + y][dx + x])

            neighbors[y][x] = neighbor_count

        return neighbors

    def select_square(self, x, y, flag=False):
        square = self.board[y][x]

        if flag:
            square.update_char(flag=True)
            return

        continue_game = self.continue_game(x, y)
        if continue_game:
            self.reveal_neighbors(x, y)

        square.update_char()
        return continue_game

    def continue_game(self, x, y):
        square = self.board[y][x]
        continue_game = True

        if square.is_mine:
            continue_game = False

        return continue_game

    def reveal_neighbors(self, x, y):
        for dx, dy in neighbor_coord_gen():
            if outside_range(self.size, [x + dx, y + dy]):
                continue

            neighbor = self.board[y + dy][x + dx]

            if not neighbor.is_mine and neighbor.display_char == "#":
                neighbor.update_char()
                self.reveal_neighbors(x + dx, y + dy)

    @property
    def total_mines(self):
        return math.ceil(self.density * self.total_sqrs)

    @property
    def total_sqrs(self):
        return self.size**2


def outside_range(size, coords):
    for c in coords:
        if c < 0 or c >= size:
            return True
    return False


def neighbor_coord_gen(dist=1):
    r = range(-dist, dist + 1)
    for dy in r:
        for dx in r:
            if dx == 0 and dy == 0:
                continue
            else:
                yield (dx, dy)


def matrix_pos_gen(r):
    for y in range(r):
        for x in range(r):
            yield (x, y)
