"""An example of conditional (if-else) statements."""

SECRET: int = 3

print("I'm thinking of a value between 1-5, what is it?")
guess: int = int(input("what is your guess? "))

if guess == SECRET:
    print("you guessed correctly ")
    print("have a nice day")
else:
    print("Sorry you guessed incorectly ")
    if guess > SECRET:
        print("You guessed too high!")
    else:
        print("You guessed too Low!")
        
print("game over. ")