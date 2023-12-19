# directions in anticlockwise order
DIRS = [
    (0, 1),
    (-1, 0),
    (0, -1),
    (1, 0)]

# what happens to your direction when you enter a tile
EFFECTS = {
    ".": {0: [0], 1: [1], 2: [2], 3: [3]},
    "/": {0: [1], 1: [0], 2: [3], 3: [2]},
   "\\": {0: [3], 1: [2], 2: [1], 3: [0]},
    "|": {0: [1, 3], 1: [1], 2: [1, 3], 3: [3]},
    "-": {0: [0], 1: [0, 2], 2: [2], 3: [0, 2]},
}

def parse():
    with open("q16_input.txt", "r") as fh:
        grid = list(map(str.strip, fh))
    return grid, len(grid), len(grid[0])

# state is (position, direction), direction being an index in DIRS.
def dfs(grid, m, n, start):
    to_visit = [start]
    seen = set(to_visit)
    while to_visit:
        i, j, prev_d = to_visit.pop()
        for d in EFFECTS[grid[i][j]][prev_d]:
            di, dj = DIRS[d]
            if 0 <= i + di < m and 0 <= j + dj < n:
                if (i + di, j + dj, d) not in seen:
                    seen.add((i + di, j + dj, d))
                    to_visit.append((i + di, j + dj, d))
    return len({(i, j) for i, j, _ in seen})

# generate edge-of-the-board starting states
def starts(m, n):
    for i in range(m):
        yield (i, 0, 0)
        yield (i, n - 1, 2)
    for j in range(n):
        yield (0, j, 3)
        yield (m - 1, j, 1)

# run in parallel. This is faster with CPython on my machine.
from multiprocessing import Pool
from functools import partial
grid, m, n = parse()
with Pool(8) as p:
    print(max(p.map(
        partial(dfs, grid, m, n), starts(m, n))))
