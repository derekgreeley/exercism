import re

from collections import Counter

def count_words(sentence):
    sentence = sentence.lower().replace('_', ' ')
    

    words = re.findall(r"\b\w+(?:'\w+)?\b", sentence)

    return dict(Counter(words))