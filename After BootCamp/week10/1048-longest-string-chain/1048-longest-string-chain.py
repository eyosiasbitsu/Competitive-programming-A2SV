class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        self.w = set(words)
        memo = {}
        
        def rec(word):
            if word not in self.w: return 0
            if word in memo: return memo[word]
            
            mx = 0
            
            for i in range(len(word)):
                w = word[:i] + word[i+1:]
                
                mx = max(mx,rec(w) + 1)
            
            memo[word] = mx
            
            return mx
        
        for word in words:
            rec(word)
        
        return max(memo.values())