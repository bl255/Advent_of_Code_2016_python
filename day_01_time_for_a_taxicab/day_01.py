input_1 = "../inputs_2016/input_01.txt"
# input_1 = "test_input.txt"

# dirs N:0, E:1, S:2, W: 3
dirs = {0: 0, 1: 0, 2: 0, 3: 0}
current_dir = 0
xy = []
first_returned = None

with open(input_1, mode="r") as text_file:
    instructions = text_file.read().split(", ")

for instruction in instructions:
    if instruction[0] == "R":
        current_dir = (current_dir + 1) % 4
    else:
        current_dir = (current_dir - 1) % 4
    for step in range(1, int(instruction[1:]) + 1):
        dirs[current_dir] += 1
        pos = (dirs[1] - dirs[3], dirs[0] - dirs[2])
        if pos in xy and not first_returned:
            first_returned = pos
        xy.append(pos)

print(f"Task 1: {abs(xy[-1][0]) + abs(xy[-1][1])}")
print(f"Task 2: {abs(first_returned[0]) + abs(first_returned[1])}")
