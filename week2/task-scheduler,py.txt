class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        L1 = sorted(c.items(), key = lambda x:-x[1])
        result = []
        x = L1[0][1] + (L1[0][1]-1)*n
        if n == 0:
            y = 0
            for char in L1:
                y += char[1]
            return y
        for char in L1:
            if (char!= L1[0]) and (char[1] == L1[0][1]):
                x += 1
        return max(x,len(tasks))
        