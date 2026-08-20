# Day 1 - Reverse Number

## Reverse Number

```python
n = int(input("Enter the number: "))
rev = 0

while n != 0:
    rem = n % 10
    rev = rev * 10 + rem
    n //= 10

print("Reverse of the number is", rev)
```

---

## Concepts Learned

- Modulus Operator (`%`)
- Integer Division (`//`)
- While Loop
- Digit Extraction
- Building a Number Digit by Digit

---

## Interview Pattern

### Extract the Last Digit

```python
digit = n % 10
```

### Remove the Last Digit

```python
n //= 10
```

### Build the Answer

```python
ans = ans * 10 + digit
```

These three operations form the basic pattern for many digit manipulation problems.

---

## LeetCode Practice

| # | Problem | Difficulty | Status |
|---|---------|------------|--------|
| 7 | Reverse Integer | Medium | ⏳ |
| 9 | Palindrome Number | Easy | ✅ |
| 202 | Happy Number | Easy | ⏳ |
| 258 | Add Digits | Easy | ⏳ |
| 1342 | Number of Steps to Reduce a Number to Zero | Easy | ✅ |
| 2520 | Count the Digits That Divide a Number | Easy | ✅ |
| 3099 | Harshad Number | Easy | ⏳ |

---

## Complexity

**Time Complexity:** `O(log n)`

**Space Complexity:** `O(1)`

---

## Key Takeaways

- Extract a digit using `%`.
- Remove the last digit using `//`.
- Build a number using `ans = ans * 10 + digit`.
- Digit manipulation is a common pattern in coding problems.
- The same digit-extraction technique can be reused for problems involving reversing, counting, summing, or analyzing digits.
