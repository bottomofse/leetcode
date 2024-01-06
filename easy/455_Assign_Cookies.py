class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
            children = sorted(g)
            cookies = sorted(s)
            cnt = 0
            for cookie in cookies:
                if cnt < len(children) and cookie >= children[cnt]:
                    cnt += 1
            return cnt
