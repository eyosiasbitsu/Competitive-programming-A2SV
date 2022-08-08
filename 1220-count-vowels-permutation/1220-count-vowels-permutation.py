class Solution:
    def countVowelPermutation(self, n: int) -> int:
        v_dic = {'a': ['e'], 'e': ['a', 'i'], 'i':['a', 'e', 'o', 'u'],
                'o':['i', 'u'], 'u':['a']}
        @cache
        def search(n, v):
            num = 0
            if n == 1:
                return 1
            next_v_lst = v_dic[v]
            for next_v in next_v_lst:
                num += search(n-1, next_v)
            return num
        return sum([search(n, v) for v in v_dic]) % (10**9+7)
    
    
    
    
    