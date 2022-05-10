class trieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        self.count = 0

class trie:
    
    def __init__(self):
        self.root = trieNode()
    
    def add(self,word):
        cur = self.root
        
        for c in word:
            if c not in cur.children:
                cur.children[c] = trieNode()
                
            cur = cur.children[c]
        
        cur.end = True
        cur.count += 1
    
    def search(self,pref):
        cur = self.root
        num = 0
        
        for c in pref:
            if c not in cur.children:
                return num
            cur = cur.children[c]
            
            if cur.end:
                num += cur.count
        
        return num
    
class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        
        tr = trie()
        
        for w in words:
            tr.add(w)
        
        return tr.search(s)