import heapq
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

    def __init__(self):
        self.lo = [] 
        self.hi = [] 
    def addNum(self, num: int) -> None:
        if not self.lo or num <= -self.lo[0]:
            heapq.heappush(self.lo,-num)
        else:
            heapq.heappush(self.hi,num)
        
        if len(self.lo)>len(self.hi)+1:
            heapq.heappush(self.hi, -heapq.heappop(self.lo))
        elif len(self.hi)>len(self.lo):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))
    def findMedian(self) -> float:
        if len(self.lo) > len(self.hi):
            return -self.lo[0]
        return (-self.lo[0] + self.hi[0]) / 2

