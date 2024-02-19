class Solution:
    def judgeCircle(self, moves: str) -> bool:
        check = {'U':0, 'D':0, 'L':0, 'R':0}
        for i in range(len(moves)):
            check[moves[i]] += 1
        return (check['U'] == check['D']) and (check['L'] == check['R'])