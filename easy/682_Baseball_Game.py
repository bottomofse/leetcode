from collections import deque

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        q = deque()
        for val in ops:
            if val.isnumeric() or '-' in val:
                q.append(int(val))
                continue
            if val == '+':
                a = q.pop()
                b = q.pop()
                q.append(b)
                q.append(a)
                q.append(a + b)  
                continue
            if val == 'D':
                a = q.pop()
                q.append(a)
                q.append(a * 2)
                continue
            if val == 'C':
                q.pop()
                continue
        return sum(q)