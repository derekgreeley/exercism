def tally(results: list[str]) -> list[str]:
    from collections import defaultdict

    # Initialize the scoreboard
    scoreboard = defaultdict(lambda: {"MP": 0, "W": 0, "D": 0, "L": 0, "P": 0})

    # Parse each match result
    for result in results:
        if not result.strip():
            continue  # skip empty lines

        team1, team2, outcome = result.split(";")

        # Update match played
        scoreboard[team1]["MP"] += 1
        scoreboard[team2]["MP"] += 1

        # Apply outcome logic
        if outcome == "win":
            scoreboard[team1]["W"] += 1
            scoreboard[team1]["P"] += 3
            scoreboard[team2]["L"] += 1
        elif outcome == "loss":
            scoreboard[team2]["W"] += 1
            scoreboard[team2]["P"] += 3
            scoreboard[team1]["L"] += 1
        elif outcome == "draw":
            scoreboard[team1]["D"] += 1
            scoreboard[team2]["D"] += 1
            scoreboard[team1]["P"] += 1
            scoreboard[team2]["P"] += 1

    # Sort teams: first by points descending, then name ascending
    sorted_teams = sorted(scoreboard.items(), key=lambda x: (-x[1]["P"], x[0]))

    # Format the table
    header = "Team                           | MP |  W |  D |  L |  P"
    lines = [header]
    for team, stats in sorted_teams:
        line = f"{team:<31}| {stats['MP']:>2} | {stats['W']:>2} | {stats['D']:>2} | {stats['L']:>2} | {stats['P']:>2}"
        lines.append(line)

    return lines