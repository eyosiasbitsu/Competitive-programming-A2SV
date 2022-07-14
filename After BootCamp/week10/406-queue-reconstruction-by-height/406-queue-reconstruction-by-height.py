class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        l = len(people)
        output = [None]*l
        people.sort()
        
        for h,q in people:
            i,j = 0,-1
            while (i < l):
                if not output[i] or  output[i][0] == h:
                    j += 1
                
                if j == q:
                    break
                
                i += 1
            output[i] = [h,q]
        
        return output