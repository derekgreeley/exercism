def steps(number):
    """Returns the number of steps to reach 1 following the Collatz Conjecture."""
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    
    steps = 0
    while number != 1:
        if number % 2 == 0:
            number //= 2  # Even: divide by 2
        else:
            number = 3 * number + 1  # Odd: multiply by 3 and add 1
        steps += 1  # Count each step

    return steps
