"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730566605"

word: str = input("Enter a 5-character word:")

if (len (word) != 5):
    print("Error: Word must contain 5 characters")
    exit()

char: str = input("Enter a single character:")
count: int = 0

if (len(char) != 1):
    print("Error: Character must be a single character")
    exit()

print("Searching for " + char + " in " + str(word))

if (char == word[0]):
    print(char + " found at index 0")
    count = count + 1

if (char == word[1]):
    print(char + " found at index 1")
    count = count + 1

if (char == word[2]):
    print(char + " found at index 2")
    count = count + 1

if (char == word[3]):
    print(char + " found at index 3")
    count = count + 1

if (char == word[4]):
    print(char + " found at index 4")
    count = count + 1

if (count > 1):
    print(str(count) + " instances of " + char + " found in " + word)
elif (count == 1):
    print(str(count) + " instance of " + char + " found in " + word)
else:
    print("No instances of " + char + " found in " + word)