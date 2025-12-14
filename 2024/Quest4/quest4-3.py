# Solution for Everybody Codes 2024, Quest 4, part 3
# https://everybody.codes/event/2024/quests/4
import statistics
from time import perf_counter

if __name__ == "__main__":
    start_time = perf_counter()
    data = open(0).read().strip().split()

    nums = list(map(int, data))
    # Need to find median, not mean/average for minimizing absolute differences
    median = int(statistics.median(nums))

    ans = sum(abs(n - median) for n in nums)

    print("\033[1mAnswer:\033[22m", ans)

    end_time = perf_counter()
    print(f"\033[2mTime: {end_time - start_time:.4f}s\033[22m")
