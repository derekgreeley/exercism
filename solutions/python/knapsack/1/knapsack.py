def maximum_value(maximum_weight, items):
    # dp[w] stores the maximum value for capacity w
    dp = [0] * (maximum_weight + 1)

    for item in items:
        weight = item["weight"]
        value = item["value"]

        # Iterate backwards to prevent using an item more than once
        for capacity in range(maximum_weight, weight - 1, -1):
            dp[capacity] = max(
                dp[capacity],
                dp[capacity - weight] + value
            )

    return dp[maximum_weight]