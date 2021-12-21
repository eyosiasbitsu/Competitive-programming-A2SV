class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num = [0]*len(nums2)
        index = []
        for i,j in enumerate(nums2):
            while len(index)!=0 and nums2[index[-1]] < j:
                i1 = index.pop()
                num[i1] = i - i1
            index.append(i)
        for i in range(len(num)):
            num[i] = nums2[num[i]+i]
        result = []
        for x in nums1:
            if num[nums2.index(x)] == x:
                result.append(-1)
            else:
                result.append(num[nums2.index(x)])
        return result   
