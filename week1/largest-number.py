class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def largest(a,b):
            if a + b < b + a:
                return 1
            else:
                return 0
        for x in range(len(nums)-1,-1,-1):
            for y in range(x):
                if largest(str(nums[y]),str(nums[y+1])):
                    nums[y],nums[y+1] = nums[y+1],nums[y]
        a = int("".join(map(str,nums)))
        return str(a)