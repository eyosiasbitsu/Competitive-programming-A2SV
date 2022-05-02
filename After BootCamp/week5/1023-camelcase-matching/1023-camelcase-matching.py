class trieNode:
    def __init__(self):
        self.children = {}
        self.end = False

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
    
    def search(self,prefix,pat):
        cur = self.root
        i = 0
        
        for c in prefix:
            if c not in cur.children:
                return False
            
            if i < len(pat) and c == pat[i]:
                i += 1
                
            elif c.isupper():
                return False
            cur = cur.children[c]
            
        return cur.end and i == len(pat)
    
class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        trie1 = trie()
        
        for q in queries:
            trie1.add(q)
            
        for i in range(len(queries)):
            queries[i] = trie1.search(queries[i],pattern)
        
        return queries
        