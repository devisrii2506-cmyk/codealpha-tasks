import random

# Dictionary with categories and words
word_categories = {
    "Animals": ["tiger", "elephant", "giraffe", "kangaroo"],
    "Fruits": ["apple", "banana", "mango", "orange"],
    "Countries": ["india", "canada", "brazil", "japan"],
    "Sports": ["cricket", "football", "tennis", "hockey"]
}

# Choose random category and word
category = random.choice(list(word_categories.keys()))
chosen_word = random.choice(word_categories[category])

# Number of attempts
lives = 3

print(" Welcome to Word Guess Game!")
print("Category:", category)
print("Total no. of lives:", lives)

# Game loop
while lives > 0:

    guess = input("\nGuess the word: ").lower()

    # Correct guess
    if guess == chosen_word:
        print("Correct! You guessed the word:", chosen_word)
        break

    # Wrong guess
    else:
        lives -= 1
        print(" Wrong guess!")
        print("Lives left:", lives)

# If user loses
if lives == 0:
    print("\n Game Over! The word was:", chosen_word)