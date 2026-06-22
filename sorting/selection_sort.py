


def selection_sort(array: list):
    try:
        for i in range(len(array)-1):
            elem = array[i]
            smallest_index = i
            for j in range(i+1, len(array)):
                if array[smallest_index]>array[j]:
                    smallest_index = j
            # if smallest_index is not None:
            swap_elements(array, i, smallest_index)
        # Print the sorted Array now
        for elem in array:
            print (elem, end=" ")
    except Exception as e:
        raise

def swap_elements(array: list , i , j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp



if __name__ == "__main__":
    array = str(input("Enter the array elements"))
    elements = array.split(" ")
    elements = list(map(int, elements))
    selection_sort(elements)