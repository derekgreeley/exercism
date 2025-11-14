def rebase(input_base, digits, output_base):
    #validate input base
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    #validate outuput base
    if output_base < 2:
        raise ValueError("output base must be >= 2")

    #validate digits
    if not digits:
        return [0]
    if any(d < 0 or d >= input_base for d in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")


    #remove leading zeroes
    while digits and digits[0] == 0:
        digits = digits[1:]

    if not digits:
        return [0]

    #convert to base 10
    decimal_value = 0 
    for digit in digits:
        decimal_value = decimal_value * input_base + digit 
    
    
    #convert from base 10 to output base
    if decimal_value == 0:
        return [0]

    result = []
    while decimal_value > 0:
        result.append(decimal_value % output_base)
        decimal_value //= output_base

    return result[::-1]