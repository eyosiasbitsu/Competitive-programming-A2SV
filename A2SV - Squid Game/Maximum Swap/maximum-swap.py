class Solution:
    def maximumSwap(self, num: int) -> int:

        arr = list(map(int, list(str(num))))
        
        descending = True
        prev = sys.maxsize
        
        changeIdx = -1
        for idx, n in enumerate(arr):
            if n > prev:
                descending = False
                changeIdx = idx - 1
                break
            prev = n

        if descending:
            return num

        maxIdx = changeIdx + 1
        for idx in range(changeIdx, len(arr)):
            if arr[idx] >= arr[maxIdx]:
                maxIdx = idx
        
        while changeIdx - 1 >= 0 and arr[changeIdx-1] < arr[maxIdx]:
            changeIdx -= 1
    
        arr[maxIdx], arr[changeIdx] = arr[changeIdx], arr[maxIdx]
        
        return int(''.join([str(x) for x in arr]))
