class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sum_d = 0
        real_x = x
        while (x!=0):
            sum_d += (x % 10)
            x = x // 10
        if real_x % sum_d == 0:
            return sum_d
        else:
            return -1
