from typing import List
import random

def generate_magic_square(n: int) -> List[List[int]]:
    square = [[None] * n for _ in range(n)]
    # search from cells with many constraints
    cells = (
            [(n//2, n//2)] +
            [(i, i) for i in range(n) if i != n//2] +
            [(i, n-1-i) for i in range(n) if i != n//2] +
            [(i, j) for i in range(n) for j in range(n) if i != j and i != n-1-j]
    )
    row_column_diagonal = (
        [[(i, i) for i in range(n)]] +
        [[(i, n-1-i) for i in range(n)]] +
        [[(i, j) for i in range(n)] for j in range(n)] +
        [[(i, j) for j in range(n)] for i in range(n)]
    )
    used = set()

    def summation(series):
        s = 0
        for i, j in series:
            val = square[i][j]
            if val is None:
                return None
            s += val
        return s

    def backtrack(pointer, magic_constant):
        if pointer == len(cells):
            return True
        i, j = cells[pointer]

        values = [i for i in range(1, n*n + 1)]
        random.shuffle(values)
        for val in values:
            if val in used:
                continue
            used.add(val)
            square[i][j] = val

            const = magic_constant
            for series in row_column_diagonal:
                s = summation(series)
                if s is None:
                    continue
                if const is None:
                    const = s
                    continue
                if s != const:
                    break
            else:
                result = backtrack(pointer + 1, const)
                if result is True:
                    return True
            used.remove(val)

        square[i][j] = None
        return False

    result = backtrack(0, None)
    if result:
        return square
    raise Exception("no ansewer")

ms = generate_magic_square(3)
for row in ms:
    print(row)
