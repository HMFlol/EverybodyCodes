# Solution for Everybody Codes 2024, Quest 5, part 1
# https://everybody.codes/event/2024/quests/5
from collections import deque
from time import perf_counter

if __name__ == "__main__":
    start_time = perf_counter()
    data = [list(map(int, line.split())) for line in open(0) if line.strip()]
    # Transpose rows to columns using zip and convert to deque for efficient pops from left
    columns = [deque(col) for col in list(zip(*data))]
    num_cols = len(columns)
    rounds = 10

    for r in range(1, rounds + 1):
        # Get current and next column indices
        cur_col_idx = (r - 1) % num_cols
        next_col_idx = r % num_cols
        # Pop clapper from front of current column
        clapper = columns[cur_col_idx].popleft()
        # Get target column and its length
        target_col = columns[next_col_idx]
        L = len(target_col)
        # Calculate clapper position, normalizing the value for the up-down cycle
        pos = (clapper - 1) % (2 * L)
        # If pos < L: it's on the way down (index = pos)
        # If pos >= L: it's on the way up (index = 2*L - pos)
        insert_index = pos if pos < L else (2 * L) - pos
        # Insert clapper
        target_col.insert(insert_index, clapper)

    ans = "".join(str(col[0]) for col in columns)

    print("\033[1mAnswer:\033[22m", ans)

    end_time = perf_counter()
    print(f"\033[2mTime: {end_time - start_time:.4f}s\033[22m")
