class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        
        days = [i for i in range(len(plantTime))] 
        cur_time = 0
        result = 0

        days.sort(key = lambda x: -growTime[x])
        for time in days:
            cur_time += plantTime[time]
            result = max(result, cur_time + growTime[time])
            
        return result
