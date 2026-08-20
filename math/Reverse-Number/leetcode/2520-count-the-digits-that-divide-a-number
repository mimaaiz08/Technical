class Solution:
    def countDigits(self, num: int) -> int:
        n = num
        count = 0
        while (num!=0):
            rem = num % 10
            num = num // 10
            if n % rem == 0:
                count +=1
        return count
