"""Counting letters in a string, Finished."""

__author__ = "730447313"


letter_searched: str = input("What letter do you want to search for?: ")
searched_word: str = input("Enter a word: ")
word_len_value: int = len(searched_word)
letter_counter: int = 0
i: int = 0
while i < word_len_value:
    letter_order: str = (searched_word[i])
    if letter_searched == letter_order:
        letter_counter = letter_counter + 1
    i = i + 1
number_of_letter: str = str(letter_counter)
print("Count: " + number_of_letter)