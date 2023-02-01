class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:

        for i in range(len(scores)):
            scores[i] = (scores[i], ages[i])
        
        scores.sort()
        dp = [scores[i][0] for i in range(len(scores))]

        for i in range(len(scores)):
            for j in range(i):
                if scores[i][1] >= scores[j][1]:
                    dp[i] = max(dp[i], scores[i][0] + dp[j])
        
        return max(dp)
