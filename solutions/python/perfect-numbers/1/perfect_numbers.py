def classify(number):
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    
    aliquot_sum = sum(i for i in range (1, number) if number % i == 0)

    if aliquot_sum == number:
        return 'perfect'
    elif aliquot_sum > number:
        return 'abundant'
    else:
        return 'deficient'