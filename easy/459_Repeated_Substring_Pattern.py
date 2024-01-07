from collections import deque
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        divide = 2
        
        while divide <= len(s):
            if len(s) % divide != 0:
                divide += 1
                continue
            queue = deque(list(s))
            target = deque()
            
            for i in range(len(s) // divide):
                target.append(queue.popleft())
            flg = True
            while queue:
                for j in range(len(target)):
                    if queue.popleft() != target[j]:
                        flg = False
                        queue = []
                        break
            if flg:
                return True
            divide += 1
        return False