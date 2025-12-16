# Solution for Everybody Codes 2024, Quest 5, part 2
# https://everybody.codes/event/2024/quests/5
from collections import defaultdict, deque
from time import perf_counter


def let_it_all_out(columns):
    num_cols = len(columns)
    seen = defaultdict(int)
    round_num = 0

    while True:
        round_num += 1
        # Get current and next column indices
        cur_col_idx = (round_num - 1) % num_cols
        next_col_idx = round_num % num_cols
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
        # Form the number from top of columns
        shouted = int("".join(str(col[0]) for col in columns))
        # Track how many times we've seen this number
        seen[shouted] += 1

        if seen[shouted] == 2024:
            return shouted * round_num


if __name__ == "__main__":
    start_time = perf_counter()
    data = [list(map(int, line.split())) for line in open(0) if line.strip()]
    columns = [deque(col) for col in zip(*data)]

    ans = let_it_all_out(columns)

    print("\033[1mAnswer:\033[22m", ans)

    end_time = perf_counter()
    print(f"\033[2mTime: {end_time - start_time:.4f}s\033[22m")
