def isValidMove(board, i, j, n):
    return 0 <= i < n and 0 <= j < n and board[i][j] == -1

def printBoard(board, n):
    for i in range(n):
        for j in range(n):
            print(f'{board[i][j]:2}', end=' ')
        print()

def getMoves(board, i, j, n):
    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
    valid_moves = []
    for move in moves:
        new_i, new_j = i + move[0], j + move[1]
        if isValidMove(board, new_i, new_j, n):
            count = 0
            for m in moves:
                x, y = new_i + m[0], new_j + m[1]
                if isValidMove(board, x, y, n):
                    count += 1
            valid_moves.append((new_i, new_j, count))
    return sorted(valid_moves, key=lambda x: x[2])

def solveKnightTour(board, n, i, j, pos):
    if pos == n ** 2:
        return True

    next_moves = getMoves(board, i, j, n)
    for move in next_moves:
        new_i, new_j, _ = move
        board[new_i][new_j] = pos
        if solveKnightTour(board, n, new_i, new_j, pos + 1):
            return True
        board[new_i][new_j] = -1
    return False

def knightTour(n):
    board = [[-1 for _ in range(n)] for _ in range(n)]
    printBoard(board, n)
    board[0][0] = 0
    if solveKnightTour(board, n, 0, 0, 1):
        printBoard(board, n)
    else:
        print('Solution does not exist')

if __name__ == '__main__':
    knightTour(8)
