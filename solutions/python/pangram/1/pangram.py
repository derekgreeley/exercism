import string

def is_pangram(sentence):
    alphabet = set(string.ascii_lowercase)
    sentence_set = set(sentence.lower())

    return alphabet.issubset(sentence_set)
