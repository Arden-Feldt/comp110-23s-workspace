"""Sink CYOA Story."""
import random

points: int
player: str
CONSTANT: str = "\u2665"


def greet() -> None:
    """Welcomes the player to the game."""
    global player
    print(f"Howdy\nWelcome to the sink. As a bubble, do your best to survive {CONSTANT}")
    player = input("What's your name: ")


def sud():
    """Sud Action."""
    global points
    global player
    add_soap: bool = True
    count_of_soap: int = 0
    while add_soap:
        soap: str = input("Would you like to add soap to sud? (Y/N)")
        if (soap == "Y"):
            count_of_soap += 1
            how_much_soap: int = int(input("How many squeezes of soap are you adding? (1-10)"))
            points += how_much_soap
            print(f"{player}, WOW - that is bubbly")
        else:
            add_soap = False
    sud: str = input("You ready to sud? (Y)")
    if (sud == "Y"):
        print("o O o O o O o\no O o O o O o\no O o O o O o")
    points += (10 + (count_of_soap * (random.randint(1, 3))))
    print(f"You now have {points} points")


def move(pts: int) -> int:
    """Move Action."""
    action: int = int(input("\nWould you like move towards? (enter your answer as a number)\n1) The dirty dishes\n2) The drain\n3) The soggy meat\n"))
    if (action == 1):
        print(f"You go explore the bowl battlefield, {player}!")
        print("You have gained 5 points")
        pts += 5
    if (action == 2):
        print(f"What a risk taker you must be, {player}!")
        print("You have lost 5 points, lucky it wasn't more.\nStay Safe")
        pts -= 5
    if (action == 3):
        print(f"Its a greasy graveyard over here {player}\nAll the oil soaks into you, you're like a bubble CYBORG!\nYou gain 15! points.")
        pts += 15
    return pts


def main():
    """Main body and Menu of game."""
    global points
    global player
    playing: bool = True
    greet()
    while (playing):
        print("\n\n-=-=-=-=- MAIN MENU -=-=-=-=-\n")
        print(f"{player}, you have {points} points!\n")
        action: int = int(input("Would you like to? (enter your answer as a number)\n1) Sud around\n2) Move towards the food\n3) pop :(\n"))
        if (action == 1):
            sud()
        if (action == 2):
            points = move(points)
        if (action == 3):
            print(f"We hate to see you go {player}, but you lived a good life.\nMay the sink god smile down upon you.\nYou ended with {points} points, truely swag {CONSTANT}")
            playing = False
    

if __name__ == "__main__":
    main()