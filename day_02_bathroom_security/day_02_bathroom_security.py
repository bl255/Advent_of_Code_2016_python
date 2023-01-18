# input_2 = "../inputs_2016/input_02.txt"
input_2 = "test_input.txt"

KEYPAD = [
    "1", "2", "3",
    "4", "5", "6",
    "7", "8", "9"
]
KEYPAD_2 = [
    "1",
    "2", "3", "4",
    "5", "6", "7", "8", "9",
    "A", "B", "C",
    "D"
]
KEYPAD_POSS = [
    (0, 0), (0, 1), (0, 2),
    (1, 0), (1, 1), (1, 2),
    (2, 0), (2, 1), (2, 2)]
KEYPAD_2_POSS = [
    (0, 0),
    (1, -1), (1, 0), (1, 1),
    (2, -2), (2, -1), (2, 0), (2, 1), (2, 2),
    (3, -1), (3, 0), (3, 1),
    (4, 0)
]

with open(input_2, mode="r") as text_file:
    instructions = text_file.read().splitlines()


def get_final_code(keypad, possibilities, instr, start):
    pos = start
    directions = ""

    def change_pos(ltr, indexes):
        nonlocal pos
        code = {"U": (pos[0] - 1, pos[1]), "D": (pos[0] + 1, pos[1]), "R": (pos[0], pos[1] + 1),
                "L": (pos[0], pos[1] - 1)}
        new_pos = code[ltr]
        if new_pos in indexes:
            pos = new_pos

    for line in instr:
        for letter in line:
            change_pos(letter, possibilities)
        directions += keypad[possibilities.index(pos)]
    return directions


print(f"Task 1: {get_final_code(KEYPAD, KEYPAD_POSS, instructions, (1, 1))}")
print(f"Task 2: {get_final_code(KEYPAD_2, KEYPAD_2_POSS, instructions, (2, -2))}")

# Task 1 test output: 1985
# Task 2 test output: 5DB3
