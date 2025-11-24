# 1. Take input from the user
start = int(input("Enter start value: "))
end = int(input("Enter end value: "))

found_prime = False

# 2 & 3. Loop through range and check prime numbers
for num in range(start, end + 1):
    if num > 1:  # primes start from 2
        is_prime = True

        # check divisors from 2 to sqrt(num)
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            print(num)
            found_prime = True

# 4. If no primes found
if not found_prime:
    print("No prime numbers in this range")
