import re
from math import prod

input_10 = "../inputs_2016/input_10.txt"
# input_10 = "test_input.txt"

OUTS = {"bot": {}, "output": {}}


class Bot:
    def __init__(self):
        self.holds = []
        self.low_high = []  # [(OUT_DICT, num), (OUT_DICT, num)]

    @staticmethod
    def bot_out_action(out_dict, num, to_send):
        if out_dict == "bot":
            if num not in OUTS["bot"]:
                OUTS["bot"][num] = Bot()
                OUTS["bot"][num].holds = [to_send]
            else:
                OUTS["bot"][num].holds.append(to_send)
                OUTS["bot"][num].bot_config_check()

        if out_dict == "output":
            if num not in OUTS["output"]:
                OUTS["output"][num] = [to_send]
            else:
                OUTS["output"][num].append(to_send)

    def bot_value_in_action(self, in_value):
        self.holds.append(in_value)
        self.bot_config_check()

    def bot_instructions_in_action(self, low, high):
        self.low_high.extend([low, high])
        self.bot_config_check()

    def bot_config_check(self):
        assert len(self.holds) <= 2, "Too many held items"
        assert len(self.low_high) <= 2, "Too many instructions"

        if len(self.holds) == 2 and len(self.low_high) == 2:
            self.bot_out_action(self.low_high[0][0], self.low_high[0][1], min(self.holds))
            self.bot_out_action(self.low_high[1][0], self.low_high[1][1], max(self.holds))


with open(input_10, mode="r") as text_file:
    instructions = text_file.read().splitlines()

for string in instructions:

    if "value" in string:
        value, bot_num = map(int, re.findall(r"\d+", string))
        if bot_num not in OUTS["bot"]:
            OUTS["bot"][bot_num] = Bot()
        OUTS["bot"][bot_num].bot_value_in_action(value)

    elif string[:3] == "bot":
        bot_num, out_low, out_high = map(int, re.findall(r"\d+", string))
        dict_low, dict_high = re.findall(r"bot|output", string[3:])
        if bot_num not in OUTS["bot"]:
            OUTS["bot"][bot_num] = Bot()
        OUTS["bot"][bot_num].bot_instructions_in_action((dict_low, out_low), (dict_high, out_high))

    else:
        print("Wrong string")

handles_17_61 = [num for num, bot in OUTS["bot"].items() if 17 in bot.holds and 61 in bot.holds][0]
multiplication_outputs_012 = prod([val[0] for key, val in OUTS["output"].items() if key in [0, 1, 2]])

print(f"Task 1: {handles_17_61}")
print(f"Task 2: {multiplication_outputs_012}")
