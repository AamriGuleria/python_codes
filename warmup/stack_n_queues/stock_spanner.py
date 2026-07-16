class StockSpanner:

    def __init__(self):
        self.nums = []

    def next(self, price: int) -> int:
        current = price
        count = 1
        n = len(self.nums)
        for i in range(n-1,-1,-1):
            if price<self.nums[i]:
                break
            count=count+1
        self.nums.append(price)
        return count