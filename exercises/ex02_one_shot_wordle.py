"""One Guess your out wordle type game."""
__author__ = "730566506"

WORD: str = "python"
playing: bool = True
guess: str = str(input(f"What is your {str(len(WORD))}-letter guess? "))
count_of_guesses: int = 0
char_check: int = 0
boxes: str = ""

while playing:

    while len(guess) != len(WORD):  # check guesses length is valid
        guess = str(input(f"that was not {str(len(WORD))} letters! try again "))
        count_of_guesses = count_of_guesses + 1

    while char_check < len(WORD):  # creates the colored boxes that you'll see
        if (guess[char_check] == WORD[char_check]):  # green box
            boxes = boxes + "\U0001F7E9"
        if (guess[char_check] != WORD[char_check]):  # non-green box
            yellow_box: bool = False
            yellow_check: int = 0
            while not yellow_box and yellow_check < len(WORD):  # loop that determines box white/yellow
                if guess[char_check] == WORD[yellow_check]:
                    yellow_box = True
                yellow_check = yellow_check + 1
            if yellow_box:
                boxes = boxes + "\U0001F7E8"
            else:
                boxes = boxes + "\U00002B1C"
        char_check = char_check + 1
    print(boxes)
    if guess == WORD:  # correct guess
        print("Woo! You got it!")
        playing = False
    if guess != WORD:  # incorrect VALID guess
        print("Not quite. Play again soon!")
        playing = False
    
    # resetting variables in order for a player to have multiple guesses (currently unused)
    char_check = 0
    boxes = ""