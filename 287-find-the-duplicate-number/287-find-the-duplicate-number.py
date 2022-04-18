class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        len1 = len(nums)
        # def _count(n):
        #     count  = 0
        #     for i in range(len1):
        #         if nums[i] <= n:
        #             count += 1
        #     return count
        l = 1
        r = len(nums) - 1
        while l <= r:
            mid = l + (r-l)//2
            count = sum( num <= mid for num in nums)
            if count > mid:
                r = mid - 1
            elif count <= mid:
                l = mid + 1
        return l
    #         \\\\\\\\\
#         \\\\\\\\\
        # val = 0
        # for num in nums:
        #     cur = abs(num)
        #     if nums[cur] < 0:
        #         val = cur
        #         break
        #     else:
        #         nums[cur] *= -1
        # for i in range(len(nums)):
        #     nums[i] = abs(nums[i])
        # return val
        #         \\\\\\\\\
#         \\\\\\\\\
        # def store(nums:List[int],cur:int)-> int:
        #     if cur == nums[cur]:
        #         return cur
        #     nxt = nums[cur]
        #     nums[cur] = cur
        #     store(nums,cur)
        # return store(nums,0)
        #         \\\\\\\\\
#         \\\\\\\\\
        # while nums[0]!=nums[nums[0]]:
        #     nums[nums[0]],nums[0] = nums[0],nums[nums[0]]
        # return nums[0]