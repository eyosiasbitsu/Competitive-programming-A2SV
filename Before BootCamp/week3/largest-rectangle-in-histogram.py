class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        l = []
        r = []
        a = 0
        st = []
        for i in range(len(heights)):
            if not st:
                l.append(0)
                st.append(i)
            else:
                while st and heights[st[-1]] >= heights[i]:                
                    st.pop()        
                if not st:
                    l.append(0)
                else:
                    l.append(st[-1]+1)
                st.append(i)
        st  = []
        l2 = len(heights)-1
        for i in range(l2,-1,-1):
            if not st:
                r.append(l2)
                st.append(i)
            else:
                while st and heights[st[-1]] >= heights[i]:
                    st.pop()
                if not st:
                    r.append(l2)
                else:
                    r.append(st[-1] - 1)
                st.append(i)
        r = r[::-1]
        for i in range(len(heights)):
            tempA = heights[i]*(r[i]-l[i]+1)
            if  tempA >= a:
                a = tempA
        return a