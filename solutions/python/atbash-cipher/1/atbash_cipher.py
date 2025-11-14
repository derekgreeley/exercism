def atbash_char(c):
    if c.isalpha():
        return chr(ord('z') - (ord(c) - ord('a')))
    return c

def encode(plain_text):
    plain_text = plain_text.lower()
    encoded = []
    count = 0

    for char in plain_text:
        if char.isalnum():
            encoded.append(atbash_char(char))
            count += 1
            if count % 5 == 0:
                encoded.append(' ')

    return ''.join(encoded).rstrip()

def decode(ciphered_text):
    ciphered_text = ciphered_text.lower().replace(' ', '')
    return ''.join(atbash_char(c) for c in ciphered_text)