import random
from dataclasses import dataclass
from typing import Set, Tuple

Cell = Tuple[int, int]

@dataclass
class Minesweeper:
    height: int
    width: int
    bombs: Set[Cell]

    @classmethod
    def random(cls, height: int, width: int, bombs_count: int):
        cells = [(i, j) for i in range(height) for j in range(width)]
        bombs = set(random.sample(cells, bombs_count))
        return cls(height, width, bombs)

    def neighbors(self, cell: Cell) -> Set[Cell]:
        (r, c) = cell
        neigh = set()
        for i in range(r-1, r+2):
            for j in range(c-1, c+2):
                if (i, j) == cell:
                    continue
                if 0 <= i < self.height and 0 <= j < self.width:
                    neigh.add((i, j))
        return neigh

    def nearby_bombs(self, cell: Cell) -> int:
        return sum((n in self.bombs) for n in self.neighbors(cell))


def play(height=5, width=5, bombs=5):
    board = Minesweeper.random(height, width, bombs)
    revealed: Set[Cell] = set()

    while True:
        # Print board
        for i in range(height):
            row = []
            for j in range(width):
                if (i, j) in revealed:
                    if (i, j) in board.bombs:
                        row.append('*')
                    else:
                        row.append(str(board.nearby_bombs((i, j))))
                else:
                    row.append('_')
            print(' '.join(row))
        print()

        # Ask user for a move
        raw = input('Enter row,col (or q to quit): ')
        if raw.strip().lower() == 'q':
            break
        try:
            r, c = map(int, raw.split(','))
        except Exception:
            print('Invalid input')
            continue
        if not (0 <= r < height and 0 <= c < width):
            print('Out of range')
            continue
        if (r, c) in board.bombs:
            print('BOOM! You hit a bomb.')
            break
        revealed.add((r, c))
        if len(revealed) == height * width - bombs:
            print('Congratulations, you cleared the board!')
            break

if __name__ == '__main__':
    play()
