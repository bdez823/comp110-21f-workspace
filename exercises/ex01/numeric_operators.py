"""Completed, COMP110 EX01 numeric_operators, which makes calculations based on user input."""

__author__ = "730447313"

user_input_00: int = int(input("Left-hand side: "))
user_input_01: int = int(input("Right-hand side: "))
power_output: int = (user_input_00) ** (user_input_01)
division_output: float = (user_input_00) / (user_input_01)
int_division_output: int = (user_input_00) // (user_input_01)
remainder_output: int = (user_input_00) % (user_input_01)
print(str(user_input_00) + " ** " + str(user_input_01) + " is " + str(power_output))
print(str(user_input_00) + " / " + str(user_input_01) + " is " + str(division_output))
print(str(user_input_00) + " // " + str(user_input_01) + " is " + str(int_division_output))
print(str(user_input_00) + " % " + str(user_input_01) + " is " + str(remainder_output))