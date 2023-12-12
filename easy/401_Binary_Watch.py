import itertools
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if turnedOn == 0:
            return ['0:00']
        if turnedOn >= 9:
            return []
        hour_mask = 0b1111000000
        minute_mask = 0b0000111111
        bit_list = [0b1000000000,0b100000000,0b10000000,0b1000000,0b100000,0b10000,0b1000,0b100,0b10,0b1]
        result = []
        for comb in itertools.combinations(bit_list, turnedOn):
            hour = 0
            for i in comb:
                hour = hour | ((i & hour_mask) >> 6)
            minute = 0
            for i in comb:
                minute = minute | (i & minute_mask)
            if hour > 11 or minute > 59:
                continue
            tmp = str(hour) + ':' + ('0' + str(minute))[-2:]
            result.append(tmp)
        return result
