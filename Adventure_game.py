import time
import random


def print_pause(message):
    print(message)
    time.sleep(1.5)


def intro(weapon, villain):
    print_pause("You find yourself standing in an open field, \n"
                "filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a " + villain + " is \n"
                "somewhere around here, and has been terrifying \n"
                "the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not so \n"
                "effective) dagger.")


def house(weapon, villain):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens\n"
                "and out steps a " + villain + ".")
    print_pause("Eep! This is the " + villain + "'s house!")
    print_pause("The " + villain + " attacks you!")
    if "sword" not in weapon:
        print_pause("You feel a bit under-prepared for this\n"
                    "what with only having a tiny dagger.")
    while True:
        action_2 = input("Would you like to (1) fight or (2) runaway\n")
        if action_2 == '1':
            if "sword" in weapon:
                print_pause("As the  " + villain + " moves to\n"
                            "attack you, you unsheath your new sword")
                print_pause("The sword of Ogoroth shines brightly\n"
                            "in your hands as you brace yourself\n"
                            "for the attack.")
                print_pause("But the " + villain + " takes one look at\n"
                            "your shiny new toy and runs away!")
                print_pause("You have rid the town of the " + villain + ".\n"
                            "You are victorious!")
                print_pause("GAME OVER")
            else:
                print_pause("You do your best...")
                print_pause("but your dagger is no match for " + villain + ".")
                print_pause("You have been defeated!")
                print_pause("GAME OVER")
            re_play()
            break
        if action_2 == '2':
            print_pause("You run back into the field. Luckily, \n"
                        "you don't seem to have been followed.")
            field(weapon, villain)
            break


def cave(weapon, villain):
    if "sword" in weapon:
        print_pause("You peer cautiously into the cave.")
        print_pause("You have been here before, and gotten \n"
                    "all the good stuff. It's just an empty cave now.")
        print_pause("You walk back out to the field.")
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical sword of Ogoroth!")
        print_pause("You discard your silly old dagger\n"
                    "and take the sword with you.")
        print_pause("You walk back out to the field.")
        weapon.append("sword")
    field(weapon, villain)


def field(weapon, villain):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to enter into the cave.")
    print_pause("What would you like to do ?")
    while True:
        action = input("Please enter 1 or 2. \n")
        if action == '1':
            house(weapon, villain)
            break
        elif action == '2':
            cave(weapon, villain)
            break


def re_play():
    replay = input("Would you like to play again? (y/n)\n").lower()
    if replay == 'y':
        print_pause("Excellent!")
        print_pause("Restarting the game")
        print_pause(".................")
        play_game()
    elif replay == 'n':
        print_pause("Thanks for playing !")
        print_pause("See you next time.")
    else:
        re_play()


def play_game():
    weapon = []
    villain = random.choice(["wicked fairie", "Pirate", "troll",
                            "gorgon", "dragon"])
    intro(weapon, villain)
    field(weapon, villain)


play_game()
