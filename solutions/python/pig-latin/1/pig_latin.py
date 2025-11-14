import re
import string

VOWELS = set('aeiouy')
CONSONANTS = set(string.ascii_lowercase).difference(VOWELS)

def translate(text):
    """Functions that translate a given text to 'Pig Latin'.
    :param text: str - String that will be translated.
    :return: str - String with the translated text.
    This functions returns a string translated to 'Pig Latin' according to the rules of the language.
    """
    pig_latin = []
    # Loops through the words in the string
    for word in text.split(' '):
        reordered_word = []
        # Checks for constants except 'xr' and 'yt'
        if set(word[0]).issubset(CONSONANTS) and word[:2] != 'xr' and word[:2] != 'yt' or word[:2] == 'ye':
            # Checks for 'h' sounds
            if re.match(r'\b[a-z]*h[a-z]+', word):
                if set(re.findall(r'(?<=h).*', word)[0][0]).issubset(CONSONANTS):
                    reordered_word.append(re.findall(r'(?<=h).*', word)[0][1:])
                    reordered_word.append(re.findall(r'[a-z]*h', word[:3])[0])
                    reordered_word.append(re.findall(r'(?<=h).*', word)[0][:1])
                else:
                    reordered_word.append(re.findall(r'(?<=h).*', word)[0])
                    reordered_word.append(re.findall(r'[a-z]*h', word[:3])[0])
            # Checks for 'qu' sounds
            elif re.match(r'\b[a-z]*qu[a-z]+', word):
                reordered_word.append(re.findall(r'(?<=qu).*', word)[0])
                reordered_word.append(re.findall(r'[a-z]*qu', word)[0])
            # Check for any other starting consonant word
            else:
                reordered_word.append(word[1:])
                reordered_word.append(word[:1])
        # Checks for vowels
        else:
            reordered_word.append(word)
        # Adds the suffix 'ay' and appends the joined word
        reordered_word.append('ay')
        pig_latin.append(''.join(reordered_word))
    # Returns the string
    return ' '.join(pig_latin)