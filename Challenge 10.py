# 1. Take integer input
num = int(input("Enter a number: "))

# Store original number for comparison
original_num = num

# 2. Find number of digits
digits = len(str(num))

# 3 & 4. Extract digits, raise to power, and sum
sum_of_powers = 0

while num > 0:
    digit = num % 10               # extract last digit
    sum_of_powers += digit ** digits  # raise to the power of total digits
    num //= 10                     # remove last digit

# 5 & 6. Compare and print result
if sum_of_powers == original_num:
    print(f"{original_num} is an Armstrong Number")
else:
    print(f"{original_num} is NOT an Armstrong Number")
