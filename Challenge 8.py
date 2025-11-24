# 1. Take input from user
text = input("Enter a string: ")

# 2. Convert to lowercase
text = text.lower()

vowels = "aeiou"
vowel_count = 0
consonant_count = 0

# 3. Loop through each character and count
for char in text:
    if char.isalpha():              # ignore digits, spaces, special chars
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

# 4. Print results
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
