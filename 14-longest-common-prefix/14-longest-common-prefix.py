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
    
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        tr = trie()
        
        for w in strs:
            tr.add(w)
            
        temp = tr.root

        return self.dfs(temp,"")
    
    
    def dfs(self,node,st):
        if len(node.children) > 1 or node.end == True:
            print(st)
            return st
        
        for c in node.children:
            return self.dfs(node.children[c], st+c)