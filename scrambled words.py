import random

def scramble_word(word):
    """Scramble the letters of the given word."""
    scrambled = list(word)
    random.shuffle(scrambled)
    return ''.join(scrambled)

def word_scramble_game():
    words = ['python', 'programming', 'code', 'computer', 'developer', 'algorithm', 'function']
    chosen_word = random.choice(words)
    scrambled_word = scramble_word(chosen_word)
    attempts = 3

    print("Welcome to the Word Scramble Game!")
    print(f"Here is the scrambled word: {scrambled_word}")

    while attempts > 0:
        guess = input("Guess the original word: ").strip().lower()
        if guess == chosen_word:
            print("Congratulations! You guessed the word correctly.")
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Incorrect guess. You have {attempts} attempts left.")
            else:
                print(f"Sorry, you've run out of attempts. The correct word was '{chosen_word}'.")

if __name__ == "__main__":
    word_scramble_game()
