def translate(text):
    def translate_word(word):
        vowels = 'aeiou'
        consonant_clusters = ['thr', 'sch', 'sh', 'squ', 'ch', 'qu', 'th', 'wh']
        
        if word.startswith(('xr', 'yt')) or word[0] in vowels:
            return word + 'ay'
        
        for cluster in consonant_clusters:
            if word.startswith(cluster):
                return word[len(cluster):] + cluster + 'ay'
        
        if 'qu' in word:
            idx = word.index('qu')
            return word[idx+2:] + word[:idx+2] + 'ay'
        
        for idx, char in enumerate(word):
            if char in vowels or (char == 'y' and idx != 0):
                return word[idx:] + word[:idx] + 'ay'
        
        return word + 'ay'

    return ' '.join(translate_word(word) for word in text.split())