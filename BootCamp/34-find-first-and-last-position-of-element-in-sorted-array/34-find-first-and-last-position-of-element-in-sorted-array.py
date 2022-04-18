class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.bs(nums,target,True)
        Right = self.bs(nums,target,False)
        return [left,Right]
    def bs(self,nums,target,toleft):
        l,r = 0, len(nums) - 1
        i = -1
        while l <= r:
            m = (l+r)//2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m -1
            else:
                i = m
                if toleft:
                    r = m -1
                else:
                    l = m + 1
        return i

        