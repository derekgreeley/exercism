def is_isogram(string):
    cleaned = string.lower().replace (" ","").replace("-","")
    return len(set(cleaned)) == len(cleaned)

    