class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        k = 0
        newr = nums1[:m]
        
        while (i < len(newr) and j < len(nums1)
               and k < len(nums2)):
            if newr[i] < nums2[k]:
                nums1[j] = newr[i]
                i += 1
                j += 1
            elif newr[i] >= nums2[k]:
                nums1[j] = nums2[k]
                k += 1
                j += 1
        while i < len(newr):
            nums1[j] = newr[i]
            i += 1
            j += 1
        
        while k < len(nums2):
            nums1[j] = nums2[k]
            j += 1
            k += 1