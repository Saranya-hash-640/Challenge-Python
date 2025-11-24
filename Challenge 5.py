# Take password input from the user
password = input("Enter your password: ")

# Initialize flags for each condition
has_upper = False
has_lower = False
has_digit = False
has_special = False

# List of allowed special characters
special_chars = ['@', '#', '$', '%', '&', '*']

# Check each character in the password
for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    elif char in special_chars:
        has_special = True

# Check password length
if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
    print("Strong Password")
else:
    print("Weak Password")
