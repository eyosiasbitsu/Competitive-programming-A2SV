class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = {}
        dict2 = {}
        dictf = {}
        
        for i in nums1:
            if i not in dict1:
                dict1[i] = 0
            dict1[i] += 1
        
        for i in nums2:
            if i not in dict2:
                dict2[i] = 0
            dict2[i] += 1
        
        for i in dict1:
            if i in dict2:
                dictf[i] = min(dict1[i],dict2[i])
        arr = []
        print(dictf)
        for i in dictf:
            for j in range(dictf[i]):
                arr.append(i)
                
        return arr