class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs.pop()
        while strs:
            poped = strs.pop()
            next_prefix = ''
            for i in range(len(poped)):
                if i >= len(prefix):
                    break
                if poped[i] == prefix[i]:
                    next_prefix += prefix[i]
                else:
                    break
            prefix = next_prefix
        return prefix
