class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        count1 = 1
        count2 = 1
        nums.sort()
        finalarr = [0]*len(nums)
        n = len(nums)//2 + len(nums)%2
        newarr1 = nums[:n]
        newarr2 = nums[n:len(nums)]
        for i in range(len(nums)):
            if i == 0:
                finalarr[i] = newarr1[i]
                continue
            elif i%2 != 0:
                finalarr[i] = newarr2[i-count1]
                count1 += 1
            elif i%2 == 0:
                finalarr[i] = newarr1[i-count2]
                count2 += 1
        return finalarr
