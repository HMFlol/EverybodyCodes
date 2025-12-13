# Solution for Everybody Codes 2024, Quest 2, part 3
# https://everybody.codes/event/2024/quests/2
from time import perf_counter


def count_runes(runes, inscriptions):
    # Build complete set of patterns (runes + reverses)
    patterns = set()

    for rune in runes:
        patterns.add(rune)
        rev_rune = rune[::-1]
        if rev_rune != rune:
            patterns.add(rev_rune)

    symbols = set()
    # Horizontal search with wrap around
    for index, inscription in enumerate(inscriptions):
        for pattern in patterns:
            # Use a while loop with find() instead of a for loop to handle overlapping matches
            start = 0
            # Extend the inscription string to account for wrap around
            extended = inscription + inscription[: len(pattern) - 1]
            while (pos := extended.find(pattern, start)) != -1:
                # pos is the starting position where pattern was found
                # If find() returns -1, pattern wasn't found, so loop ends
                # Add each character position of this pattern match to our symbols set
                for j in range(pos, pos + len(pattern)):
                    # Some modulo math stuff to find the OG position
                    original_pos = j % len(inscription)
                    symbols.add((index, original_pos))
                # Move start position to just after current match to find overlapping patterns
                start = pos + 1
    # Rotate the inscriptions 90 degrees for vertical search
    v_inscriptions = ["".join(col) for col in zip(*inscriptions)]
    # Vertical search using flipped inscriptions
    for v_index, v_inscription in enumerate(v_inscriptions):
        for pattern in patterns:
            start = 0
            while (pos := v_inscription.find(pattern, start)) != -1:
                # v_index is column, pos+i is row
                for i in range(len(pattern)):
                    # Add the tuple backwards to match the OG orientation
                    symbols.add((pos + i, v_index))
                start = pos + 1

    return len(symbols)


if __name__ == "__main__":
    start_time = perf_counter()
    data = open(0).read().strip().splitlines()

    runes = data[0].split(":")[1].split(",")
    inscriptions = data[2:]

    ans = count_runes(runes, inscriptions)

    print("\033[1mAnswer:\033[22m", ans)

    end_time = perf_counter()
    print(f"\033[2mTime: {end_time - start_time:.4f}s\033[22m")
