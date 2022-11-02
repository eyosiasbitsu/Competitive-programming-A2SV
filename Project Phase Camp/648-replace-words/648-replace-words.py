
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.trie = TrieNode()
    
    def add(self, word):
        cur = self.trie
        
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            
            cur = cur.children[c]
        
        cur.end = True
    
    def search(self, word):
        cur = self.trie
        st = ""
        
        for c in word:
            if c not in cur.children:
                break
                
            st += c
            cur = cur.children[c]
            
            if cur.end:
                return st
        
        return word
    
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        ar = []
        
        temp = ""
        
        for c in sentence:
            if c == " ":
                ar.append(temp)
                temp = ""
            
            else:
                temp += c
        
        ar.append(temp)
        
        res = ""
        
        trie = Trie()
        
        for w in dictionary:
            trie.add(w)
        
        for w in ar:
            res += trie.search(w)
            res += " "
            
        return res[:-1]
        
        
        
        
        
        