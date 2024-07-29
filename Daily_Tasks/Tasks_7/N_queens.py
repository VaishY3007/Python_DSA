def validate(board, row, col, n):
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

def solveQueens(board, row, n, result):
    if row == n:
        result.append([row[:] for row in board])
        return
    
    for col in range(n):
        if validate(board, row, col, n):
            board[row][col] = 1
            solveQueens(board, row+1, n, result)
            board[row][col] = 0

def NQueens(n):
    board = [[0] * n for _ in range(n)]
    result = []
    solveQueens(board, 0, n, result)
    return result

def printSolution(solutions):
    if not solutions:
        print('No solution')
        return
    for solution in solutions:
        for row in solution:
            print(' '.join('Q' if col == 1 else '.' for col in row))
        print()

if __name__ == '__main__':
    n = 6
    solutions = NQueens(n)
    printSolution(solutions)
