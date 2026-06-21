
# 1      1
# 12    21
# 123  321
# 12344321
import threading

inc_limit =4
row_limit = 4
col_limit = 8
inc_pattern = []
dec_pattern = []
def increement_pattern():
    global inc_pattern
    for i in range(1,row_limit+1):
        inc_pattern.append(''.join(str(j) for j in range(1, i + 1)))

def decreement_pattern():
    global dec_pattern
    for i in range(1, row_limit+1):
        spaces = col_limit - 2 * i
        dec_pattern.append(" " * spaces + ''.join(str(j) for j in range(i, 0, -1)))

if __name__ == '__main__':  
    p1 = threading.Thread(target=increement_pattern)
    p2 = threading.Thread(target=decreement_pattern)
    
    p1.start()
    p2.start()  
    
    p1.join()
    p2.join()

    for inc,dec in zip(inc_pattern, dec_pattern):
        print(inc+dec)