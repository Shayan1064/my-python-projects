import random
import string


value=string.ascii_letters+string.digits

pass_length=10
password=""
for i in range(pass_length):
    password+=random.choice(value)

print("Your Random Password : ",password)
