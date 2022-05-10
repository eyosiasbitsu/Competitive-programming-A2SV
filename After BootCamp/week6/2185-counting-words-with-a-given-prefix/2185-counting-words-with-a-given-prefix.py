class trieNode:
    def __init__(self):
        self.children = {}
        self.num = 0

class trie:
    
    def __init__(self):
        self.root = trieNode()
    
    def add(self,word):
        cur = self.root
        
        for c in word:
            if c not in cur.children:
                cur.children[c] = trieNode()
                
            cur = cur.children[c]
            cur.num += 1
    
    def search(self,pref):
        cur = self.root
        
        for c in pref:
            if c not in cur.children:
                return 0
            cur = cur.children[c]
        
        return cur.num
    
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        tr = trie()
        
        for w in words:
            tr.add(w)
        
        return tr.search(pref)
        
        
        