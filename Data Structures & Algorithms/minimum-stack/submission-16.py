from collections import deque
import heapq
    
class MinStack:
    
    def __init__(self):
        self.stack = deque()
    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        element_0 = self.stack[-1]
        return element_0

    def getMin(self) -> int:
        return heapq.nsmallest(1,self.stack)[0]
            
