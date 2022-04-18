class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # result = []
        # dict1 = {}
        # heapq.heapify(words)
        # i = 0
        # for i in range(len(words)):
        #     x = heapq.heappop(words)
        #     if x not in dict1:
        #         dict1[x] = 1
        #     dict1[x] += 1
        # sor = sorted(dict1.items(), key = lambda x:-x[1])
        # for i in range(k):
        #     result.append(sor[i][0])
        # return result
        d1 = {}
        result = []
        for char in words:
            if char not in d1:
                d1[char] = 0
            d1[char] -= 1
        l2 = list(d1.items())
        for i in range(len(l2)):
            l2[i] = l2[i][::-1]
        heapq.heapify(l2)     
        for i in range(k):
            result.append(heapq.heappop(l2)[1])
        return result