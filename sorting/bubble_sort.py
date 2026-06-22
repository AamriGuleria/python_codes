


def bubble_sort(array: list):
    try:
        for i in range(len(array)):
            swapped = False
            for j in range(len(array)-1-i):
                if array[j]>array[j+1]:
                    swap_elements(array, j, j+1)
                    swapped = True
            if swapped == False:
                break
        for i in range(len(array)):
            print(array[i], end=" ")
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
    bubble_sort(elements)