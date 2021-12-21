class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        num = [0]*len(temperatures)
        index = []
        for i,j in enumerate(temperatures):
            while len(index)!=0 and temperatures[index[-1]] < j:
                i1 = index.pop()
                num[i1] = i - i1
            index.append(i)
        return num