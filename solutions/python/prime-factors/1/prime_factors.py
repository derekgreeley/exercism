def factors(value: int) ->list[int]:
    result = []
    divisor = 2

    while value > 1:
        while value % divisor == 0:
            result.append(divisor)
            value//= divisor
        divisor += 1


        if divisor * divisor > value:
            if value > 1:
                result.append(value)
            break

    return result
    