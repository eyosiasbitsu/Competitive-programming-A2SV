class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        pairedarr = [0]*(len(nums)//2)
        n = len(nums)//2
        arr1 = nums[:n]
        arr2 = nums[n:]
        for i in range(n):
            pairedarr[i] = arr1[i] + arr2[n-i-1]
        pairedarr.sort()           
        return pairedarr[n-1]
            
