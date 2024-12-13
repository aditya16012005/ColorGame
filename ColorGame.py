import random
import sys


total_attempts = 6

color_list = [
    "red","green","blue","pink"
]

computer_choice = None

def continue_play(total_attempts):
    print()
    print("Enter your choice")
    print("1> Start again")
    print("2> Exit")
    choice = int(input())
    if choice == 1:
        start_game(total_attempts,True)
    elif choice == 2:
        sys.exit()



def start_game(total_attempts,newgame):
    global computer_choice

    if newgame:
        computer_choice = random.choice(color_list)

    print("Choose a color: ")
    print()
    user_choice = str(input())

    if user_choice == computer_choice:
        print("Congrats! you won.")
        print("Attempts left:"+str(total_attempts-1))
        continue_play(total_attempts)

    elif total_attempts > 1:
            print("Incorrect color, try again")
            total_attempts -= 1
            print("Attempts left:" + str(total_attempts))
            print()
            start_game(total_attempts,False)
    else:
            print("You lose, no attempts left")
            continue_play(5)






start_game(total_attempts,True)
