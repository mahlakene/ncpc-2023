import sys
lines = sys.stdin.readlines()
result = ""
some_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
for i in range(int(lines[0])):
    roman_string = str(lines[i + 1])[::-1]
    if roman_string[0] == '\n':
        roman_string = roman_string[1:]
    total = 0
    current_max = 0
    for c in roman_string:
        value = some_dict[c]
        current_max = max(current_max,value)
        if value >= current_max:
            total += value
        else:
            total -= value
    print(total)
