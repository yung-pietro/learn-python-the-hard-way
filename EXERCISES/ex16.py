#imports argv
from sys import argv
#let's you know you need to call the script first, then a filename
script, filename = argv
#prints text and a variable
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
#opens the file - w signifies that we have write permissions, we'll write to it
target = open(filename, 'w')

print("Truncating the file.  Goodbye!")
target.truncate()
#empties the file

print("Now I'm going to ask you for three lines.")
#creates 3 variables
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")
#writes first variable
target.write(line1)
#creates a line-break
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()
