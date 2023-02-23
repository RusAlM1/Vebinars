import string
import random

# print(help(string))

symbol = string.ascii_letters + string.digits + "!_"
print(random.choice(symbol))

# Решение1
    # for sym1 in s1:
    #     for sym2 in s2:
    #         if sym1 == sym2:
    #             return True
    # return False

g = "aeiou"
# s = "".join(set(string.ascii_lowercase).difference(g))
# print(s)
s = "fwzbknptvxcrjyhqdgmsl"
L = 6
res = ""
for i in range(L):
    if i % 2 == 0:
        res += random.choice(s)
    else:
        res += random.choice(g)


print(res)