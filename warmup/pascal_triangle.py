


from typing import List


def generate(self, numRows: int) -> List[List[int]]:
    final_list = []
    for i in range(numRows):
        if i == 0:
            final_list.append([1])
        elif i == 1:
            final_list.append([1,1])
        else:
            final_list.append(self.generates_next(final_list[-1]))
    return final_list

def generates_next(self, prev_list):
    new_list = [1]
    for i in range(len(prev_list)-1):
        new_list.append(prev_list[i] + prev_list[i+1])
    new_list.append(1)
    return new_list

if __name__ == "__main__":
    num = int(input("Enter the Number: "))
    generate(num)
