# Python program to print the ASCII table
print ("Program started")

character = input("Enter a letter: ")
if len(character) == 1:
     print(f"The ASCII code of {character} is {ord(character)}")
else:
    print(" A single character was expected:")
print ("Program ended")

