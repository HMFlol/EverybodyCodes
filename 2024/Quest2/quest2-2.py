# Solution for Everybody Codes 2024, Quest 2, part 2
# https://everybody.codes/event/2024/quests/2
from time import perf_counter

if __name__ == "__main__":
    start_time = perf_counter()
    data = open(0).read().strip().splitlines()

    runes = data[0].split(":")[1].split(",")
    inscriptions = data[2:]

    # Build complete set of patterns (runes + reverses)
    patterns = set()

    for rune in runes:
        patterns.add(rune)
        rev_rune = rune[::-1]
        if rev_rune != rune:
            patterns.add(rev_rune)

    symbols = set()
    # Search all patterns in all inscriptions
    for index, inscription in enumerate(inscriptions):
        for pattern in patterns:
            # Use a while loop with find() instead of a for loop to handle overlapping matches
            start = 0
            while (pos := inscription.find(pattern, start)) != -1:
                # pos is the starting position where pattern was found
                # If find() returns -1, pattern wasn't found, so loop ends
                # Add each character position of this pattern match to our symbols set
                for j in range(pos, pos + len(pattern)):
                    symbols.add((index, j))
                # Move start position to just after current match to find overlapping patterns
                start = pos + 1

    p1 = len(symbols)

    print("\033[1mPart1:\033[22m", p1)
    print("\033[1mPart2:\033[22m", "p2")

    end_time = perf_counter()
    print(f"\033[2mTime: {end_time - start_time:.4f}s\033[22m")
