def find_fewest_coins(coins: list[int], target: int) -> list[int]:
    """
    Return a multiset (list) of coins that sums to `target` with the fewest coins.
    Raises:
      - ValueError("target can't be negative") if target < 0
      - ValueError("can't make target with given coins") if no combination exists
    """
    if target < 0:
        raise ValueError("target can't be negative")
    if target == 0:
        return []

    # Clean up coin list: positive, unique, sorted
    coins = sorted(set(c for c in coins if c > 0))

    # Quick impossibility check
    if not coins or coins[0] > target:
        raise ValueError("can't make target with given coins")

    INF = float("inf")
    dp = [INF] * (target + 1)          # dp[a] = min coins to reach amount a
    choice = [-1] * (target + 1)       # choice[a] = coin chosen last to reach a
    dp[0] = 0

    for a in range(1, target + 1):
        for c in coins:
            if c > a:
                break
            if dp[a - c] + 1 < dp[a]:
                dp[a] = dp[a - c] + 1
                choice[a] = c

    if dp[target] == INF:
        raise ValueError("can't make target with given coins")

    # Reconstruct solution
    res = []
    a = target
    while a > 0:
        c = choice[a]
        # Safety check (shouldn't happen if dp[target] != INF)
        if c == -1:
            raise ValueError("can't make target with given coins")
        res.append(c)
        a -= c

    # Tests expect coins in ascending order
    res.sort()
    return res
