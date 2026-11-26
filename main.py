# The Robot Vacuum's Best Excuse — make.fun entry.
# A small machine keeps a straight face: the map is always right,
# and if the map says a corner does not exist, then it does not exist.
# Pure Python standard library, deterministic, no network, no input.

import os

# v2 (revised): shorter, punchier, and the turn lands on the last
# two words — the vacuum blames cartography, not itself. The map
# is still the authority; the homeowner is still wrong.
ENTRY = "That spot isn't on my map, so as far as I'm concerned it doesn't exist. Blame cartography, not me."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
