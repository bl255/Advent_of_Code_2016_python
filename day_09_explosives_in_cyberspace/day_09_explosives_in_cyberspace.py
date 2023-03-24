import re

input_9 = "../inputs_2016/input_09.txt"


def decode(message):
    # pattern = r"(?<!\))\(\d+x\d+\)"
    pattern = r"\(\d+x\d+\)"
    index_shift = 0
    add_to_decoded = 0
    next_mark = re.search(pattern, message[index_shift:])
    print(next_mark)

    while next_mark:
        instruction_len = len(next_mark.group())
        repeated_len, repeat = map(int, re.findall(r"\d+", next_mark.group()))
        index_shift += repeated_len + instruction_len
        add_to_decoded += (repeated_len * (repeat - 1)) - instruction_len
        next_mark = re.search(pattern, message[index_shift:])
    return add_to_decoded + len(message)


aoc_examples = [
    ("ADVENT", "ADVENT"),
    ("A(1x5)BC", "ABBBBBC"),
    ("(3x3)XYZ", "XYZXYZXYZ"),
    ("(6x1)(1x3)A", "(1x3)A"),
    ("X(8x2)(3x3)ABCY", "X(3x3)ABC(3x3)ABCY"),
    ("A(2x2)BCD(2x2)EFG", "ABCBCDEFEFG")
]

for example in aoc_examples:
    assert decode(example[0]) == len(example[1])

my_examples = [
    ("(7x2)AA(1x2)C", "AA(1x2)AA(1x2)C"),
    ("(7x2)AA(1x2)C(1x10)M", "AA(1x2)AA(1x2)CMMMMMMMMMM")
]

for example in my_examples:
    assert decode(example[0]) == len(example[1])


with open(input_9, mode="r") as text_file:
    raw_message = text_file.read()
    no_newline_message = raw_message.strip()

print(decode(no_newline_message))

# print(decode("(3x3)(2x2)HIJ(2x2)KLM(1x1)NO"))


# print(len(re.findall("\s", raw_message)))

# finds = list(re.finditer(pattern, message))
# if not finds:
#     return len(message)

# beginning = finds[0].span()[0]
# end = len(message) - finds[-1].span()[1]
# middle_span = []
# for num in range(len(finds) - 1):
#     middle_span.append(finds[num + 1].span()[0] - finds[num].span()[1])
# middle_span.append(end)
#
# mark_turns = []
# for num, find in enumerate(finds):
#     index, repeat = map(int, re.findall(r"\d+", finds[num].group()))
#     mark_turns.append(index * repeat + max(middle_span[num] - index, 0))
# return beginning + sum(mark_turns)


# nope