# input_2 = "../inputs_2016/input_02.txt"
input_2 = "test_input.txt"

KEYPAD = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]
KEYPAD_2 = [
    ["1"],
    ["2", "3", "4"],
    ["5", "6", "7", "8", "9"],
    ["A", "B", "C"],
    ["D"]
]
KEYPAD_INDEXES = [
    (0, 0), (0, 1), (0, 2),
    (1, 0), (1, 1), (1, 2),
    (2, 0), (2, 1), (2, 2)]
KEYPAD_2_INDEXES = [
    (0, 0),
    (1, 0), (1, 1), (1, 2),
    (2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
    (3, 0), (3, 1), (3, 2),
    (4, 0)
]
POS = 1, 1

with open(input_2, mode="r") as text_file:
    instructions = text_file.read().splitlines()


# def change_pos(ltr):
#     global POS
#     code = {"U": (POS[0] - 1, POS[1]), "D": (POS[0] + 1, POS[1]), "R": (POS[0], POS[1] + 1), "L": (POS[0], POS[1] - 1)}
#     new_pos = code[ltr]
#     if min(new_pos) > -1 and max(new_pos) < 3:
#         POS = new_pos


# directions = ""
# for line in instructions:
#     for letter in line:
#         change_pos(letter)
#     directions += str(KEYPAD[POS[0]][POS[1]])
#
# print(f"Task 1: {directions}")


# def change_pos_2(ltr, keypad):
#     global POS
#     code = {"U": (POS[0] - 1, POS[1]), "D": (POS[0] + 1, POS[1]), "R": (POS[0], POS[1] + 1), "L": (POS[0], POS[1] - 1)}
#     new_pos = code[ltr]
#     try:
#         keypad[new_pos[0]][new_pos[1]]
#     except IndexError:
#         pass
#     else:
#         POS = new_pos


def change_pos_2(ltr, indexes):
    global POS
    code = {"U": (POS[0] - 1, POS[1]), "D": (POS[0] + 1, POS[1]), "R": (POS[0], POS[1] + 1), "L": (POS[0], POS[1] - 1)}
    new_pos = code[ltr]
    if new_pos in indexes:
        POS = new_pos


directions = ""
for line in instructions:
    for letter in line:
        change_pos_2(letter, KEYPAD_INDEXES)
        print(letter, POS)
    directions += str(KEYPAD[POS[0]][POS[1]])
    print()

print(f"Task 1: {directions}")
#
# print(f"Task 2: {0}")
