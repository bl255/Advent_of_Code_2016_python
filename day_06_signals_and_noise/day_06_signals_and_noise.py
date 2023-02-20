from collections import Counter

# input_6 = "../inputs_2016/input_06.txt"
input_6 = "test_input.txt"

with open(input_6, mode="r") as text_file:
    message = text_file.read().splitlines()

rows = list(zip(*message))
most_common_in_column = "".join([Counter(r).most_common()[0][0] for r in rows])
least_common_in_column = "".join([Counter(r).most_common()[-1][0] for r in rows])

print(f"Task 1: {most_common_in_column}")
print(f"Task 2: {least_common_in_column}")
