class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        self.friq = 0
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def add(self,word):
        cur = self.root
        temp = False
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True
        cur.friq += 1
        
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        trie = Trie()
        cur = trie.root
        
        for w in words:
            trie.add(w)
        
        dict1 = defaultdict(int)
        que = deque()
        str1 = ""
        for c in cur.children:
            temp = str1 + c
            if cur.children[c].end:
                dict1[temp] = cur.children[c].friq
                
            que.append((cur.children[c],temp))
            
        while que:
            cur,word = que.popleft()
            
            for child in cur.children:
                node = cur.children[child]
                w = word + child
                if node.end:
                    dict1[w] = node.friq
                que.append((node,w))
                
        l = sorted(dict1.items(), key = lambda x : x[1],reverse = True)
        ar = []
        for i in range(len(l)):
            heapq.heappush(ar,(-l[i][1],l[i][0]))
        res = []
        
        for i in range(k):
            temp = heapq.heappop(ar)
            res.append(temp[1])
        
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        