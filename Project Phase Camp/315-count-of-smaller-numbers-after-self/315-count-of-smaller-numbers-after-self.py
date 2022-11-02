from sortedcontainers import SortedList

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        s = SortedList()
        res = []
        
        for n in nums[::-1]:
            ans = SortedList.bisect_left(s,n)
            res.append(ans)
            s.add(n)
        
        return reversed(res)