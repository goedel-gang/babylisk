__import__("sys").setrecursionlimit(99999) or (
    lambda DIRS, EFFECTS, grid: (
        lambda m, n: (
            lambda dfs:
                print(max(map(
                    dfs, (
                        [x
                        for i in range(m)
                        for x in [(i, 0, 0), (i, n - 1, 2)]
                        ] +
                        [x
                        for j in range(n)
                        for x in [(0, j, 3), (m - 1, j, 1)]]
                    ))))
            )(dfs=
            lambda start: (
                lambda seen, _dfs_ptr: (
                    lambda _dfs:
                        [_dfs_ptr.__setitem__(0, _dfs),
                        _dfs(*start),
                        len({(i, j) for i, j, _ in seen})][-1]
                    )(_dfs=
                        lambda i, j, d: (i, j, d) in seen or
                            [seen.add((i, j, d)),
                            [0 <= i + DIRS[nd][0] < m
                                and 0 <= j + DIRS[nd][1] < n
                                and _dfs_ptr[0](i + DIRS[nd][0], j + DIRS[nd][1], nd)
                            for nd in EFFECTS[grid[i][j]][d]]
                            ]
                    )
            )(seen=set(), _dfs_ptr=[None]))
        )(m=len(grid), n=len(grid[0]))
)(
DIRS = [
    (0, 1),
    (-1, 0),
    (0, -1),
    (1, 0)],
EFFECTS = {
    ".": {0: [0], 1: [1], 2: [2], 3: [3]},
    "/": {0: [1], 1: [0], 2: [3], 3: [2]},
   "\\": {0: [3], 1: [2], 2: [1], 3: [0]},
    "|": {0: [1, 3], 1: [1], 2: [1, 3], 3: [3]},
    "-": {0: [0], 1: [0, 2], 2: [2], 3: [0, 2]},
},
grid = list(map(str.strip, open("q16_input.txt", "r"))),)
