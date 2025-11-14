def find_anagrams(word, candidates):
    target = word.lower()
    sorted_target = sorted(target)

    result = []

    for word in candidates:
        word_lower = word.lower()
        if word_lower != target and sorted(word_lower) == sorted_target:
            result.append(word)

    return result
    
    
