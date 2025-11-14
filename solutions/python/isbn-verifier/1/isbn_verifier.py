def is_valid(isbn):
 # Remove any hyphens from the ISBN
    isbn = isbn.replace("-", "")
    
    # ISBN-10 must have exactly 10 characters
    if len(isbn) != 10:
        return False
    
    # Validate all characters except the last one are digits
    if not (isbn[:-1].isdigit() and (isbn[-1].isdigit() or isbn[-1] == 'X')):
        return False
    
    # Compute the ISBN-10 checksum
    total = 0
    for i in range(9):
        total += int(isbn[i]) * (i + 1)
    
    # Handle last character separately (X represents 10)
    last_digit = 10 if isbn[-1] == 'X' else int(isbn[-1])
    total += last_digit * 10

    # Check validity (must be divisible by 11)
    return total % 11 == 0