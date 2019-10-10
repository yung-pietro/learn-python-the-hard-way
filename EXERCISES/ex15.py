#imports the argv module from the system
from sys import argv
#defines the arguments needed to run the script
script, filename = argv
#sets txt as a variable equal to an open file
txt = open(filename)
#prints a mixed line of text  /variable
print(f"Here's your file {filename}:")
#reads the variable 'txt' and prints it
print(txt.read())
txt.close()
#uses an input to define a new variable
print("Type your filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
txt_again.close()
