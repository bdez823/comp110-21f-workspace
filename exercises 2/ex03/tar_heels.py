"""An exercise in remainders and boolean logic."""

__author__ = "ENTER YOUR 9-DIGIT PID HERE"


user_int: int = int(input("Enter an int: "))

if ((user_int % 2) == 0) and ((user_int % 7) == 0):
    print("TAR HEELS")
else:    
    if (user_int % 2) == 0:
        print("TAR")
    else:    
        if (user_int % 7) == 0:
            print("HEELS")
        else:
            print("CAROLINA")
    