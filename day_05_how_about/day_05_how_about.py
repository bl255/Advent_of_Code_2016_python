import hashlib

room_id = "abc"

result = hashlib.md5(room_id.encode())

# print(result)

# 18f47a30

print(result.hexdigest())