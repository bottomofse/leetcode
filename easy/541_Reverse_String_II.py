from collections import deque
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s_list = deque(list(s))
        output = []
        stack = []
        cnt = 0
        while s_list:
            tmp = s_list.popleft()
            if cnt < k:
                stack.append(tmp)
            else:
                while stack:
                    output.append(stack.pop())
                output.append(tmp)
            if cnt == 2 * k - 1:
                cnt = 0
            else:
                cnt += 1
        if stack:
            while stack:
                output.append(stack.pop())
        return ''.join(output)