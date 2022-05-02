class trieNode:
    
    def __init__(self):
        self.children = {}
        self.end = False

class trie:
    
    def __init__(self):
        self.root = trieNode()
    
    def add(self,word):
        cur = self.root
        i = 0
        while i < len(word):
            temp = ""
            
            if word[i] == "/":
                temp = word[i]
                i += 1
            else:
                while i < len(word) and word[i] != "/":
                    temp += word[i]
                    i += 1
                    
            if temp not in cur.children:
                cur.children[temp] = trieNode()
                
            cur = cur.children[temp]
        cur.end = True
    
    def search(self):
        cur = self.root
        res = []
        stk = []
        
        for ch in cur.children:
            node = cur.children[ch]
            stk.append((ch,node))
        
        while stk:
            str1,nxt = stk.pop()
            
            if nxt.end or not nxt.children:
                res.append(str1)
            else:
                for ch in nxt.children:
                    node = nxt.children[ch]
                    stk.append((str1 + ch,node))
        res.sort()
        return res
    
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        tr = trie()
        
        for f in folder:
            tr.add(f)
        
        return tr.search()