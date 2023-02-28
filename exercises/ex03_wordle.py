"""wordle type game."""
__author__ = "730566506"

def contains_char (word: str, letter: str) -> bool:
    """Declares if a provided char is in the provided string"""
    assert len(letter) == 1  # Ensure 'letter' has a length of one
    idx: int = 0
    while idx < len(word):  # Checks to see if 'letter' is in the given word
        if word[idx] == letter:
            return True
        idx = idx + 1
    return False

def emojified (guess: str, secret: str) -> str:
    """returns a string of boxes wordle-esk by repeatedly calling contains_char"""
    assert len(guess) == len(secret)
    ret_str: str = ""
    idx: int = 0
    while idx < len(secret):  # While loops that builds the colored box string
        if(guess[idx] == secret[idx]):  # Adds Green Box
            ret_str = ret_str + "\U0001F7E9"
        elif contains_char(secret, guess[idx]):  # Adds Yellow Box
            ret_str = ret_str + "\U0001F7E8"
        elif not contains_char(secret, guess[idx]):  # Adds White Box
            ret_str = ret_str + "\U00002B1C"
        idx = idx + 1
    return ret_str

def input_guess (expected_len: int) -> str:
    guess: str = str(input(f"Enter a {expected_len} character word: "))
    while len(guess) != expected_len:  # check guesses length is valid
        guess = input(f"That wasn't {expected_len} chars! Try again: ")
    return guess

def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    SECRET: str = "codes"
    playing: bool = True
    while (playing and turn <=6):  # Loop that runs the 6 turns
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(len(SECRET))
        print(emojified(guess, SECRET))
        if (guess == SECRET):  # Way to check if they won
            print(f"You won in {turn}/6 turns!")
            playing = False
        turn = turn + 1
    if (turn >= 6):  # Game loss due to turns runningout
        print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()