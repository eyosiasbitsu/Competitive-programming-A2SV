class trieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class trie:
    
    def __init__(self):
        self.root = trieNode()
        self.l = 0
    def add(self,word):
        cur = self.root
        
        for c in word:
            if c not in cur.children:
                cur.children[c] = trieNode()
            cur.end = False
            cur = cur.children[c]
            
        cur.end = True
        
    def search(self):
        cur = self.root
        stk = [] # goint to hold a tuple (string,node)
        
        final = ""
        for c in cur.children:
            node = cur.children[c]
            stk.append((c,node))
            
        while stk:
            str1,nxt = stk.pop()
            if not nxt.children:
                final += str1
                final += "#"
                
            for ch in nxt.children:
                temp = nxt.children[ch]
                stk.append((str1+ch,temp))
                
        return len(final)
        
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        tr = trie()
        for word in words:
            tr.add(word[::-1])
            
        return tr.search()