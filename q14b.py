def parse():
    with open("q14_input.txt", "r") as fh:
        return tuple(tuple(".O#".index(c) for c in line.strip()) for line in fh)

def roll_left(row):
    output = [0] * len(row)
    floor_pos = 0
    for i, x in enumerate(row):
        if x == 1:
            output[floor_pos] = 1
            floor_pos += 1
        elif x == 2:
            output[i] = 2
            floor_pos = i + 1
    return output

def load(col):
    return sum(
        idx
        for idx, x in enumerate(reversed(col), 1)
        if x == 1)

def spincycle(grid):
    grid = list(zip(*(map(roll_left, zip(*grid)))))
    grid = list(map(roll_left, grid))
    grid = list(zip(*map(roll_left, zip(*reversed(grid)))))[::-1]
    grid = [row[::-1] for row in map(roll_left, map(list, map(reversed, grid)))]
    return tuple(map(tuple, grid))

def pprint(grid):
    print("\n".join("".join(".O#"[c] for c in row) for row in grid))
    print()

def main(grid):
    grid = parse()
    seen = {grid: 0}
    for i in range(10 ** 9):
        print(i)
        grid = spincycle(grid)
        if grid in seen:
            clen = i - seen[grid]
            break
        else:
            seen[grid] = i
    i += (10 ** 9 - i) // clen * clen
    print(clen)
    for i in range(i + 1, 10 ** 9):
        grid = spincycle(grid)
    print(sum(map(load, zip(*grid))))

main(parse())
