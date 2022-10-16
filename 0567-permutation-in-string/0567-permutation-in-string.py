class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        count1 = defaultdict(int)
        for c in s1:
            count1[c] += 1
        
        count2 = defaultdict(int)
        l = 0
        
        for i in range(len(s2)):
            count2[s2[i]] += 1
            while count2[s2[i]] > count1[s2[i]]:
                count2[s2[l]] -= 1
                l += 1
            
            if count2 == count1:
                return True
        
        return False
            