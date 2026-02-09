

number_of_rows = int(input())
maze = []
for row in range(number_of_rows):
    current_row = input()
    maze.append(current_row)

    if "k" in current_row:
        col = current_row.index("k")
        k_row = row



