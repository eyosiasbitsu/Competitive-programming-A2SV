class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        count = defaultdict(int)
        original = []

        for num in changed:
            count[num] += 1
        
        for i in range(len(changed) - 1, -1, -1):
            cur_num = changed[i]
            count[cur_num] -= 1

            if count[cur_num] >= 0 and cur_num%2 == 0 and count[cur_num / 2] != 0:
                count[cur_num//2] -= 1
                original.append(cur_num//2)
            
        if len(original) == len(changed) / 2:
            return original
