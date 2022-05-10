class trieNode:
    def __init__(self):
        self.children = {}
        self.idx = -1

class trie:
    
    def __init__(self):
        self.root = trieNode()
    
    def add(self,word,idx):
        cur = self.root
        
        for c in word:
            if c not in cur.children:
                cur.children[c] = trieNode()
                cur.children[c].idx = idx
            cur = cur.children[c]
    
    def search(self,pref):
        cur = self.root
        
        for c in pref:
            if c not in cur.children:
                return -1
            cur = cur.children[c]
        
        return cur.idx
        
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        ar = sentence.split(" ")
        
        tr = trie()
        
        for i in range(len(ar)):
            tr.add(ar[i],i+1)
        
        return tr.search(searchWord)