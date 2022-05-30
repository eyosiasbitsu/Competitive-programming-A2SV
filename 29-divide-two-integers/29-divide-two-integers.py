class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if abs(divisor) > abs(dividend):
            return 0

        positive = (divisor > 0 and dividend > 0) or (divisor < 0 and dividend < 0)

        if abs(divisor) == abs(dividend):
            return 1 if positive else -1

        ans = 0
        dividend = abs(dividend)
        divisor = abs(divisor)

        if divisor > 1:
            while dividend >= divisor:
                tempDivisor = divisor
                multiple = 1
                while dividend >= tempDivisor:
                    dividend -= tempDivisor
                    ans += multiple
                    multiple = multiple << 1
                    tempDivisor = tempDivisor << 1
        else:
            ans = dividend

        if not positive:
            ans = -ans

        ans = max(-2 ** 31, ans)
        ans = min(ans, 2 ** 31 - 1)

        return ans