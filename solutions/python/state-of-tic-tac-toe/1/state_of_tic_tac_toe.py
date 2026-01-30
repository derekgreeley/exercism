# state_of_tic_tac_toe.py

def gamestate(board: list[str]) -> str:
    x_count = sum(row.count("X") for row in board)
    o_count = sum(row.count("O") for row in board)

    # Turn-order validity (X starts)
    if o_count > x_count:
        raise ValueError("Wrong turn order: O started")
    if x_count > o_count + 1:
        raise ValueError("Wrong turn order: X went twice")

    # Build all winning lines
    lines = []
    lines.extend(board)  # rows
    lines.extend("".join(board[r][c] for r in range(3)) for c in range(3))  # cols
    lines.append("".join(board[i][i] for i in range(3)))  # main diagonal
    lines.append("".join(board[i][2 - i] for i in range(3)))  # anti diagonal

    x_wins = any(line == "XXX" for line in lines)
    o_wins = any(line == "OOO" for line in lines)

    # Impossible: both winners
    if x_wins and o_wins:
        raise ValueError("Impossible board: game should have ended after the game was won")

    # Winner consistency with move counts
    if x_wins:
        if x_count != o_count + 1:
            raise ValueError("Impossible board: game should have ended after the game was won")
        return "win"

    if o_wins:
        if x_count != o_count:
            raise ValueError("Impossible board: game should have ended after the game was won")
        return "win"

    # No winner
    if x_count + o_count == 9:
        return "draw"
    return "ongoing"