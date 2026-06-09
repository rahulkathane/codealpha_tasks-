import random

# ── Hangman ASCII art (0 = no mistakes, 6 = game over) ──────────────────────
HANGMAN = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========""",
]

# ── Word list ────────────────────────────────────────────────────────────────
WORDS = ["python", "rocket", "jungle", "castle", "breeze"]

MAX_WRONG = 6


def display_state(hidden: list, wrong: list, attempts_left: int) -> None:
    """Print the current game state."""
    print(HANGMAN[MAX_WRONG - attempts_left])
    print(f"\n  Word:  {' '.join(hidden)}")
    if wrong:
        print(f"  Wrong guesses ({len(wrong)}/{MAX_WRONG}): {', '.join(sorted(wrong))}")
    else:
        print(f"  Wrong guesses (0/{MAX_WRONG}): —")
    print(f"  Attempts left: {attempts_left}\n")


def get_guess(guessed: set) -> str:
    """Prompt the player for a valid, unused letter."""
    while True:
        guess = input("  Guess a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("  ⚠  Please enter a single letter.\n")
        elif guess in guessed:
            print(f"  ⚠  You already guessed '{guess}'. Try another.\n")
        else:
            return guess


def play_game() -> None:
    """Run one round of Hangman."""
    word = random.choice(WORDS)
    hidden = ["_"] * len(word)   # letters to reveal
    wrong: list[str] = []        # incorrect guesses
    guessed: set[str] = set()    # all guesses so far
    attempts_left = MAX_WRONG

    print("\n" + "=" * 40)
    print("       W E L C O M E  T O  H A N G M A N")
    print("=" * 40)
    print(f"  The word has {len(word)} letters. Good luck!\n")

    # ── Main game loop ───────────────────────────────────────────────────────
    while attempts_left > 0 and "_" in hidden:
        display_state(hidden, wrong, attempts_left)

        guess = get_guess(guessed)
        guessed.add(guess)

        if guess in word:
            # Reveal every occurrence of the guessed letter
            for i, letter in enumerate(word):
                if letter == guess:
                    hidden[i] = guess
            print(f"  ✔  '{guess}' is in the word!\n")
        else:
            wrong.append(guess)
            attempts_left -= 1
            print(f"  ✘  '{guess}' is NOT in the word.\n")

    # ── Result ───────────────────────────────────────────────────────────────
    display_state(hidden, wrong, attempts_left)

    if "_" not in hidden:
        print("  🎉  You WON! Great job!\n")
    else:
        print(f"  💀  You lost! The word was: '{word.upper()}'\n")


def main() -> None:
    """Entry point — supports multiple rounds."""
    while True:
        play_game()
        again = input("  Play again? (y/n): ").strip().lower()
        if again != "y":
            print("\n  Thanks for playing Hangman! Goodbye. 👋\n")
            break


if __name__ == "__main__":
    main()
