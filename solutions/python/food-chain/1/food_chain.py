def recite(start_verse: int, end_verse: int) -> list[str]:
    animals = [
        "fly",
        "spider",
        "bird",
        "cat",
        "dog",
        "goat",
        "cow",
        "horse",
    ]

    reactions = {
        "spider": "It wriggled and jiggled and tickled inside her.",
        "bird": "How absurd to swallow a bird!",
        "cat": "Imagine that, to swallow a cat!",
        "dog": "What a hog, to swallow a dog!",
        "goat": "Just opened her throat and swallowed a goat!",
        "cow": "I don't know how she swallowed a cow!",
        "horse": "She's dead, of course!",
    }

    def verse(n: int) -> list[str]:
        lines = [f"I know an old lady who swallowed a {animals[n]}."]
        animal = animals[n]

        # Add special line if available
        if animal in reactions:
            lines.append(reactions[animal])

        if animal == "horse":
            return lines

        # Build the cumulative "swallowed X to catch Y" lines
        for i in range(n, 0, -1):
            predator = animals[i]
            prey = animals[i - 1]
            if predator == "bird" and prey == "spider":
                prey = "spider that wriggled and jiggled and tickled inside her"
            lines.append(f"She swallowed the {predator} to catch the {prey}.")

        lines.append("I don't know why she swallowed the fly. Perhaps she'll die.")
        return lines

    result = []
    for i in range(start_verse - 1, end_verse):
        result.extend(verse(i))
        if i != end_verse - 1:
            result.append("")

    return result
