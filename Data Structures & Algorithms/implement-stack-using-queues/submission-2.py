class MyStack:

    def __init__(self):
        self.deque_list = deque()
        

    def push(self, x: int) -> None:
        self.deque_list.append(x)

    def pop(self) -> int:
        return self.deque_list.pop()
        

    def top(self) -> int:
        return self.deque_list[-1]

    def empty(self) -> bool:
        if len(self.deque_list) == 0:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()