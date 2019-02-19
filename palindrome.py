# Find the largest palindromic number resulting from two n-digit numers

# We'll check for two digit numbers First
palindrome = 0

n = input("Number of digits: ")

for x in range(10**(n-1), 10**n):
    for y in range(10**(n-1), 10**n):
        total = x * y
        if str(total) == str(total)[::-1]:
            if total > palindrome:
                palindrome = total

print(palindrome)
