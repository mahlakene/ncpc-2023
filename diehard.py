import sys
lines = sys.stdin.readlines()
first_dice = sorted([int(i) for i in lines[0].split()])
second_dice = sorted([int(i) for i in lines[1].split()])
third_dice = sorted([int(i) for i in lines[2].split()])


first_win_count = 0
second_win_count = 0
third_win_count = 0


def calculate_win_percentage(dice1, dice2):
    if dice1[0] == dice1[1] == dice1[2] == dice1[3] == dice1[4] == dice1[5] \
            == dice2[0] == dice2[1] == dice2[2] == dice2[3] == dice2[4] == dice2[5]:
        return 0
    win_count = 0
    for i in dice1:
        for j in dice2:
            if i > j:
                win_count += 1
    for i in dice1:
        for j in dice2:
            if i == j:
                win_count += 0.5
    return win_count / 36


first_win_percentage = min(calculate_win_percentage(first_dice, second_dice),
                           calculate_win_percentage(first_dice, third_dice))
second_win_percentage = min(calculate_win_percentage(second_dice, first_dice),
                            calculate_win_percentage(second_dice, third_dice))
third_win_percentage = min(calculate_win_percentage(third_dice, first_dice),
                           calculate_win_percentage(third_dice, second_dice))
if first_win_percentage >= 0.5:
    print(1)
elif second_win_percentage >= 0.5:
    print(2)
elif third_win_percentage >= 0.5:
    print(3)
else:
    print("No dice")
