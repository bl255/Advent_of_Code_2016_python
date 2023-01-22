import numpy as np
np.set_printoptions(threshold=np.inf)

input_3 = "../inputs_2016/input_03.txt"


def sum_triangle_rows(arr_2d):
    row_rule = (np.median(arr_2d, axis=1).astype(int) + np.min(arr_2d, axis=1)) > np.max(arr_2d, axis=1)
    return np.sum(row_rule)


def transpose_bits(arr_2d):
    transposed_splits = [np.transpose(item) for item in np.array_split(arr_2d, arr_2d.shape[0] // 3, axis=0)]
    return np.concatenate(transposed_splits, axis=0)


with open(input_3, mode="r") as text_file:
    instructions = [line.split() for line in text_file.read().splitlines()]
rows = np.array(instructions).astype(int)


print(f"Task 1: {sum_triangle_rows(rows)}")
print(f"Task 2: {sum_triangle_rows(transpose_bits(rows))}")
