from collections import deque
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        queue = deque()
        while s:
            queue.append(s.pop())
        while queue:
            s.append(queue.popleft())
