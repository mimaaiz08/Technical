# Reverse Number
```python
n = int(input("Enter the number: "))
rev = 0
while (n!=0):
    rem = n % 10
    rev = (rev * 10) + rem
    n = n // 10
print("Reverse of the number is",rev)
```
## Concepts
- Modulus Operator (%)
- Integer Division (//)
- While Loop

## Problems on Leetcode
7 --- Reverse Integer *(Medium)*  
9 Palindrome Number *(Easy)*  
202 Happy Number / Add Digits *(Easy)*  
1342 Number of Steps to Reduce a Number to Zero *(Easy)*  
2520 Count the Digits That Divide a Number *(Easy)*  
3099 Harshad Number *(Easy)*  


## Complexity
- Reverse Number
- Time: O(log n)
- Space: O(1)
