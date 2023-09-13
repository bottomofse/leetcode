class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        taiou = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        cur_num = columnNumber
        col_str = ''
        while cur_num > 26:
            idx = cur_num % 26
            if idx == 0:
                col_str = col_str + 'Z'
                cur_num = (cur_num - 1) // 26
            else:
                col_str = taiou[idx - 1] + col_str
                cur_num = cur_num // 26
        col_str = taiou[cur_num - 1] + col_str
        return col_str
