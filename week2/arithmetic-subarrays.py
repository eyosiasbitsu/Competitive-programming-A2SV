class Solution:
    def checkArt(self, l: list[int]) -> bool:
            l.sort()
            st = []
            for i in range(len(l)):
                if len(st) <= 1:
                    st.append(l[i])
                elif st[-1] - st[-2] == l[i] - st[-1]:
                    st.append(l[i])
            if len(st) == len(l):
                return True
            else:
                return False
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        l1 = []
        l2 = []
        for i in range(len(r)):
            l1.append(nums[l[i]:r[i]+1])
        print (l1)
        
        for char in l1:
            l2.append(self.checkArt(char))
        return l2
            
                