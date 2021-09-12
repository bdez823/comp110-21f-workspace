"""Finding duplicate letters in a word."""

__author__ = "123456789"

user_word: str = input("Enter a word: ")
i: int = 0
j: int = 1
t: int = 1
bool_storage: bool = False
number_of_characters: int = (len(user_word))
number_of_characters_minus_two: int = (len(user_word) - 2)

while i < number_of_characters:
    # isolates letter from user_word input
    first_letter_identifier: str = user_word[i]
    # Loop to compare specific letter to others in string
    while j < number_of_characters:
        second_letter_identifier: str = user_word[j]
        if first_letter_identifier == second_letter_identifier:
            bool_storage = True    
        j = j + 1
    # lines 23 and 24, reseting counter and adding one, in order to run sub loop and to make sure loop not evaluating same value twice.
    t = t + 1
    j = t   
    i = i + 1
print("Found duplicate: " + str(bool_storage))