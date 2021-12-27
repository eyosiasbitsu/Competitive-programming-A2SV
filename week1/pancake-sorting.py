class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        count = len(arr)
        result = []
        while count > 1:
            idx = arr.index(count)
            result.append(idx+1)
            arr[0:idx+1] = arr[0:idx+1][::-1]
            arr[0:count] = arr[0:count][::-1]
            result.append(count)
            count -= 1           
        return result
            