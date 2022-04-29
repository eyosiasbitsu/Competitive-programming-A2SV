class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        i = 0
        j = 0
        arr = []
        nums1.sort()
        nums2.sort()
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                print(nums1[i])
                arr.append(nums1[i])
                j += 1
                i += 1
                while j < len(nums2) and nums2[j] == nums2[j-1]:
                    j += 1
                while i < len(nums1) and nums1[i] == nums1[i-1]:
                    i += 1
            else:
                if nums1[i] < nums2[j]:
                    i += 1
                elif nums1[i] > nums2[j]:
                    j += 1
                
        return arr
            