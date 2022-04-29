class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self,word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True
        
class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for w in words:
            trie.add(w)
            
        que = deque()
        cur = trie.root
        str1 = ""
        temp = []
        for c in cur.children:
            if cur.children[c].end:
                que.append((cur.children[c],str1+c))
                
        while que:
            temp = []
            for i in range(len(que)):
                car,word = que.popleft()
                heapq.heappush(temp,word)

                for child in car.children:
                    if car.children[child].end:
                        que.append((car.children[child],word+child))

        return temp[0] if temp else ""
        
        
        
        
        