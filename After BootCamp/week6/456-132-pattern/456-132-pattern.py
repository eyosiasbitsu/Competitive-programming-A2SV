class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stk = []
        m = nums[0]

        for n in nums[1:]:
            while stk and n >= stk[-1][0]:
                stk.pop()
            
            if stk and n > stk[-1][1]:
                return True
            
            stk.append([n,m])
            m = min(m,n)
            
        return False