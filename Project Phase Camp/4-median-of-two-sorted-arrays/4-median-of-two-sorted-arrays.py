class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a,b = nums1,nums2
        
        if len(a) > len(b):
            a,b = b,a
        
        total = len(a) + len(b)
        half = total//2
        
        l,r = 0, len(a) - 1
        
        while True:
            ma = (l + r)//2
            mb = half - ma - 2
            
            aleft = a[ma] if ma >= 0 else float("-inf")
            bleft = b[mb] if mb >= 0 else float("-inf")
            
            aright = a[ma + 1] if ma + 1 < len(a) else float("inf")
            bright = b[mb + 1] if mb + 1 < len(b) else float("inf")
            
            if aleft <= bright and aright >= bleft:
                if total % 2 != 0:
                    return min(aright, bright)
                
                return (min(aright,bright) + max(aleft, bleft)) / 2
            
            elif aleft > bright:
                r = ma - 1
            
            else:
                l = ma + 1