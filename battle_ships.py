field = []
rows = int(input())
for row in range(rows):
    current_row = list(map(int, input().split()))
    field.append(current_row)

attacked = input().split()
attacked_field = [attack.split("-") for attack in attacked]
