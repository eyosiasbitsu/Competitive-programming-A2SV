class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def bck(com,count):
            if len(com) == len(nums):
                res.append(list(com))
                return
            
            for n in count:
                if count[n] > 0:
                    com.append(n)
                    count[n] -= 1
                    bck(com,count)
                    
                    com.pop()
                    count[n] += 1
        
        bck([],Counter(nums))
        
        return res