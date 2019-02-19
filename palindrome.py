# Find the largest palindromic number resulting from two n-digit numers

# We'll check for two digit numbers First
palindrome = 11

for x in range(100, 1000):
    for y in range(100, 1000):
        total = x * y
        if str(total) == str(total)[::-1]:
            if total > palindrome:
                palindrome = total
print(palindrome)
