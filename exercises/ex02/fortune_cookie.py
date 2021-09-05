"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730447313"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


print("Your fortune cookie says...") 

variable_response: int = randint(1, 4)

if variable_response == 1:
    print("You are going to have a good day!")
else:
    if variable_response == 2: 
        print("Positive vibes are headed your way!")
if variable_response == 3:
    print("You will feel relaxed today!")
else:
    if variable_response == 4:
        print("You are going to ace your next quiz!")
print("Now, go spread positive vibes!")