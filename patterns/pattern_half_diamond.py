# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

limit = 6
num_of_rows = 11
step = 1
for i in range(1,num_of_rows+1):
    if i<limit:
        for j in range(0,i):
            print("*",end='')
    else:
        for j in range(0, (limit-step)):
            print("*", end='')
        step += 1
    print()