class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums2 = map(int, nums)
        nums3 = list(nums2) 
        nums3.sort()
        nums4 = map(str, nums3)
        nums5 = list(nums4)
        return nums5[len(nums3)-k]
