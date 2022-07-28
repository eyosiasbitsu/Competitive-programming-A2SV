class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        dict1 = {}
        
        for i in range(len(boxes)):
            if boxes[i] == '1':
                dict1[i] = 1
        
        res = []
        
        for i in range(len(boxes)):
            temp = 0
            
            for c in dict1:
                temp += abs(i - c)
                
            res.append(temp)
        
        return res