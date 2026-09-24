import random

words = ["python", "code", "alpha", "program", "developer"]

word = random.choice(words)

guessed_letters = []

incorrect_guesses = 0
max_guesses = 6

print("-----HANGMAN GAME-----")
print("Guess the word")
print("You only have 6 tries")

while incorrect_guesses < max_guesses:
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"
    print("\nWord: ", display_word)

    if "_" not in display_word:
        print("Congratulations!!")
        print("You guessed correctly")
        break

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("correct guess!")
    else:
        incorrect_guesses += 1
        print("Wrong guess")
        print("Incorrect guesses: ", incorrect_guesses, "/", max_guesses)
else:
    print("\nGame Over!")
    print("The word was: ", word)