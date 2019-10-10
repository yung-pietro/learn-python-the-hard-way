#standard variable
types_of_people = 10
#my first interaction with what looks like a compound variable.  (a variable containing another avariable)
x = f"there are {types_of_people} types of people."

#string variables
binary = "binary"
do_not = "don't"
#another compound variable
y = f"Those who know {binary} and those who {do_not}."

#printing variables
print(x)
print(y)

#using f-print to output strings containing variables
print(f"I said: {x}")
print(f"I also said: '{y}'")

#designating hilarious to False
hilarious = False

#this seems to set up the end of this string to be able to handle an insert
joke_evaluation = "Isn't that joke so funny?! {}"

#the .format inserts the hilarious variable into joke_evaluation
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side"

print(w + e)
