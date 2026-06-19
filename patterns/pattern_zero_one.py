
# 1
# 01
# 101
# 0101
# 10101


limit = 6

for i in range(0,limit):
    for j in range(0,i):
        if (i+j)%2 == 0:
            print("1",end='')
        else:
            print("0",end='')
    print()