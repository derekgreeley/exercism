def square_root(number):
    if number < 1:
        raise ValueError("Number must be a positive integer.")

    low, high = 1, number

    while low <= high:
        mid = (low + high) // 2
        mid_squared = mid * mid

        if mid_squared == number:
            return mid
        elif mid_squared < number:
            low = mid +1 
        else:
            high = mid - 1
    return high

    