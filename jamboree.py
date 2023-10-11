import sys
lines = sys.stdin.readlines()
total_items = int(lines[0].split()[0])
total_scouts = int(lines[0].split()[1])
items_weights = lines[1].split()
items_weights_in_int = []
for i in items_weights:
    items_weights_in_int.append(int(i))

sorted_list = sorted(items_weights_in_int)[::-1]

new_list = [0 for i in range(total_scouts)]
for i, j in enumerate(sorted_list):
    if total_scouts > i:
        new_list[i] = j
    else:
        sorted_list = sorted_list[i:]
        break
if total_items <= total_scouts:
    print(max(new_list))
new_list = new_list[::-1]
for i, j in enumerate(sorted_list):
    new_list[i] += j
if total_items > total_scouts:
    print(max(new_list))
