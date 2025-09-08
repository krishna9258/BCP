# **********
# ****  ****
# ***    ***
# **      **
# *        *

n = 5

for i in range(n, 0, -1):
    print("*" * i, end="")
    spaces = (n - i) * 2
    print(" " * spaces, end="")
    if i != n:
        print("*" * i, end="")
    print()

print("*",end="")