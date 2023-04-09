import re
import numpy as np
import time

t1 = time.time()
input_9 = "../inputs_2016/input_09.txt"
# input_9 = "test_input.txt"

with open(input_9, mode="r") as text_file:
    raw_message = text_file.read()
    no_newline_message = raw_message.strip()

pattern = r"\(\d+x\d+\)"


# TASK 1
whole_length1 = 0
decompressed1 = no_newline_message
while re.search(pattern, decompressed1):
    search1 = re.search(pattern, decompressed1)
    repeated_len, repeat = map(int, re.findall(r"\d+", search1.group()))
    head_len = search1.span()[0]
    if repeated_len > len(decompressed1):
        repeated_len = len(decompressed1)
    whole_length1 += (head_len + repeated_len * repeat)
    decompressed1 = decompressed1[search1.span()[1] + repeated_len:]
tail = decompressed1
whole_length1 += len(tail)


# TASK 2
repeats = np.ones(len(no_newline_message), dtype="int64")
for item in re.finditer(pattern, no_newline_message):
    repeat_len, repeat_amount = list(map(int, re.findall(r"\d+", item.group())))
    repeat_start, repeat_end = item.end(), item.end() + repeat_len
    repeats[repeat_start:repeat_end] *= repeat_amount

pure_text = re.sub(f"[^{pattern}]", "*", no_newline_message)
pure_text = re.sub(r"[^*]", "0", pure_text)
pure_text = re.sub(r"[^0]", "1", pure_text)
pure_text = np.array(tuple(map(int, pure_text)), dtype="int64")
final = pure_text * repeats
final_sum = np.sum(final)

print(f"Task 1: {whole_length1}")
print(f"Task 2: {final_sum}")



