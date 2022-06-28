class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        nums = {2 : ["a","b","c"], 3: ["d","e","f"], 4: ["g","h","i"], 5: ["j","k","l"], 6: ["m","n","o"], 7: ["p","q","r","s"], 8: ["t","u","v"], 9: ["w","x","y","z"]}
        
        res = []
        
        def do_dfs(st, idx):
            if idx == len(digits):
                if st: res.append(st)
                return
            
            for c in nums[int(digits[idx])]:
                do_dfs(st + c,idx+1)
        
        do_dfs("",0)
        return res
                
            
        