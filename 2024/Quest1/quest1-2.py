# Solution for Everybody Codes 2024, Quest 1, part 2
# https://everybody.codes/event/2024/quests/1
from time import perf_counter


def potion_master(data):
    # Point values based on x count
    points = {
        0: {"A": 1, "B": 2, "C": 4, "D": 6},
        1: {"A": 0, "B": 1, "C": 3, "D": 5},
    }

    total = 0

    for i in range(0, len(data), 2):
        pair = data[i : i + 2]
        xes = pair.count("x")

        for char in pair:
            if char != "x":
                total += points[xes][char]

    return total


if __name__ == "__main__":
    start_time = perf_counter()
    data = open(0).read().strip()

    ans = potion_master(data)

    print("\033[1mAnswer:\033[22m", ans)

    end_time = perf_counter()
    print(f"\033[2mTime: {end_time - start_time:.4f}s\033[22m")
