import time
import random
import string


def print_pause(message):
    print(message)
    time.sleep(1.2)


def typewriter_simulator(message):
    for char in message:
        print(char, end='')
        if char in string.punctuation:
            time.sleep(.0)
        time.sleep(.00)


def scene_one(ammo, villain):
    typewriter_simulator("You are a poor cop in a new city. \n")
    typewriter_simulator("You are driving late at night, \n")
    typewriter_simulator("a thunderstorm approaches. \n")
    typewriter_simulator("You drive into what looks \n"
                         "like a carpark with a weird entrance. \n")
    typewriter_simulator("Immediately you passs the entrance, \n"
                         "you blank out. ")
    typewriter_simulator("You wake up in an open field, \n"
                         "and cannot remember anything. ")
    typewriter_simulator("In your hand you is a small pistol \n"
                         "with no bullets. \n")


def field(ammo, villain):
    print_pause("On your left is a lab.")
    print_pause("On your right, is a dark cave.")
    typewriter_simulator("Press 1 to enter the lab.\n")
    typewriter_simulator("Press 2 to enter into the dark cave.\n")
    while True:
        choice1 = input('\u001b[37mPlease enter 1 or 2.\n')
        if choice1 == "1":
            lab(ammo, villain)
            break
        elif choice1 == "2":
            cave(ammo, villain)
            break
        else:
            validator_message()


def lab(ammo, villain):
    typewriter_simulator("You walk into the lab.  \n")
    typewriter_simulator(f"You find a {villain}'s lair. \n")
    typewriter_simulator(f"The {villain} had turned the lab to its nest. \n")
    typewriter_simulator("You see a door that leads \n"
                         "to the carpark you came through. \n")
    typewriter_simulator(f"You approach the door \n"
                         "but the {villain} appears  \n"
                         "and blocks you from leaving.\n")
    typewriter_simulator("What are you going to do ?\n")
    while True:
        action_2 = input("\u001b[37mWould you like to do \n"
                         "(1) fight or (2) runaway ? \n")
        if action_2 == '1':
            if "bullets" in ammo:
                fight(ammo, villain)
                typewriter_simulator("You quickly load the bullets.")
                typewriter_simulator(f"You fire multiple times \n"
                                     "at the {villain}.")
                typewriter_simulator(f"The gunshots scare the {villain} and \n"
                                     "it retreats in fear")
                typewriter_simulator("The coast is clear, you can now \n"
                                     "escape with your diamond.")
                typewriter_simulator("You go through the exit door and  \n"
                                     "return back to the real world\n")
                typewriter_simulator("You are victorious and rich $ $ $ $ $ ")
            else:
                fight(ammo, villain)
                typewriter_simulator("You have no bullets\n")
                typewriter_simulator("You say your last prayers.\n")
                typewriter_simulator(f"The {villain} attacks you and \n"
                                     "makes you its dinner.\n")
                typewriter_simulator("You should have been more prepared\n")
                print_pause("GAME OVER!!!!!!\n")
            replay()
            break
        elif action_2 == '2':
            runaway(ammo, villain)
            field(ammo, villain)
        else:
            validator_message()


def cave(ammo, villain):
    if "bullets" in ammo:
        print_pause("You have already been here, \n"
                    "nothing more to do here.")
        print_pause("You exit the cave and return to the open field.")
    else:
        print_pause("You walk into the dark cave.")
        print_pause("It is empty and scary.")
        print_pause("You trip over something")
        print_pause("It feels like a box, you open it and find \n"
                    "a huge diamond and some bullets.")
        ammo.append("bullets")
        print_pause("Hurray!!! You are goiing to be very rich, \n"
                    "you just need to find a\n"
                    "way out of this strange place.")
        print_pause("You exit the cave and return to the open field.")
    field(ammo, villain)


def fight(ammo, villain):
    print_pause(f"The {villain} attacks you! ")
    print_pause("You draw your gun.")


def runaway(ammo, villain):
    print_pause("You feel you are unprepared")
    print_pause("You see an open lab window")
    print_pause("You jump through it and skedaddle")
    print_pause("You run for your life like there is no tomorrow.")
    print_pause("You managed to escape back to the open field.")


def replay():
    play_again = input("\u001b[37mDo you want to play again ?\n"
                       "  (y / n )\n").lower()
    if play_again == 'y':
        print_pause("LETS GOOOOOOO!!!!!!")
        print_pause("Game is Loading.......................")
        game_play()
    elif play_again == 'n':
        print_pause("Thanks for playing the ADVENTURE GAME")
        print_pause("Until next time")
        print_pause("Goodbye")
    else:
        validator_message()
        replay()


def validator_message():
    colour_red = "\u001b[31;40mSorry that option is invalid. Try again." + " "
    invalid_input_text = colour_red
    typewriter_simulator(invalid_input_text)


def game_play():
    ammo = []
    villain = random.choice(["Dragon", "Goblin", "Bear", "Beast", "Dinosaur"])
    scene_one(ammo, villain)
    field(ammo, villain)


game_play()
