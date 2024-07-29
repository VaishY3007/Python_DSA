from pycallgraph2 import PyCallGraph
from pycallgraph2.output import GraphvizOutput

def isValidMove(maze, i, j):
    return 0 <= i < len(maze) and 0 <= j < len(maze[0]) and maze[i][j] == 1

def solveMaze(maze, i, j, solution):
    if i == len(maze) - 1 and j == len(maze[0]) - 1:
        solution[i][j] = 1
        return True

    if isValidMove(maze, i, j):
        solution[i][j] = 1

        directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        for di, dj in directions:
            nextI, nextJ = i + di, j + dj
            if solveMaze(maze, nextI, nextJ, solution):
                return True

        solution[i][j] = 0
        return False

    return False

def ratInAMaze(maze):
    if not maze:
        return []

    solution = [[0] * len(maze[0]) for _ in range(len(maze))]
    if solveMaze(maze, 0, 0, solution):
        return solution

    return []

if __name__ == '__main__':
    graphviz = GraphvizOutput()
    graphviz.output_file = 'call_graph.png'

    with PyCallGraph(output=graphviz):
        maze = [
            [1, 1, 1, 0],
            [1, 0, 0, 0],
            [1, 1, 0, 0],
            [0, 1, 1, 1]
        ]

        solution = ratInAMaze(maze)

        if solution:
            print('Solution:')
            for row in solution:
                print(row)
        else:
            print('No Solution Exists')
