"""Create your own adventure progam, Boxing and Letter guessing game adventures."""

__author__ = "730447313"

from random import randint


points: int 
player: str
INJURED_CONSTANT: str = "\U0001F4A5\U0001F915\U0001F4AB"
POINT_SCORED_CONSTANT: str = "\U0001F601"
WINNER_CONSTANT: str = "\U0001F3C5"
CONGRADULATIONS_CONSTANT: str = "\U0001F973"
NO_POINTS_CONSTANT: str = "\U0001F62C"


def main() -> None:
    greet()
    global points
    points = 0
    i: int = 0

    while i < 1:
        print("Type the path you wish to go on.")
        path_choice: str = input("Boxing, Letter or Quit: ")
        
        if path_choice == "Quit":
            print(f"You accumulated {points} point(s) on your adventure, thanks for playing!!")
            i = 2
    
        if path_choice == "Boxing":
            textual_input_game()
         
        if path_choice == "Letter":
            points = letter_input_game(points)

        if i < 1:
            print(f"{CONGRADULATIONS_CONSTANT}You've earned {points} total adventure point(s), {player}, would you like to continue")


def greet() -> None:
    print("In this adventure, you get to choose between taking part in a 3 round textual Boxing match, where you call your own strikes, to earn adventure points ")
    print("or a Letter guessing game where you will type a word and try to guess the which letter the computer selects each round their will be 5 rounds to try and earn the most points.")
    print("Points earned in each adventure will affect your overall adventure points.")
    global player
    player = input("Enter your name to begin adventure: ")
    print(f"Good luck on your adventure {player}")


def textual_input_game() -> None:
    rounds: int = 3
    i: int = 1
    match_score: int = 0
    global player
    global points
    while i <= rounds:
        cpu_pts: int = 0
        user_action_int: int = 0
        j: int = 0
        print(f"Round {i}")
        while j < 3:
            user_action: str = input(f"choose your action {player}: Hook, Jab or Uppercut! ")
            cpu_random: int = randint(1, 3)
            if user_action == "Hook":
                user_action_int = 1
            if user_action == "Jab":
                user_action_int = 2
            if user_action == "Uppercut":
                user_action_int = 3
            
            if user_action_int == cpu_random:
                if 1 == randint(1, 10):
                    cpu_pts = cpu_pts + 3
                    match_score = match_score - 3
                    points = points - 3
                    print(f"{INJURED_CONSTANT} You were knocked down {player}. You lost 3 pts")
                else:
                    cpu_pts = cpu_pts + 1
                    match_score = match_score - 1
                    points = points - 1
                    print(f"You got hit {player}. You lost 1 pts")
            
            if user_action_int != cpu_random:
                if 1 == randint(1, 10):
                    cpu_pts = cpu_pts - 3
                    match_score = match_score + 3
                    points = points + 3
                    print(f"{POINT_SCORED_CONSTANT}You scored a knock down {player}. You gain 3 points!!!")
                else: 
                    cpu_pts = cpu_pts - 1
                    match_score = match_score + 1
                    points = points + 1
                    print(f"{POINT_SCORED_CONSTANT}You scored a hit {player}. You gain 1 point!")
            
            j = j + 1

        print(f"After round {i} you have {match_score} point(s) in this match, and {points} total adventure point(s).")
        if i == 3:
            if match_score > cpu_pts:
                print(f"{WINNER_CONSTANT}You won {player}")
            else:
                print(f"You didn't win {player}")
        i = i + 1


def letter_input_game(x: int) -> int:
    global player
    rounds: int = 5
    i: int = 1
    user_word: str = input("Type a word you would like to use to play: ")
    indexing_word_minus_one: int = len(user_word) - 1
    
    while i <= rounds:
        user_guess: str = input(f"Guess a letter in the word \"{user_word}\" ")
        cpu_letter: str = user_word[randint(0, indexing_word_minus_one)]

        if user_guess == cpu_letter:
            x = x + 2
            print(f"{POINT_SCORED_CONSTANT} You guessed correctly {player}, you've earned two points!!! Your total adventure points after round {i} is {x}. ")
    
        else:
            print(f"{NO_POINTS_CONSTANT}You did not guess correctly {player}. no points.Your total adventure points after round {i} is {x}.")

        i = i + 1
    
    return x


if __name__ == "__main__":
    main()