class Solution: 
    def select(self, arr, i):
        minindex = i
        for num in range(i,len(arr)):
            if arr[num] < arr[minindex]:
                minindex = num
        return minindex
        
    def selectionSort(self, arr,n):
        for n in range(len(arr)):
            x = self.select(arr,n)
            arr[n], arr[x] = arr[x],arr[n]
        return arr
