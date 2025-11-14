def recite(start_verse: int, end_verse: int) -> list[str]:
    
    """Return verses from 'This is the House that Jack Built' between given range."""

    parts = [
        ("the house that Jack built.", ""),
        ("the malt", "that lay in"),
        ("the rat", "that ate"),
        ("the cat", "that killed"),
        ("the dog", "that worried"),
        ("the cow with the crumpled horn", "that tossed"),
        ("the maiden all forlorn", "that milked"),
        ("the man all tattered and torn", "that kissed"),
        ("the priest all shaven and shorn", "that married"),
        ("the rooster that crowed in the morn", "that woke"),
        ("the farmer sowing his corn", "that kept"),
        ("the horse and the hound and the horn", "that belonged to"),
    ]

    verses = []
    for verse_num in range(start_verse, end_verse + 1):
        lines = ["This is " + parts[verse_num - 1][0]]
        for prev in range(verse_num - 1, 0, -1):
            lines.append(f"{parts[prev][1]} {parts[prev -1][0]}")
        verses.append(" ".join(lines))
    return verses

