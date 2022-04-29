class TreeNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:

    def __init__(self):
        self.root = TreeNode()
        self.set = set()
    def add(self, word: str) -> None:
        cur = self.root
        self.set.add(word)
        for c in word:
            if c not in cur.children:
                cur.children[c] = TreeNode()
            cur = cur.children[c]
        
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.root
        
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        
        return cur.end

    def startsWith(self, prefix: str) -> list:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return []
            cur = cur.children[c]
            
        res = []
        que = deque()
        if prefix in self.set:
            res.append(prefix)
            
        for c in cur.children:
            node = cur.children[c]
            if node.end:
                res.append(prefix + c)
                
            que.append((prefix + c,node))
            
        while que:
            word,nxt = que.popleft()
            
            if not nxt:
                res.append(word)
                
            else:
                for child in nxt.children:
                    node = nxt.children[child]
                    
                    if node.end:
                        res.append(word+child)
                        
                    que.append((word+child,node))
        return res
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        out = []
        trie = Trie()
        
        for w in products:
            trie.add(w)
        s = ""
        for w in searchWord:
            s += w
            temp = trie.startsWith(s)
            temp.sort()
            if len(temp) > 3:
                temp = temp[:3]
            out.append(temp)
        return out