class TreeNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:

    def __init__(self):
        self.root = TreeNode()

    def add(self, word: str) -> None:
        cur = self.root
        
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

class MapSum:

    def __init__(self):
        self.map = defaultdict(int)
        self.trie = Trie()
        
    def insert(self, key: str, val: int) -> None:
        self.map[key] = val
        self.trie.add(key)

    def sum(self, prefix: str) -> int:
        ar = self.trie.startsWith(prefix)
        n = 0
        
        for i in ar:
            n += self.map[i]
        return n



# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)