# Initialize the string
input_string = "Python Programming"

# Define vowels and consonants
vowels = 'aeiouAEIOU'
consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'

# Initialize counters
vowel_count = 0
consonant_count = 0

# Loop through the string and count vowels and consonants
for char in input_string:
    if char in vowels:
        vowel_count += 1
    elif char in consonants:
        consonant_count += 1

# Print the counts
print(f"Vowels: {vowel_count}")
print(f"Consonants: {consonant_count}")