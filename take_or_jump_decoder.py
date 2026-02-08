string = input()

clean_string = "".join(char for char in string if not char.isdigit())
digits_lst = [int(digit) for digit in string if digit.isdigit()]
take_indices = [digit for idx, digit in enumerate(digits_lst) if idx % 2 == 0]
skip_indices = [digit for idx, digit in enumerate(digits_lst) if idx % 2 == 1]

index = 0
result = ""
for take, skip in zip(take_indices, skip_indices):
    result += clean_string[index:index + take]
    index += take
    index += skip

difference = len(take_indices) - len(skip_indices)
if difference > 0:
    for remaining_take in take_indices[len(skip_indices):]:
        result += clean_string[index:index + remaining_take]
        index += remaining_take

print(result)
