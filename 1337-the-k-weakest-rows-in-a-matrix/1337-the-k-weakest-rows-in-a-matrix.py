class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ar = []
        for i in range(len(mat)):
            temp = 0
            j = 0
            while j < len(mat[i]) and mat[i][j]!= 0:
                temp += 1
                j += 1
            heapq.heappush(ar,[temp,i])
        # print(ar)
        result = []
        while ar and k > 0:
            k -= 1
            result.append(heapq.heappop(ar)[1])
        return result