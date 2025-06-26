import random

def hangman():
    words = ['apple', 'lemon', 'mango', 'grape', 'peach']
    word = random.choice(words)
    guessed = ['_'] * len(word)
    tries = 6
    guessed_letters = []

    print("Welcome to Hangman!")
    print("Word: " + " ".join(guessed))

    while tries > 0 and '_' in guessed:
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct!")
            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess
        else:
            tries -= 1
            print(f"Wrong! You have {tries} guesses left.")

        print("Word: " + " ".join(guessed))

    if '_' not in guessed:
        print("Congratulations! You won!")
    else:
        print(f"You lost! The word was '{word}'.")

if __name__ == "__main__":
    hangman()

