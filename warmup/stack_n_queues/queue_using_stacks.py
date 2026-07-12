from collections import deque
class MyQueue:

    def __init__(self):
        self.in_list = []
        self.out_list = []

    def push(self, x: int) -> None:
        self.in_list.append(x)

    def pop(self) -> int:
        self.transfer_in_lists()
        return self.out_list.pop()

    def peek(self) -> int:
        self.transfer_in_lists()
        return self.out_list[-1]

    def empty(self) -> bool:
        return len(self.in_list)+len(self.out_list)==0

    def transfer_in_lists(self):
        if not self.out_list:
            while self.in_list:
                self.out_list.append(self.in_list.pop())

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()