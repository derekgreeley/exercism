
days = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh","eighth", "ninth", "tenth", "eleventh", "twelfth"]
verses =[
    "a Partridge in a Pear Tree",
    "two Turtle Doves",
    "three French Hens",
    "four Calling Birds",
    "five Gold Rings",
    "six Geese-a-Laying",
    "seven Swans-a-Swimming",
    "eight Maids-a-Milking",
    "nine Ladies Dancing",
    "ten Lords-a-Leaping",
    "eleven Pipers Piping",
    "twelve Drummers Drumming"
]


def recite(start_verse, end_verse):
    recites = []
    for i in range (start_verse, end_verse+1):
        end = i
        string = f"On the {days[end-1]} day of Christmas my true love gave to me: "
        tmp = verses[:end]
        tmp.reverse()
        verse = ", ".join(tmp[:-1])
        if (end != 1):
            verse +=", and "
        verse += f"{tmp[-1]}."
        recites.append(string + verse)
    return recites

    