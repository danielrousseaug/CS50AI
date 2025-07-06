"""Tic Tac Toe game with minimax AI."""

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """Start with an empty 3x3 board."""
    return [[EMPTY, EMPTY, EMPTY] for _ in range(3)]


def player(board):
    """Return player who has the next turn."""
    flat = [cell for row in board for cell in row]
    if flat.count(X) <= flat.count(O):
        return X
    else:
        return O


def actions(board):
    """Return all available actions as (i, j) tuples."""
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] is EMPTY}


def result(board, action):
    i, j = action
    if board[i][j] is not EMPTY:
        raise ValueError("Invalid move")
    new_board = [row[:] for row in board]
    new_board[i][j] = player(board)
    return new_board


def winner(board):
    lines = []
    lines.extend(board)
    lines.extend([[board[i][j] for i in range(3)] for j in range(3)])
    lines.append([board[i][i] for i in range(3)])
    lines.append([board[i][2 - i] for i in range(3)])
    for line in lines:
        if line == [X, X, X]:
            return X
        if line == [O, O, O]:
            return O
    return None


def terminal(board):
    return winner(board) is not None or all(cell is not EMPTY for row in board for cell in row)


def utility(board):
    w = winner(board)
    if w == X:
        return 1
    if w == O:
        return -1
    return 0


def minimax(board):
    """Compute the optimal move using the minimax algorithm."""
    if terminal(board):
        return None

    turn = player(board)
    if turn == X:
        best_value = float('-inf')
        best_move = None
        for action in actions(board):
            value = min_value(result(board, action))
            if value > best_value:
                best_value = value
                best_move = action
        return best_move
    else:
        best_value = float('inf')
        best_move = None
        for action in actions(board):
            value = max_value(result(board, action))
            if value < best_value:
                best_value = value
                best_move = action
        return best_move


def max_value(board):
    if terminal(board):
        return utility(board)
    v = float('-inf')
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):
    if terminal(board):
        return utility(board)
    v = float('inf')
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v


def print_board(board):
    """Helper to print a board nicely."""
    for row in board:
        print("|".join('_' if cell is EMPTY else cell for cell in row))
    print()


def main():
    board = initial_state()
    while not terminal(board):
        move = minimax(board)
        board = result(board, move)
        print_board(board)
    print("Winner:", winner(board))


if __name__ == "__main__":
    main()
