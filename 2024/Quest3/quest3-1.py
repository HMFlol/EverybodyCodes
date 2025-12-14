# Solution for Everybody Codes 2024, Quest 3, part 1
# https://everybody.codes/event/2024/quests/3
from time import perf_counter

"""def print_grid(grid_dict):
    if not grid_dict:
        return

    # Find dimensions
    max_row = int(max(pos.imag for pos in grid_dict))
    max_col = int(max(pos.real for pos in grid_dict))

    # Print row by row
    for row in range(max_row + 1):
        line = ""
        for col in range(max_col + 1):
            line += grid_dict.get(col + row * 1j, " ")
        print(line)
    print()"""  # Empty line after grid


def bae_caught_me_slopin(grid, directions):
    ans = 0
    # Convert all # to 1 initially
    for pos in grid:
        if grid[pos] == "#":
            grid[pos] = "1"
            ans += 1

    # Increment levels until no more can be done
    changed = True
    cur_level = 1

    while changed:
        changed = False
        next_level = cur_level + 1

        for pos in grid:
            if grid[pos] == str(cur_level):
                neighbours = [grid.get(pos + d) for d in directions]
                # Check if all neighbors are either '#' or '.'
                if all(n.isdigit() and int(n) >= cur_level for n in neighbours if n is not None):
                    grid[pos] = str(next_level)
                    changed = True
                    ans += 1

        cur_level += 1

    return ans


if __name__ == "__main__":
    start_time = perf_counter()
    data = open(0).read().strip().splitlines()

    grid = {col + row * 1j: char for row, line in enumerate(data) for col, char in enumerate(line)}
    # Directions: 1 = right, -1 = left, 1j = down, -1j = up
    directions = [1, -1, 1j, -1j]

    ans = bae_caught_me_slopin(grid, directions)

    print("\033[1mAnswer:\033[22m", ans)

    end_time = perf_counter()
    print(f"\033[2mTime: {end_time - start_time:.4f}s\033[22m")
