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
    
    def search(self):
        cur = self.root
        stk = [(cur,"")]
        
        while stk:
            nxt,temp = stk.pop()
            
            if len(nxt.children) > 1 or nxt.end:
                return temp
            
            for c in nxt.children:
                node = nxt.children[c]
                
                stk.append((node,temp + c))
        
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        tr = trie()
        
        for w in strs:
            if not w:
                return ""
            tr.add(w)
        
        return tr.search()
