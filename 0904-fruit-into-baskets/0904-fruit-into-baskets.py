class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        left = 0
        _dict = {}
        
        result = 0
        count = 0
        
        for right in range(len(fruits)):
            _dict[fruits[right]] = 1 + _dict.get(fruits[right], 0)
            count += 1
            
            while len(_dict) > 2:
                _dict[fruits[left]] -= 1
                count -= 1
                
                if _dict[fruits[left]] == 0:
                    del _dict[fruits[left]]
                
                left += 1
                
            result = max(count, result)
        
        return result