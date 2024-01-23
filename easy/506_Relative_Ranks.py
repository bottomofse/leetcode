class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score,reverse=True)
        score_dic = {}
        if len(sorted_score) >= 1:
            score_dic[sorted_score[0]] = 'Gold Medal'
        if len(sorted_score) >= 2:
            score_dic[sorted_score[1]] = 'Silver Medal'
        if len(sorted_score) >= 3:
            score_dic[sorted_score[2]] = 'Bronze Medal'
        if len(sorted_score) >= 4:
            for i in range(3, len(sorted_score)):
                score_dic[sorted_score[i]] = str(i + 1)
        ret = []
        for i in score:
            ret.append(score_dic[i])
        return ret