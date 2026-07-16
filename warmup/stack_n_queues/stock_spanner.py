class StockSpanner:

    # def __init__(self):
    #     self.nums = []

    # def next(self, price: int) -> int:
    #     current = price
    #     count = 1
    #     n = len(self.nums)
    #     for i in range(n-1,-1,-1):
    #         if price<self.nums[i]:
    #             break
    #         count=count+1
    #     self.nums.append(price)
    #     return count

    def __init__(self):
        self.stack = []  

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            _, prev_span = self.stack.pop()
            span += prev_span
        self.stack.append((price, span))
        return span