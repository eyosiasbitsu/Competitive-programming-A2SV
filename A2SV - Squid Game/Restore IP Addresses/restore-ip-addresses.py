class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        result = []
        self.backTrack(0, 0, "", result, s)
        
        return result

    def backTrack(self, idx, dots, ip, result, s):
        if dots == 4 and idx == len(s):
            result.append("".join(ip[:-1]))
            return 
        
        if dots > 4:
            return
        
        for i in range(idx, min(idx + 3, len(s))):
            if int(s[idx: i + 1]) <= 255 and (idx == i or s[idx] != '0'):
                self.backTrack(i + 1, dots + 1, ip + s[idx: i + 1] + '.', result, s)
            
