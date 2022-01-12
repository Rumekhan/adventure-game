import time
import random
villain_1 = "Dragon"
villain_2 = "Goblin"
villain_3 = "Bear"
villain_4 = "Beast"
villain_5 = "Dinosaur"
ammo = []
villain = random.choice([villain_1, villain_2,
                        villain_3, villain_4, villain_5])


def print_pause(message):
    print(message)
    time.sleep(1.8)


def fight():
    print_pause(f"The {villain} attacks you! ")
    print_pause("You draw your gun.")


def runaway():
    print_pause("You feel you are unprepared")
    print_pause("You see an open lab window")
    print_pause("You jump through it and skedaddle")
    print_pause("You run for your life like there is no tomorrow.")
    print_pause("You managed to escape back to the open field.")


def scene_one():
    print_pause("You are a poor cop in a new city")
    print_pause("You are driving late at night, \n"
                "a thunderstorm approaches.")
    print_pause("You drive into what looks \n"
                "like a carpark with a weird entrance")
    print_pause("Immediately you passs the entrance, \n"
                "you blank out.")
    print_pause("You wake up in an open field, \n"
                "and cannot remember anything.")
    print_pause("In your hand you is a small pistol \n"
                "with no bullets.")


def scene_two():
    print_pause("To your left is a lab.")
    print_pause("To your right is a dark cave.")
    print_pause("Press 1 to enter the lab.")
    print_pause("Press 2 to enter into the cave")
    print_pause("Which will you enter ?")
    while True:
        action = input("Please enter 1 or 2. ")
        if action == '1':
            lab()
            break
        elif action == '2':
            cave()
            break


def lab():
    print_pause("You walk into the lab")
    print_pause(f"You find a {villain}'s lair")
    print_pause(f"The {villain} had turned the lab to its nest.")
    print_pause("You see a door that leads to the carpark you came through")
    print_pause(f"You approach the door but the {villain} appears  \n"
                "and block's you from leaving.")
    print_pause("What are you going to do ?")
    while True:
        action_2 = input("Would you like to (1) fight or (2) runaway ? \n")
        if action_2 == '1':
            if "bullets" in ammo:
                fight()
                print_pause("You quickly load the bullets.")
                print_pause(f"You fire multiple times at the {villain}.")
                print_pause(f"The gunshots scare the villain and \n"
                            "it retreats in fear")
                print_pause("The coast is clear, you can now \n"
                            "escape with your diamond.")
                print_pause("You go through the exit door and  \n"
                            "return back to the real world")
                print_pause("You are victorious and rich !!!!")
            else:
                fight()
                print_pause("You have no bullets")
                print_pause("You say your last prayers")
                print_pause(f"The {villain} attacks you and \n"
                            "makes you its dinner.")
                print_pause("You should have been more prepared")
                print_pause("GAME OVER!!!!!!")
            replay()
            break
        elif action_2 == '2':
            runaway()
            scene_two()


def cave():
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
                    "you just need to find a \n "
                    "way out of this strange place.")
        print_pause("You exit the cave and return to the open field.")
    scene_two()


def replay():
    play_again = input("Do you want to play again ?  (y/n)\n").lower()
    if play_again == 'y':
        print_pause("LETS GOOOOOOO!!!!!!")
        print_pause("Game is Loading.......................")
        game_play()
    elif play_again == 'n':
        print_pause("Thanks for playing the ADVENTURE GAME")
        print_pause("Until next time")
        print_pause("Goodbye")
    else:
        replay()


def game_play():
    scene_one()
    scene_two()


game_play()
