class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total_time = 0
        
        for i in range(len(timeSeries)):
            if i == len(timeSeries) - 1:
                total_time += duration
                continue
            if timeSeries[i] + duration <= timeSeries[i + 1]:
                total_time += duration
            else:
                total_time += timeSeries[i + 1] - timeSeries[i]
        return total_time
