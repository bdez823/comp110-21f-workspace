"""Create your own adventure progam,pj00."""

__author__ = "730447313"

from random import randint


points: int 
player: str 


def main() -> None:
    greet()
    global points
    points = 0
    i: int = 0

    while i < 1:
        print("Type the path you wish to go on.")
        path_choice: str = input("Textual, Number or Quit: ")
        
        if path_choice == "Quit":
            print(f"Your score is {points}, thanks for playing!!")
            i = 2
    
        if path_choice == "Textual":
            textual_input_game()
        
        if i < 1:
            print(f"You've earned {points}, {player}, would you like to continue")


def greet() -> None:
    print("In this adventure you get to choose between taking part in a textual boxing match or ..... .")
    global player
    player = input("Enter your name: ")
    print(f"Good luck in your match {player}")


def textual_input_game() -> None:
    rounds: int = 3
    i: int = 1
    global player
    global points
    
    while i <= rounds:
        cpu_pts: int = 0
        user_action_int: int = 0
        j: int = 0
        print(f"Round {i}")
        while j < 3:
            user_action: str = input(f"choose your action {player}: Hook, Jab or Uppercut! ")
        
            if user_action == "Hook":
                user_action_int = 1
            if user_action == "Jab":
                user_action_int = 2
            if user_action == "Uppercut":
                user_action_int = 3
        
            if user_action_int != randint(1, 3):
                if 1 == randint(1, 15):
                    cpu_pts = cpu_pts + 3
                    points = points - 3
                    print(f"You were knocked down {player}. You lost 3 pts")
                else:
                    points = points - 1
                    cpu_pts = cpu_pts + 1
                    print(f"You got hit {player}. You lost 1 pts")
            else:
                if 1 == randint(1, 3):
                    points = points + 3
                    cpu_pts = cpu_pts - 3
                    print(f"You scored a knock down {player}. You gain 3 points!!!")

                else: 
                    points = points + 1
                    cpu_pts = cpu_pts - 1
                    print(f"You scored a hit {player}. You gain 1 point!")
            j = j + 1
        print(f"After round {i} you have {points}")
        if i == 3:
            if points > cpu_pts:
                print(f"You won {player}")
            else:
                print(f"You didn't win {player}")
        i = i + 1


if __name__ == "__main__":
    main()