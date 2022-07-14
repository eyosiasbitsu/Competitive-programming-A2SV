class Node:
    def __init__(self):
        self.children = {}
        self.end = False
    
class Trie:
    def __init__(self):
        self.root = Node()
    
    def add(self,word):
        cur = self.root
        
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            
            cur = cur.children[c]
        
        cur.end = True
    
    def search(self):
        stk = []
        res = ""
        cur = self.root
        
        for c in cur.children:
            node = cur.children[c]
            
            stk.append((c,node))
        
        while stk:
            st,nxt = stk.pop()
            
            if not nxt.children:
                res += st
                res += "#"
            
            for c in nxt.children:
                node = nxt.children[c]
                stk.append((st + c,node))
        
        return len(res)

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie = Trie()
        
        for w in words:
            trie.add(w[::-1])
        
        return trie.search()
        
        
        