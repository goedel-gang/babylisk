(
    lambda roll_left, load, spincycle, grid: (
        lambda seen, clen, final_i:
            [
             all(
                 [grid.__setitem__(0, spincycle(grid, roll_left)),
                  (grid[0] not in seen
                   and [seen.__setitem__(grid[0], i), True][-1])
                  or
                  (grid[0] in seen
                   and [final_i.__setitem__(0, i),
                        clen.__setitem__(0, i - seen[grid[0]]), False][-1])
                  ][-1]
                 for i in range(10 ** 9)),
             final_i.__setitem__(0,
                 final_i[0] + (10 ** 9 - final_i[0]) // clen[0] * clen[0]),
             [grid.__setitem__(0, spincycle(grid, roll_left))
              for i in range(final_i[0] + 1, 10 ** 9)],
             print(sum(map(load, zip(*grid[0]))))]
    )(seen={grid[0]: 0}, clen=[None], final_i=[None])
)(
grid = [
    tuple(tuple(".O#".index(c) for c in line.strip())
    for line in open("q14_input.txt"))],
roll_left = (
    lambda row: (
        lambda output, floor_pos:
            [[
                [output.__setitem__(floor_pos[0], 1),
                 floor_pos.__setitem__(0, floor_pos[0] + 1)]
                if x == 1 else
                [output.__setitem__(i, 2),
                 floor_pos.__setitem__(0, i + 1)]
                if x == 2 else ...
                for i, x in enumerate(row)
            ], output][-1]
    )(output=[0] * len(row), floor_pos=[0])
),
load = (
    lambda col:
        sum(
            idx
            for idx, x in enumerate(reversed(col), 1)
            if x == 1)
),
spincycle = (
    lambda grid, roll_left:
        [grid.__setitem__(
            0, list(zip(*(map(roll_left, zip(*grid[0])))))),
         grid.__setitem__(
            0, list(map(roll_left, grid[0]))),
         grid.__setitem__(
            0, list(zip(*map(roll_left, zip(*reversed(grid[0])))))[::-1]),
         grid.__setitem__(
            0,
            [row[::-1]
             for row in map(roll_left, map(list, map(reversed, grid[0])))]),
         tuple(map(tuple, grid[0]))][-1]
))
