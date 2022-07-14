class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if not matchsticks:
            return False

        L = len(matchsticks)

        perimeter = sum(matchsticks)

        possible_side =  perimeter // 4

        if possible_side * 4 != perimeter:
            return False

        memo = {}

        def recurse(mask, sides_done):

            total = 0
            for i in range(L - 1, -1, -1):
                if not (mask & (1 << i)):
                    total += matchsticks[L - 1 - i]

            if total > 0 and total % possible_side == 0:
                sides_done += 1

            if sides_done == 3:
                return True

            if (mask, sides_done) in memo:
                return memo[(mask, sides_done)]

            ans = False

            c = int(total / possible_side)
            rem = possible_side * (c + 1) - total

            for i in range(L - 1, -1, -1):

                if matchsticks[L - 1 - i] <= rem and mask&(1 << i):

                    if recurse(mask ^ (1 << i), sides_done):
                        ans = True
                        break

            memo[(mask, sides_done)] = ans
            return ans

        return recurse((1 << L) - 1, 0)