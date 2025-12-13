# Solution for Everybody Codes 2024, Quest 1, part 1
# https://everybody.codes/event/2024/quests/1
from time import perf_counter


def potion_master(data):
    points = {"A": 0, "B": 1, "C": 3}

    total = 0

    for char in data:
        total += points[char]

    return total


if __name__ == "__main__":
    start_time = perf_counter()
    data = open(0).read().strip()

    ans = potion_master(data)

    print("\033[1mAnswer:\033[22m", ans)

    end_time = perf_counter()
    print(f"\033[2mTime: {end_time - start_time:.4f}s\033[22m")
