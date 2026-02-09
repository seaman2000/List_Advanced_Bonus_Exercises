field = []
rows = int(input())
for row in range(rows):
    current_row = list(map(int, input().split()))
    field.append(current_row)

attacked = input().split()
attacked_field = [[int(x) for x in attack.split("-")] for attack in attacked]

destroyed = 0
for row, col in attacked_field:
    if field[row][col] > 0:
        field[row][col] -= 1
        if field[row][col] == 0:
            destroyed += 1

print(destroyed)