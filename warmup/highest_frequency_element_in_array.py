
from collections import Counter, defaultdict


def highest_frequency_element(array: list)-> None:
    freq = Counter(array)
    max_item = freq.most_common(1)
    max_element, max_count = max_item[0]
    print(f"Maximum Frequency Element is {max_element} (appears {max_count} times)") 

def highest_frequency_approach_2(array: list)-> None:
    freq = defaultdict(int)
    for item in array:
        freq[item] += 1
    
    max_element = max(freq, key=freq.get)
    print(f"Maximum Frequency Element is {max_element} (appears {freq[max_element]} times)")

if __name__ == "__main__":
    array = str(input("Enter the array elements: "))
    array = array.split()
    highest_frequency_element(array)

