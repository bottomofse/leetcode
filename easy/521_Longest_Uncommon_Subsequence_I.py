from collections import deque
class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        long_list = deque(list(a)) if len(a) >= len(b) else deque(list(b))
        long_list_len = len(long_list)
        short_list = deque(list(a)) if len(a) < len(b) else deque(list(b))
                
        #print(long_list)
        #print(short_list)
        while long_list and short_list:
            if long_list[0] == short_list[0]:
                long_list.popleft()
                short_list.popleft()
            else:
                long_list.popleft()
        if len(long_list) == 0 and len(short_list) == 0:
            return -1
        if len(long_list) == 0:
            return max(len(a), len(b))
        if len(short_list) == 0:
            return long_list_len
        return -1