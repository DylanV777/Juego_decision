print("Welcome to the Enchanted Forest Adventure!")

while True:
    print("\nYou find yourself in front of two paths: left or right.")
    path = input("Which do you choose? ").lower()

    if path == "left":
        print("You encounter a river. You can swim or go around.")
        action = input("What do you do? swim/go around: ").lower()
        if action == "swim":
            print("The current drags you away. Game over!")
        elif action == "go around":
            print("You find a hidden treasure. You win!")
        else:
            print("You do nothing and night falls. Game over!")
    elif path == "right":
        print("You run into a dragon. You can fight or run away.")
        action = input("What do you do? fight/run: ").lower()
        if action == "fight":
            print("The dragon burns you with fire. Game over!")
        elif action == "run":
            print("You escape safe and sound. You are a hero!")
        else:
            print("You freeze and the dragon sees you. Game over!")
    else:
        print("You did not choose a valid path. The forest confuses you. Game over!")

    replay = input("\nDo you want to play again? yes/no: ").lower()
    if replay != "yes":
        print("Thanks for playing! See you next time.")
        break