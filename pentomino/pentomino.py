import string
from copy import deepcopy, copy
from heapq import heappush, heappop
import random
import time
from typing import Iterator, List

PENTO = 5
_ = None

# O to Z
piece_labels = string.ascii_uppercase[-12:]

piece_shape = {
    "O": [["@", "@", "@", "@", "@"]],
    "P": [["@", "@", "@"],
          ["@", "@"]],
    "Q": [["@", "@", "@", "@"],
          ["@"]],
    "R": [["@", "@"],
          [  _, "@", "@"],
          [  _, "@"]],
    "S": [[  _, "@", "@", "@"],
          ["@", "@"]],
    "T": [["@"],
          ["@", "@", "@"],
          ["@"]],
    "U": [["@", "@", "@"],
          ["@",   _, "@"]],
    "V": [["@", "@", "@"],
          ["@"],
          ["@"]],
    "W": [[  _, "@", "@"],
          ["@", "@"],
          ["@"]],
    "X": [[  _, "@"],
          ["@", "@", "@"],
          [  _, "@"]],
    "Y": [["@", "@", "@", "@"],
          [  _, "@"]],
    "Z": [["@", "@"],
          [  _, "@"],
          [  _, "@", "@"]]
}


class MinoPosition:
    def __init__(self, minos):
        self.minos = minos

    def turn_flip(self, factor):
        new_position = []
        for y, x in self.minos:
            if factor == 0:
                ny, nx = y, x
            elif factor == 1:
                ny, nx = x, -y
            elif factor == 2:
                ny, nx = -y, -x
            elif factor == 3:
                ny, nx = -x, y
            elif factor == 4:
                ny, nx = y, -x
            elif factor == 5:
                ny, nx = -x, -y
            elif factor == 6:
                ny, nx = -y, x
            elif factor == 7:
                ny, nx = x, y
            new_position.append((ny, nx))
        new_position.sort()
        self.minos = new_position

    def move(self, basecell, y, x):
        y0, x0 = self.minos[basecell]
        self.minos = [(cy - y0 + y, cx - x0 + x) for cy, cx in self.minos]

    def __repr__(self):
        return f"MinoPosition({repr(self.minos)})"

    def __iter__(self):
        return iter(self.minos)


class Board:
    def __init__(self, ny, nx):
        self.cells = [[None] * nx for _ in range(ny)]
        self.put_history = []

    def span(self):
        ny = len(self.cells)
        nx = len(self.cells[0])
        return (ny, nx)

    def is_empty_at(self, y, x):
        ny, nx = self.span()
        return 0 <= y < ny and 0 <= x < nx and self.cells[y][x] is None

    def can_accept(self, minos: MinoPosition) -> bool:
        return all(self.is_empty_at(y, x) for y, x in minos)

    def put(self, position: MinoPosition, k: str):
        for y, x in position:
            self.cells[y][x] = k
        self.put_history.append(k)

    def print(self):
        for row in self.cells:
            plain_string = " ".join(c if c else "." for c in row)
            print(color_string(plain_string))


def color_string(plain_string):
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    LIGHT_RED = '\033[91m'
    LIGHT_GREEN = '\033[92m'
    LIGHT_YELLOW = '\033[93m'
    LIGHT_BLUE = '\033[94m'
    LIGHT_MAGENTA = '\033[95m'
    LIGHT_CYAN = '\033[96m'
    RESET = '\033[0m'
    color_map = {
        'O': RED,
        'P': GREEN,
        'Q': YELLOW,
        'R': BLUE,
        'S': MAGENTA,
        'T': CYAN,
        'U': LIGHT_RED,
        'V': LIGHT_GREEN,
        'W': LIGHT_YELLOW,
        'X': LIGHT_BLUE,
        'Y': LIGHT_MAGENTA,
        'Z': LIGHT_CYAN
    }
    colored_string = []
    for c in plain_string:
        if c in color_map:
            code = color_map[c]
            colored_string.extend([code, c, RESET])
            continue
        colored_string .append(c)
    return ''.join(colored_string)


class Piece:
    def __init__(self, label):
        self.label = label
        shape = piece_shape[label]
        minos = []
        for y, row in enumerate(shape):
            for x, blk in enumerate(row):
                if blk:
                    minos.append((y, x))
        self.minos = minos

    def __eq__(self, other):
        return self.label == other.label

    def __str__(self):
        return self.label

    def __hash__(self):
        return hash(self.label)

    def possible_positions(self, y, x, board: Board) -> Iterator[MinoPosition]:
        # randomize piece direction
        turn_factors = [i for i in range(0, 8)]
        random.shuffle(turn_factors)

        done = set()
        for factor in turn_factors:
            for center_cell in range(0, PENTO):
                position = MinoPosition(self.minos)
                position.turn_flip(factor)
                position.move(center_cell, y, x)

                # for deduplicating symmetry
                key = tuple(position.minos)
                if key in done:
                    continue
                done.add(key)

                if board.can_accept(position):
                    yield position


pieces = [Piece(s) for s in piece_labels]


class NoAnswer(Exception):
    pass


class FitStatistics:
    def __init__(self, pieces: List[Piece]):
        # start from 1 to avoid zero-division error
        self.trial = {p: 1 for p in pieces}
        self.fit = {p: 1 for p in pieces}

    def countup_trial(self, piece: Piece):
        self.trial[piece] += 1

    def countup_fit(self, piece: Piece):
        self.fit[piece] += 1

    def fit_rate(self, piece: Piece):
        return self.fit[piece] / self.trial[piece]

    def list_fit_rate(self):
        rate_list = [(p, self.fit_rate(p)) for p in pieces]
        rate_list.sort(key=lambda t: t[1])
        return rate_list

    def mean_fit_rate(self):
        return sum(self.fit.values()) / sum(self.trial.values())


