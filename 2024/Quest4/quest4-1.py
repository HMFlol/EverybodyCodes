# Solution for Everybody Codes 2024, Quest 4, part 1
# https://everybody.codes/event/2024/quests/4
from time import perf_counter

if __name__ == "__main__":
    start_time = perf_counter()
    data = open(0).read().strip().split()
    # Nums list
    nums = list(map(int, data))
    # Nothing too fancy today
    ans = sum(nums) - len(nums) * min(nums)

    print("\033[1mAnswer:\033[22m", ans)

    end_time = perf_counter()
    print(f"\033[2mTime: {end_time - start_time:.4f}s\033[22m")
