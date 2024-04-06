import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        l = paragraph.lower()
        print(l)
        s_list = re.split(r"[ !?',;.]", l)
        banned_set = set(banned)
        check = {}
        print(s_list)
        for i in s_list:
            if not i:
                continue
            if i in banned_set:
                continue
            if i in check:
                check[i] += 1
            else:
                check[i] = 1
        maximum = 0
        for i in check:
            if check[i] > maximum:
                maximum = check[i]
                word = i
        return word