class SearchStatistics:
    def __init__(self):
        self.reached_depth_count = {i: 0 for i in range(1, len(pieces))}

    def countup(self, reached_depth: int):
        self.reached_depth_count[reached_depth] += 1

    def total_trial(self):
        return sum(self.reached_depth_count.values())

    def mean_reached_depth(self):
        dc = self.reached_depth_count
        return sum(d * c for d, c in dc.items()) / sum(dc.values())

    def reach_distribution(self):
        reachd = [
            (d, c / self.total_trial()) for d, c in self.reached_depth_count.items()
        ]
        reachd.sort()
        return reachd


fit_statistics = FitStatistics(pieces)
search_statistics = SearchStatistics()

# Strategies of piece choice for the next fit trial


class FitDifficultPieceChoice:
    """A: Try from fit-diffucult piece"""

    def pop(self, pieces):
        global fit_statistics
        pieces.sort(key=fit_statistics.fit_rate, reverse=True)
        return pieces.pop()


class FitEasyPieceChoice:
    """B: Try from fit-easy piece"""

    def pop(self, pieces):
        global fit_statistics
        pieces.sort(key=fit_statistics.fit_rate, reverse=False)
        return pieces.pop()


class RandomPieceChoice:
    """C: Try randomly"""

    def pop(self, pieces):
        random.shuffle(pieces)
        return pieces.pop()


piece_choice_strategy = FitDifficultPieceChoice()
# piece_choice_strategy = FitEasyPieceChoice()
# piece_choice_strategy = RandomPieceChoice()


def prioritize(open_edges, y, x, yspan, xspan):
    """Return priority value. Smaller value has higher priority."""
    ran = random.randrange(9999)
    # 1: short spanwise scan
    # return (y, x) if xspan < yspan else (x, y)

    # 2: open edges
    # return (open_edges, ran)

    # 3: open edges + short spanwise scan
    return (open_edges, y, x) if xspan < yspan else (open_edges, x, y)

    # 4: open edges + distance from two wall
    # return (open_edges, min(y, yspan - y) + min(x, xspan - x), ran)

    # 5: open edges + distance from nearest wall
    # return (open_edges, min(y, yspan - y, x, xspan - x), ran)


def backtrack(cell_queue, remaining_pieces, board: Board):
    global search_trial

    while cell_queue:
        _, y, x = heappop(cell_queue)

        # find the next empty cell
        if not board.is_empty_at(y, x):
            continue

        pieces_not_tried = copy(remaining_pieces)

        # try all pieces and positions
        while pieces_not_tried:

            piece = piece_choice_strategy.pop(pieces_not_tried)
            fit_statistics.countup_trial(piece)

            for piece_position in piece.possible_positions(y, x, board):

                # get fit-difficulty statistics
                fit_statistics.countup_fit(piece)

                board2 = deepcopy(board)
                board2.put(piece_position, piece.label)

                remaining_pieces2 = copy(remaining_pieces)
                remaining_pieces2.remove(piece)

                cell_queue2 = copy(cell_queue)
                four = ((-1, 0), (1, 0), (0, -1), (0, 1))

                # find neighbor cells beside the piece
                neighbors = {
                    (y1 + y2, x1 + x2)
                    for y1, x1 in four
                    for y2, x2 in piece_position
                    if board2.is_empty_at(y1 + y2, x1 + x2)
                }

                for nby, nbx in neighbors:
                    parameters = {
                        "open_edges": sum(
                            board2.is_empty_at(nby + y1, nbx + x1) for y1, x1 in four
                        ),
                        "y": y,
                        "x": x,
                        "yspan": board2.span()[0],
                        "xspan": board2.span()[1],
                    }
                    priority = prioritize(**parameters)
                    heappush(cell_queue2, (priority, nby, nbx))

                try:
                    return backtrack(cell_queue2, remaining_pieces2, board2)
                except NoAnswer:
                    continue

        search_statistics.countup(len(board.put_history))
        board.cells[y][x] = "+"

        # print progress
        if search_statistics.total_trial() % 1000 == 0:
            print(
                "#search trial:",
                search_statistics.total_trial(),
                ":",
                "".join(board.put_history),
            )
            board.print()
            print()

        raise NoAnswer()

    return board


YSPAN = 6
XSPAN = 10

if __name__ == "__main__":
    board = Board(YSPAN, XSPAN)
    # for y, x in [(3,3), (3,4), (4,3), (4,4)]:
    #    board.cells[y][x] = "#"
    board.print()
    random.shuffle(pieces)

    start_time_ns = time.time_ns()

    cell_queue = [(0, 0, 0)]  # (open edge, y, x)
    answer = backtrack(cell_queue, pieces, board)

    end_time_ns = time.time_ns()

    print("#fit rate")
    for piece, rate in fit_statistics.list_fit_rate():
        print(f"{piece}: {rate:.3f}")

    print("\n#reach distribution")
    for depth, rate in search_statistics.reach_distribution():
        print(f"{depth:2d}: {rate:.4f}")

    print()
    elapsed = (end_time_ns - start_time_ns) / 10**9
    print(f"elapsed time [s]: {elapsed:.2f}")
    print("total search trial:", search_statistics.total_trial())
    fit_rate = fit_statistics.mean_fit_rate()
    print(f"mean fit rate: {fit_rate:.2f}")
    depth = search_statistics.mean_reached_depth()
    print(f"mean reached depth: {depth:.2f}")
    print()
    answer.print()
