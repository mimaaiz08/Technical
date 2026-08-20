class Solution:
    def isHappy(self, n: int) -> bool:
        while n > 9:
            total_sum = 0
            while n > 0:
                digit = n % 10
                total_sum += digit * digit
                n = n // 10
            n = total_sum
        return n == 1 or n == 7
