"""An interactive command-line Treasure Island adventure game."""


def get_choice(prompt, valid_options):
    """Keep prompting until the player enters one of the allowed choices."""
    while True:
        choice = input(prompt).strip().lower()

        if choice in valid_options:
            return choice

        print(f"Invalid choice! Please enter: {', '.join(valid_options)}.")


def treasure_game():
    """Play one round; return True if the player finds the treasure."""
    print("\n" + "=" * 39)
    print("       WELCOME TO TREASURE ISLAND")
    print("=" * 39)
    print("Your mission is to find the treasure.\n")

    direction = get_choice(
        "You are at a crossroad. Do you go left or right? ",
        ("left", "right"),
    )

    if direction == "right":
        print("\nGame Over! You fell into a trap!")
        return False

    river_choice = get_choice(
        "You reached a river. Do you swim or wait? ",
        ("swim", "wait"),
    )

    if river_choice == "swim":
        print("\nGame Over! You were attacked by a shark!")
        return False

    door = get_choice(
        "You see 3 doors: red, blue, yellow. Choose one: ",
        ("red", "blue", "yellow"),
    )

    if door == "yellow":
        print("\nCongratulations! You found the treasure! YOU WIN!")
        return True
    elif door == "red":
        print("\nGame Over! You entered the fire room!")
    else:
        print("\nGame Over! You entered the beast room!")

    return False


def main():
    """Let the player replay until they decide to quit."""
    while True:
        treasure_game()

        play_again = get_choice(
            "\nWould you like to play again? (yes/no): ",
            ("yes", "no", "y", "n"),
        )

        if play_again in ("no", "n"):
            print("Thanks for playing Treasure Island! Goodbye!")
            break


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nGame closed. Thanks for playing!")
