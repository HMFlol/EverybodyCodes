# Solution for Everybody Codes 2024, Quest 2, part 1
# https://everybody.codes/event/2024/quests/2
from time import perf_counter


def count_runes(runes, inscription):
    count = 0

    for rune in runes:
        count += inscription.count(rune)

    return count


if __name__ == "__main__":
    start_time = perf_counter()
    data = open(0).read().strip().splitlines()

    runes = data[0].split(":")[1].split(",")
    inscription = data[2]

    ans = count_runes(runes, inscription)

    print("\033[1mAnswer:\033[22m", ans)

    end_time = perf_counter()
    print(f"\033[2mTime: {end_time - start_time:.4f}s\033[22m")
