"""In Progess, COMP110 EX01 relational_operators."""

__author__ = "730447313"

user_input_1: int = int(input("Left-hand side: "))
user_input_2: int = int(input("Right-hand side: "))
less_than_output: int = bool((user_input_1) < (user_input_2))
is_at_least_output: int = bool((user_input_1) >= (user_input_2))
eqaul_to_output: int = bool((user_input_1) == (user_input_2))
not_eqaul_to_output: int = bool((user_input_1) != (user_input_2))
print(str(user_input_1) + " < " + str(user_input_2) + " is " + str(less_than_output))
print(str(user_input_1) + " >= " + str(user_input_2) + " is " + str(is_at_least_output))
print(str(user_input_1) + " == " + str(user_input_2) + " is " + str(eqaul_to_output))
print(str(user_input_1) + " != " + str(user_input_2) + " is " + str(not_eqaul_to_output))