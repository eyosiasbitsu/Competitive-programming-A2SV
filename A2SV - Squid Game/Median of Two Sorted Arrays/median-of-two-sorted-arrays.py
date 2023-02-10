# Approach1
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        for n in nums2:
            nums1.append(n)
        
        nums1.sort()
        
        median = -1
        if len(nums1)%2 == 0:
            median = (nums1[len(nums1)//2] + nums1[len(nums1)//2 - 1])/2
        
        else:
            median = nums1[len(nums1)//2]
        
        return median

# Approach2
