class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dic = {}
        common = [[] for i in range(2010)]
        for idx, val in enumerate(list1):
            dic[val] = idx
        for idx, val in enumerate(list2):
            if val in dic:
                common[dic[val] + idx] += [val]
            else:
                dic[val] = idx
        ret = []
        for i in common:
            if i:
                return i