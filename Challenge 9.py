# 1. Take a number as input
num = int(input("Enter a number: "))

# Store original number
original_num = num

# Function to calculate factorial of a digit
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

sum_of_factorials = 0

# 2, 3 & 4. Extract digits, find factorial, and add
while num > 0:
    digit = num % 10
    sum_of_factorials += factorial(digit)
    num //= 10

# 5 & 6. Compare and print result
if sum_of_factorials == original_num:
    print(f"{original_num} is a Strong Number")
else:
    print(f"{original_num} is not a Strong Number")
