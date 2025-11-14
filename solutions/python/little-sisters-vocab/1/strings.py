def add_prefix_un(word):
    """

    :param word: str of a root word
    :return:  str of root word with un prefix

    This function takes `word` as a parameter and
    returns a new word with an 'un' prefix.
    """
    unword = "un" + word
    return unword


def make_word_groups(vocab_words):
    """

    :param vocab_words: list of vocabulary words with a prefix.
    :return: str of prefix followed by vocabulary words with
             prefix applied, separated by ' :: '.

    This function takes a `vocab_words` list and returns a string
    with the prefix  and the words with prefix applied, separated
     by ' :: '.
    """
    prefix = vocab_words[0]
    word_list = vocab_words[1:]
    new_words = f'{prefix} :: '
    for word in word_list:
        new_words += prefix + word + ' :: '
    return new_words[:-4]


def remove_suffix_ness(word):
    """

    :param word: str of word to remove suffix from.
    :return: str of word with suffix removed & spelling adjusted.

    This function takes in a word and returns the base word with `ness` removed.
    """
    if word[-5:-4] == 'i':
        new_word = word.replace('iness','y')
    else:
        new_word = word.replace('ness','')

    return new_word


def adjective_to_verb(sentence, index):
    """

    :param sentence: str that uses the word in sentence
    :param index:  index of the word to remove and transform
    :return:  str word that changes the extracted adjective to a verb.

    A function takes a `sentence` using the
    vocabulary word, and the `index` of the word once that sentence
    is split apart.  The function should return the extracted
    adjective as a verb.
    """
    sentence_to_list = sentence.split()
    verb_to_change = sentence_to_list[index]

    if verb_to_change[-1:] == '.':
        new_word = verb_to_change[:-1] + 'en'
    else:
        new_word = verb_to_change + 'en'

    return new_word
 
