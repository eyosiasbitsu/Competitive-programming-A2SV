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
        
    def search(self,pref):
        cur = self.root
        res = ""
        
        for c in pref:
            if c not in cur.children:
                return ""
            
            res += c
            cur = cur.children[c]
            
            if cur.end:
                return res
            
        return ""

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        tr = trie()
        
        for w in dictionary:
            tr.add(w)
        
        sent = ""
        i = 0
        
        while i < len(sentence):
            temp = ""
            
            while i < len(sentence) and sentence[i].isalpha():
                temp += sentence[i]
                i += 1
            while i < len(sentence) and not sentence[i].isalpha():
                i += 1
            st = tr.search(temp)
            if st:
                sent += st
            else:
                sent += temp
                
            sent += " "
            
        return sent[:-1]
        
        
        
        
        
        
        
        
        