from collections import Counter
import re
from string import ascii_lowercase as lower

input_4 = "../inputs_2016/input_04.txt"
# input_4 = "test_input_2.txt"


with open(input_4, mode="r") as text_file:
    raw_input = text_file.read().split()

rooms_sum = 0
searched_rooms = []
for line in raw_input:
    beginning, end = line.split("[")
    beginning = " ".join(beginning.split("-")[:-1])

    room_data = [(v, k) for k, v in Counter(re.findall("[a-z]", beginning)).items()]
    room_sorted = sorted(room_data, key=lambda y: (-y[0], y[1]))
    room_code = [code[1] for code in room_sorted[:5]]

    room_id = int("".join(re.findall("[0-9]", line)))
    checksum = re.findall("[a-z]", end)

    if room_code == checksum:
        rooms_sum += room_id
        real_name = "".join([lower[(lower.index(sb) + room_id) % 26] if sb in lower else " " for sb in beginning])
        if "north" in real_name:
            searched_rooms.append((real_name, room_id))

print(f"Task 1: {rooms_sum}")
print(f"Task 2: {searched_rooms[0][1]}")

# Task 1 test output: 1514
