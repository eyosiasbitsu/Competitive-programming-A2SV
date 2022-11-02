class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        idx = {}
        
        for i in range(len(nums2)):
            idx[nums2[i]] = i
        
        stk = []
        
        for i in range(len(nums2) - 1, -1, -1):
            while stk and nums2[i] > stk[-1]:
                stk.pop()
            
            stk.append(nums2[i])
            if len(stk) > 1:
                nums2[i] = stk[-2]
            
            else:
                nums2[i] = -1
        
        for i in range(len(nums1)):
            nums1[i] = nums2[idx[nums1[i]]]
        
        return nums1
        
        
        
        
        
        
        