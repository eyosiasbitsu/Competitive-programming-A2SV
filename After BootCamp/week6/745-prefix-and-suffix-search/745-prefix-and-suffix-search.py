class trieNode:
    def __init__(self):
        self.children = {}
        self.idx = -1

class trie:
    
    def __init__(self):
        self.root = trieNode()
        
    def add(self, word, i):
        cur = self.root
        
        for c in word:
            if c not in cur.children:
                cur.children[c] = trieNode()
                
            cur.idx = i
            cur = cur.children[c]
            cur.idx = i
    
    def search(self,pref,suf):
        word = suf + "#" + pref
        cur = self.root
        
        for c in word:
            if c not in cur.children:
                return -1
            
            cur = cur.children[c]
        
        return cur.idx
        
class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = trie()
        
        for i in range(len(words)):
            w = words[i] + "#" + words[i]
            
            for j in range(len(words[i])):
                self.trie.add(w[j:],i)

    def f(self, prefix: str, suffix: str) -> int:
        return self.trie.search(prefix,suffix)


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)