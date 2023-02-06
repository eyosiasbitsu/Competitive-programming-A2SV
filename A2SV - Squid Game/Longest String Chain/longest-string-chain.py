class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        word_coll = set(words)
        memo = {}
        
        for word in words:
            self.dp(word, word_coll, memo)
        
        return max(memo.values())
    
    def dp(self, word, word_coll, memo):

        if word not in word_coll:
            return 0

        if word in memo: 
            return memo[word]
        
        _max = 0
        
        for i in range(len(word)):
            sliced_word = word[:i] + word[i+1:]
            
            _max = max(_max,self.dp(sliced_word, word_coll, memo) + 1)
        
        memo[word] = _max
        
        return memo[word]
