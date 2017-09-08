n = int(input())
check = {True: "Not Weird", False: "Weird"}

print(check[
        n%2==0 and (
            n in range(2,6) or 
            n > 20)
    ])
    
#Line 1. We just take the input, remove any excess whitespace and store the integer in a variable. 
#Line 2. We define a dictionary, with boolean values as keys. If you didn't know this before, dictionaries can use any types as keys, not just strings! We are now using this to translate boolean values to strings. Now, we ask Python to print something. We put the dictionary we just defined inside, and expect the program to print the value of the key we put in. I've cut some corners here, because usually you would see a single variable inside those square brackets. I just didn't feel like adding an extra line, so I put the entire boolean expression instead. Here comes the interesting part: first, we are checking if the input number is even. If it isn't, the expression will automatically return False, the dictionary outputs Weird and the print function prints the string on the console. However, if the input number is indeed even, we then check if it's in the range from 2 to 6 or if it's more than 20. If either of these are true, the expression returns True, the dictionary outputs Not Weird and the said string is printed on the screen. If neither of these expressions are true, the expression returns False.
