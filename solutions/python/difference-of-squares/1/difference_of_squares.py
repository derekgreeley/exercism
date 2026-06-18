def square_of_sum(n):
    # Formula: (n(n+1)/2)^2
    return (n * (n + 1) // 2) ** 2


def sum_of_squares(n):
    # Formula: n(n+1)(2n+1)/6
    return n * (n + 1) * (2 * n + 1) // 6


def difference_of_squares(n):
    return square_of_sum(n) - sum_of_squares(n)