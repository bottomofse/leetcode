from collections import deque
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.reserve = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        while len(self.stack) > 1:
            self.reserve.append(self.stack.pop())
        ret = self.stack.pop()
        while self.reserve:
            self.stack.append(self.reserve.pop())
        return ret
        
    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack[0]
        
    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack) == 0