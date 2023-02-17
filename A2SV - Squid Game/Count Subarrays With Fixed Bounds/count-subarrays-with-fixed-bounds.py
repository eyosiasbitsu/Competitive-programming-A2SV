class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        res, i = 0, 0

        while i < n:
            while i < n and (nums[i] < minK or nums[i] > maxK): i += 1
            if i == n: 
                break

            l = i
            while i < n and (nums[i] >= minK and nums[i] <= maxK): 
                i += 1
                last_min, last_max = l - 1, l - 1
                invalid = 0
                cnt = i - l

            while l < i:
                if nums[l] == minK: 
                    last_min = l

                if nums[l] == maxK: 
                    last_max = l

                invalid += l - min(last_max, last_min)
                l += 1

            res += (cnt * (cnt + 1)) // 2 - invalid

        return res
