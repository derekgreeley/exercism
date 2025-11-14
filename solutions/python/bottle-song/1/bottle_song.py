def recite(start, take=1):
    nums = (
        "no",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
    )

    verses = []

    for i in range(start, start - take, -1):
        current_bottle = nums[i].title() 
        next_bottle = nums[i - 1]  

        bottle_word = "bottle" if i == 1 else "bottles"
        next_bottle_word = "bottle" if i - 1 == 1 else "bottles"

        verses.append(f"{current_bottle} green {bottle_word} hanging on the wall,")
        verses.append(f"{current_bottle} green {bottle_word} hanging on the wall,")
        verses.append("And if one green bottle should accidentally fall,")
        verses.append(
            f"There'll be {next_bottle} green {next_bottle_word} hanging on the wall."
        )

        if i - 1 > start - take:
            verses.append("")

    return verses