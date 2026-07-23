class MedianFinder:

    def __init__(self):
        self.numbers = []

    def addNum(self, num: int) -> None:
        self.numbers.append(num)

    def findMedian(self) -> float:
        self.numbers.sort()
        n = len(self.numbers)
        if n % 2 == 0:
            i = n // 2
            j = i - 1
            return (self.numbers[i] + self.numbers[j]) / 2  
        else:
            return self.numbers[n // 2]