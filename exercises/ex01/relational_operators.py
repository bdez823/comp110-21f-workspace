"""In Progess, COMP110 EX01 relational_operators, bool questions that ouput an answer that are determined by user input."""

__author__ = "730447313"

user_input_1: str = input("Left-hand side: ")
user_input_2: str = input("Right-hand side: ")
integer_value_1: int = int(user_input_1)
integer_value_2: int = int(user_input_2)
less_than_output: bool = (integer_value_1) < (integer_value_2)
is_at_least_output: bool = (integer_value_1) >= (integer_value_2)
eqaul_to_output: bool = (integer_value_1) == (integer_value_2)
not_eqaul_to_output: bool = (integer_value_1) != (integer_value_2)
print((user_input_1) + " < " + (user_input_2) + " is " + str(less_than_output))
print((user_input_1) + " >= " + (user_input_2) + " is " + str(is_at_least_output))
print((user_input_1) + " == " + (user_input_2) + " is " + str(eqaul_to_output))
print((user_input_1) + " != " + (user_input_2) + " is " + str(not_eqaul_to_output))