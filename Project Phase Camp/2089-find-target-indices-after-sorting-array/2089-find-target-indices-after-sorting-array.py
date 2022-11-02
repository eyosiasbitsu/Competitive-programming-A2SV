class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
#         first sort the array, you can use buble sort or merge sort or selection sort or insertion sort
#         let's just use the built in sort function since we've agreed on the sorting part

        nums.sort()
    
        l = 0
        
        for i in range(len(nums)):
            if nums[i] == target:
                nums[l] = i
                l += 1
        
        return nums[:l]
