# Solution for Everybody Codes 2024, Quest 1, part 1
# https://everybody.codes/event/2024/quests/1
from time import perf_counter

if __name__ == "__main__":
    start_time = perf_counter()
    data = open(0).read().strip()

    points = {"A": 0, "B": 1, "C": 3, "D": 5}

    p1 = 0

    for char in data:
        p1 += points[char]

    print("\033[1mPart1:\033[22m", p1)
    print("\033[1mPart2:\033[22m", "p2")

    end_time = perf_counter()
    print(f"\033[2mTime: {end_time - start_time:.4f}s\033[22m")
