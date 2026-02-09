def dfs(maze, visited, rows, r, c, moves):

    if r < 0 or r >= rows or c < 0 or c >= len(maze[r]):
        return moves

    if maze[r][c] == "#":
        return -1

    if visited[r][c]:
        return -1

    visited[r][c] = True

    up = dfs(maze, visited, rows, r - 1, c, moves + 1)
    down = dfs(maze, visited, rows, r + 1, c, moves + 1)
    left = dfs(maze, visited, rows, r, c - 1, moves + 1)
    right = dfs(maze, visited, rows, r, c + 1, moves + 1)

    visited[r][c] = False

    return max(up, down, left, right)


rows = int(input())
maze = []
k_row = k_col = None

for r in range(rows):
    line = input()
    maze.append(list(line))
    if "k" in line:
        k_row = r
        k_col = line.index("k")

visited = [[False] * len(maze[r]) for r in range(rows)]

best = dfs(maze, visited, rows, k_row, k_col, 0)

if best == -1:
    print("Kate cannot get out")
else:
    print(f"Kate got out in {best} moves")
    




