class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = [0]*len(nums)
        arr1 = [nums[0]]
        output = [0]*len(nums)
        c = Counter(nums)
        sor = sorted(c.items(), key = lambda x:-x[1])
        result = []
        for i in range(k):
            result.append(sor[i][0])
        return result