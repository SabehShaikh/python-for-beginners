# function that counts the number of vowels in a given string text
# the function should be case-insensitive and count both lowercase and uppercase vowels. 
# Return the total number of vowels found in the string.
# Test the func with a sentence or a word.


def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count


text = input("Enter a text: ")
vowel_count = count_vowels(text)
print(f"Number of vowels: {vowel_count}")
