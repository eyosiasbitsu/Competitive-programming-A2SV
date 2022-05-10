class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        temp = nums[::]
        temp.sort()
        ar = []
        
        for i in range(len(nums)):
            if nums[i] != temp[i]:
                ar.append(i)
        
        return ar[-1] - ar[0] + 1 if ar else 0
        