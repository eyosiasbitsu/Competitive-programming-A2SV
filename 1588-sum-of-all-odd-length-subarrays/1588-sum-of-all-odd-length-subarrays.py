class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        arr.append(0)
        
        ar = [0 for _ in range(len(arr))]
        res = 0
        
        for i in range(len(ar)):
            ar[i] = arr[i - 1] + ar[i - 1]
        
        res = 0
        
        for i in range(len(ar)):
            for j in range(i, len(ar)):
                if (j - i) %2 != 0:
                    res += (ar[j] - ar[i])
        
        return res