import re
import numpy as np
import matplotlib.pyplot as plt

input_8 = "../inputs_2016/input_08.txt"
# input_8 = "test_input.txt"

with open(input_8, mode="r") as text_file:
    instructions = text_file.read().splitlines()

# SCREEN FOR TEST DATA:
# test_screen = np.zeros((3, 7), dtype="int16")
# screen = test_screen

true_screen = np.zeros((6, 50), dtype="int16")
screen = true_screen


def shifted_vector(vector, index):
    a, b = vector[:index], vector[index:]
    return np.concatenate((b, a))


for instruction in instructions:
    nums = [int(num) for num in re.findall(r"\d+", instruction)]
    if "rect" in instruction:
        screen[:nums[1], :nums[0]] = 1
    elif "row" in instruction:
        screen[nums[0]] = shifted_vector(screen[nums[0]], - nums[1])
    else:
        screen[:, nums[0]] = shifted_vector(screen[:, nums[0]], - nums[1])

print(f"Task 1: {np.sum(screen)}")  # task 1

# plotting task 2:
for_print = np.array(screen)
img = plt.imshow(for_print, cmap="Greys")
ax = plt.gca()
plt.axis("off")

plt.show()



