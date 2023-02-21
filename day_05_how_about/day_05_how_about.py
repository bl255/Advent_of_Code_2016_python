import hashlib
from datetime import datetime

input_5 = "../inputs_2016/input_05.txt"
# input_5 = "test_input.txt"

t0 = datetime.now()
with open(input_5, mode="r") as text_file:
    door_id = text_file.read()

num = 0
password1 = ""
password2 = ["_" for n in range(8)]
string = door_id + str(num)
while len(password1) < 8 or "_" in password2:
    string = door_id + str(num)
    processed_string = hashlib.md5(string.encode()).hexdigest()
    if processed_string[:5] == "00000":

        # task1:
        if len(password1) < 8:
            password1 += processed_string[5]

        # task 2
        try:
            pos = int(processed_string[5])
        except ValueError:
            pass
        if 0 <= pos <= 7 and password2[pos] == "_":
            password2[pos] = processed_string[6]

    num += 1

print(f"Task 1: {password1}")
print(f"Task 2: {''.join(password2)}")

t1 = datetime.now()
print(f"Time: {(t1 - t0).total_seconds()} seconds")
