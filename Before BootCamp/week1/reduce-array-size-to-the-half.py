class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count_dict = Counter(arr)
        x = 0
        result = 0
        for k,v in sorted(count_dict.items(),key = lambda x:-x[1]):
            x += v
            result +=1
            if x >= len(arr)//2:
                break
        return result