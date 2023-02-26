import re

input_7 = "../inputs_2016/input_07.txt"
# input_7 = "test_input.txt"
# input_7 = "test_input2.txt"


def reverse_aba(aba_str):
    return f"{aba_str[1]}{aba_str[0]}{aba_str[1]}"


with open(input_7, mode="r") as text_file:
    addresses = text_file.read().splitlines()

supports_tsl = []
supports_ssl = []

pattern_in = r"\[(.*?)\]"
pattern_out = r"(?:(?<=^)|(?<=\]))[^\[\]]+(?:(?=$)|(?=\[))"
pattern_abba = r"(.)(?!\1)(.)\2\1"
pattern_aba = r"(?=(.)(?!\1)(.)(\1))"  # sort of works


for address in addresses:
    inside_brackets = re.findall(pattern_in, address)
    outside_brackets = re.findall(pattern_out, address)

    # task 1
    if any([re.search(pattern_abba, item) is not None for item in inside_brackets]):
        supports_tsl.append(False)
    elif any([re.search(pattern_abba, item) is not None for item in outside_brackets]):
        supports_tsl.append(True)
    else:
        supports_tsl.append(False)

    # task 2
    aba_outside_brackets = set()
    aba_inside_brackets = set()

    for item in outside_brackets:
        aba_outside_brackets.update(["".join(chars) for chars in re.findall(pattern_aba, item)])
    for item in inside_brackets:
        aba_inside_brackets.update(["".join(chars) for chars in re.findall(pattern_aba, item)])

    len_sorted_aba = sorted([aba_inside_brackets, aba_outside_brackets], key=len)
    if len(len_sorted_aba[0]) != 0:
        supports_ssl.append(any([reverse_aba(aba) in len_sorted_aba[1] for aba in len_sorted_aba[0]]))
    else:
        supports_ssl.append(False)


print(f"Task 1: {sum(supports_tsl)}")
print(f"Task 2: {sum(supports_ssl)}")
