class node:
    def __init__(self):
        self.children = {}
        self.idx = None
        
class trieNode:
    def __init__(self):
        self.root = node()
    
    def add(self, word,idx):
        cur = self.root
        
        for c in word:
            if c not in cur.children:
                cur.children[c] = node()
            
            cur = cur.children[c]
            cur.idx = idx 
    
    def search(self,word):
        cur = self.root
        
        for c in word:
            if c not in cur.children:
                return -1
            
            cur = cur.children[c]
        
        return cur.idx
        
class WordFilter:

    def __init__(self, words: List[str]):
        self.words = trieNode()
        
        for i in range(len(words)):
            l = len(words[i])
            w =  words[i] + "#" + words[i]
            
            for j in range(l):
                temp = w[j:]
                self.words.add(temp,i)
            
    def f(self, prefix: str, suffix: str) -> int:
        st = suffix + "#" + prefix
        
        return self.words.search(st)


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)