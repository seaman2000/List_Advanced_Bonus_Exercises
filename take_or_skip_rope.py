string = input()

clean_string = "".join(char for char in string if  not char.isdigit())
digits_list = [int(digit) for digit in string if digit.isdigit()]
take_list = [take_digit for idx, take_digit in enumerate(digits_list) if idx % 2 == 0]
skip_list = [skip_digit for idx, skip_digit in enumerate(digits_list) if idx % 2 == 1]

result = ""
pointer = 0

for take, skip in zip(take_list, skip_list):
    result += clean_string[pointer:pointer + take]
    pointer += take
    pointer += skip

print(result)