class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @cache
        def dp(i, prev, prev_cnt, k):
            # set it to inf as we will take the min later
            if k < 0: return inf
            # we delete all characters, return 0
            if i == len(s): return 0
            delete = dp(i + 1, prev, prev_cnt, k - 1)
            
            if s[i] == prev:
                # e.g. a2 -> a3
                keep = dp(i + 1, prev, prev_cnt + 1, k)
                
                if prev_cnt in [1, 9, 99]:
                    keep += 1
            else:
                # e.g. a
                keep = dp(i + 1, s[i], 1, k) + 1
            return min(delete, keep)
        
        return dp(0, "", 0, k)