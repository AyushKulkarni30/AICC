def is_safe(board, row, col, n):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, row, n):
    if row == n:
        # All queens are placed, return true to signal success
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            # Place queen
            board[row][col] = 1

            # Recur to place rest of the queens
            if solve_n_queens(board, row + 1, n):
                return True

            # If placing queen in board[row][col] doesn't lead to a solution, backtrack
            board[row][col] = 0

    # If the queen cannot be placed in any column in this row, return false to backtrack
    return False

def n_queens(n):
    # Create an empty n x n chessboard
    board = [[0 for _ in range(n)] for _ in range(n)]

    # Try to place queens recursively
    if not solve_n_queens(board, 0, n):
        print("Solution does not exist")
        return

    # Print the solution
    for row in board:
        print(row)

# Example usage
n_queens(4)
