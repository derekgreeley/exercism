# two_bucket.py

from collections import deque


def measure(bucket_one, bucket_two, goal, start_bucket):
    if goal > max(bucket_one, bucket_two):
        raise ValueError("Goal cannot be larger than both buckets.")
    if start_bucket not in ("one", "two"):
        raise ValueError("Invalid starting bucket.")

    # Forbidden state per exercise rules:
    # after any action, you may not end up with the starting bucket empty
    # and the other bucket full.
    forbidden = (0, bucket_two) if start_bucket == "one" else (bucket_one, 0)

    def neighbors(a, b):
        states = set()

        # Fill either bucket
        states.add((bucket_one, b))
        states.add((a, bucket_two))

        # Empty either bucket
        states.add((0, b))
        states.add((a, 0))

        # Pour bucket one -> bucket two
        transfer = min(a, bucket_two - b)
        states.add((a - transfer, b + transfer))

        # Pour bucket two -> bucket one
        transfer = min(b, bucket_one - a)
        states.add((a + transfer, b - transfer))

        # Remove unchanged states and forbidden state
        states.discard((a, b))
        if forbidden in states:
            states.remove(forbidden)

        return states

    # First move must be filling the chosen starting bucket
    start_state = (bucket_one, 0) if start_bucket == "one" else (0, bucket_two)
    moves = 1

    if start_state[0] == goal:
        return (moves, "one", start_state[1])
    if start_state[1] == goal:
        return (moves, "two", start_state[0])

    queue = deque([(start_state[0], start_state[1], moves)])
    visited = {start_state}

    while queue:
        a, b, steps = queue.popleft()

        for na, nb in neighbors(a, b):
            if (na, nb) in visited:
                continue

            if na == goal:
                return (steps + 1, "one", nb)
            if nb == goal:
                return (steps + 1, "two", na)

            visited.add((na, nb))
            queue.append((na, nb, steps + 1))

    raise ValueError("No solution possible.")