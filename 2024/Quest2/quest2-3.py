# Solution for Everybody Codes 2024, Quest 2, part 3
# https://everybody.codes/event/2024/quests/2
from time import perf_counter

if __name__ == "__main__":
    start_time = perf_counter()
    data = open(0).read().strip()

    print("\033[1mPart1:\033[22m", "p1")
    print("\033[1mPart2:\033[22m", "p2")

    end_time = perf_counter()
    print(f"\033[2mTime: {end_time - start_time:.4f}s\033[22m")
