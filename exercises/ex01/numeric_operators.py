"""Completed, COMP110 EX01 numeric_operators, which makes calculations based on user input."""

__author__ = "730447313"

user_input_00: str = input("Left-hand side: ")
user_input_01: str = input("Right-hand side: ")
integer_value_00: int = int(user_input_00)
integer_value_01: int = int(user_input_01)
power_output: int = (integer_value_00) ** (integer_value_01)
division_output: float = (integer_value_00) / (integer_value_01)
int_division_output: int = (integer_value_00) // (integer_value_01)
remainder_output: int = (integer_value_00) % (integer_value_01)
print((user_input_00) + " ** " + (user_input_01) + " is " + str(power_output))
print((user_input_00) + " / " + (user_input_01) + " is " + str(division_output))
print((user_input_00) + " // " + (user_input_01) + " is " + str(int_division_output))
print((user_input_00) + " % " + (user_input_01) + " is " + str(remainder_output))