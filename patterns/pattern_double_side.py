
# 1      1
# 12    21
# 123  321
# 12344321
import threading
import multiprocessing

inc_limit =4
row_limit = 4
col_limit = 8

def inc_pattern():
    for i in range(1,row_limit+1):
        for j in range(1,i+1):
            print(j,end='')
        print()

def dec_pattern():
    for i in range(1, row_limit+1):
        spaces = (col_limit//2)-i
        print(" "*spaces, end='')
        for j in range(i, 0, -1):
            print(j, end='')
        print()

if __name__ == '__main__':  
    p1 = multiprocessing.Process(target=inc_pattern)
    p2 = multiprocessing.Process(target=dec_pattern)
    
    p1.start()
    p2.start()  
    
    p1.join()
    p2.join()