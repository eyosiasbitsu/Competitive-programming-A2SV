class Solution:
    def numberOfWays(self, s: str) -> int:
        
        count = {
                  "1" : 0,
                  "0" : 0,
                  "10" : 0,
                  "01" :  0
                }
        
        result = 0
        for i in range(len(s)):
            if s[i] == "1":
                count["01"] += count["0"]
                result += count["10"]

            elif s[i] == "0":
                count["10"] += count["1"]
                result += count["01"]

            count[s[i]] += 1
        
        return result
