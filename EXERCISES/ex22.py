print("something")
#prints a string

print("something", 4 + 2)
#prints a string and an operations

variable1 = 12 / 5
# '=' sign defines a variable

print(f"Some string and a {variable}")
# f-print allows you to print a string and a variable

variable = f"some string and a {variable}"
#variables can be compound

variable = False
#variables can be binary

joke_evaluation = "Isn't that funny? {}"
print(joke_evaluation.format(variable))
#use format to evaluate the binary

print(variable1 + variable)
#concatenates two variables

print (variable3 = 'another value')
#one can define and print a variable inline

formatter = "{} {} {}"
print(formatter.format("thing1", "thing2", "thing3"))
#that's the syntax.  Nor really sure what one uses this for

print("This is a line. \n This is a new line.")
# \n creates a line break

print("""
Three " marks also creates a
multi-line text field.
Like this one.
""")

\t
#creates an indent

print("How old are you?", end=' ')
age = input()
#not sure what the end= ' ' does here.
#input allows you to manipulate the variable1

age = input("How old are you? ")
#a more simple way to create an input


from sys import argv
thing1, thing2, thing3 = argv
#allows one to define different variables when calling the python funciton originally

txt = open(filename)
#opens a file and sets a variable to it

print(txt.read())
txt.close()
#prints the full file

target = open(filename, 'w')
#opens file with write permissions
target.truncate()
#erases file
target.write("Some thing")
target.close()

## Finished at exercise 16
