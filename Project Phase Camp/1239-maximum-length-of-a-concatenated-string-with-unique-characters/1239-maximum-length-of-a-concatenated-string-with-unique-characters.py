class Solution:
    def maxLength(self, sequences: List[str]) -> int:
        dp = [set()]

        for seq in sequences:
            chars = set(seq)

            if len(chars) < len(seq):
                continue

            dp.extend(chars | other for other in dp if not (chars & other))

        return max(map(len, dp))