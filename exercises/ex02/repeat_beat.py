"""Repeating a beat in a loop."""

__author__ = "730447313"


user_str_input: str = input("What beat do you want to repeat? ")
user_int_input: int = int(input("How many times do you want to repeat it? "))
user_str_gap: str = (" " + user_str_input)
user_stored_input: str = (user_str_input)
user_int_minus: int = int(user_int_input - 1)
i: int = 0
if user_int_input <= 0:
    print("No beat...")
while i < user_int_minus:
    user_stored_input = user_stored_input + user_str_gap
    i = i + 1
if i == user_int_minus:
    print(user_stored_input)