"""Examples of using lists in a simple 'game' ."""

from random import randint

rolls: list[int] = list()  # str(10)

while len(rolls) == 0 or rolls[len(rolls) - 1] != 1:
    rolls.append(randint(1, 6))

print(rolls)

# Remove an item from list by its index("pop")
rolls.pop(len(rolls) - 1)
print(rolls)

# sum the values of our rolls!
i: int = 0
sum: int = 0
while i < len(rolls):
    sum = sum + rolls[i]
    i = i + 1

print(f"Total score: {sum}")
# rolls.append(randint(1, 6))
# rolls.append(randint(1, 6))
# rolls.append(randint(1, 6))
# print(rolls)


# # Acces an individual item
# print(rolls[0])
# print(rolls[1])

# # Access the legnth of a list (number of items)
# print(len(rolls))

# # Access the last item of a list
# print(rolls[len(rolls)-1])