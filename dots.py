def dfs(row_, col_, visited_):

    if row_ < 0 or row_ >= rows or col_ < 0 or col_ >= len(field[row_]):
        return 0
    if field[row_][col_] != ".":
        return 0
    if visited_[row_][col_]:
        return 0

    visited_[row_][col_] = True

    count = 1
    count += dfs(row_ - 1, col_, visited_)
    count += dfs(row_ + 1, col_, visited_)
    count += dfs(row_, col_ - 1, visited_)
    count += dfs(row_, col_ + 1, visited_)

    return count


rows = int(input())
field = []
for row in range(rows):
    current_row = input().split()
    field.append(current_row)

visited = [[False] * len(field[r]) for r in range(rows)]
max_dots = 0

for row in range(rows):
    for col in range(len(field[row])):
        if field[row][col] == "." and not visited[row][col]:
            size = dfs(row,col, visited)
            max_dots = max(max_dots, size)

print(max_dots)
