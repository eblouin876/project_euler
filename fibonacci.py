from numpy import math
# Find the sum of the even numbers in the Fibonacci sequence by considering
# the terms whose values do not exceed 4 million

# Define the fibonacci sequence
fib_nums = [1, 2]
while fib_nums[-1] < 4000000:
    x = fib_nums[-1] + fib_nums[-2]
    if (x > 4000000):
        break
    else:
        fib_nums.append(x)

# sum all evens
sum = 0
for each in fib_nums:
    if each % 2 == 0:
        sum += each
print(sum)
