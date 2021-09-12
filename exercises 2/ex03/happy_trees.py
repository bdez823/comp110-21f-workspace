"""Drawing forests in a loop."""

__author__ = "123456789"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
tree_string: str = TREE
depth: int = int(input("Depth: "))
i: int = 0
depth_plus_one: int = (depth + 1)

if depth >= 1:
    while i < depth_plus_one:    
        if i == 0:
            print(TREE)
        if i > 1:
            tree_string = tree_string + TREE
            print(tree_string)
        i = i + 1