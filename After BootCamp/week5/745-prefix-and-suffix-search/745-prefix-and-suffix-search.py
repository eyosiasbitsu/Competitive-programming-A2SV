class trieNode:
    
    def __init__(self):
        self.children = {}
        self.end = False
        self.idx = -1

class trie:
    
    def __init__(self):
        self.root = trieNode()
    
    def add(self,word,i):
        cur = self.root
        cur.idx = i
        
        for c in word:
            if c not in cur.children:
                cur.children[c] = trieNode()
            cur = cur.children[c]
            cur.idx = i

    def search(self,pref,suf):
        temp = suf + "#" + pref
        cur = self.root
        
        for c in temp:
            if c not in cur.children:
                return -1
            cur = cur.children[c]
            
        return cur.idx
    
class WordFilter:

    def __init__(self, words: List[str]):
        self.tr = trie()
        
        for i in range(len(words)):
            word = words[i]
            temp = word + "#" + word
            
            for j in range(len(word)):
                self.tr.add(temp[j:],i)
                
    def f(self, prefix: str, suffix: str) -> int:
        r = self.tr.search(prefix,suffix)
        return r

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)