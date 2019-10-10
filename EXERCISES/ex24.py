#this exercise is designed to build up stamina
print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of lovelynor comprehend passion from intuition
and requires explanation
\n\t\twhere there is none.
"""

print("----------------")
print(poem)
print("----------------")


five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secretFormula(started):
    jellyBeans = started * 500
    jars = jellyBeans/1000
    crates = jars / 100
    return jellyBeans, jars, crates
#A common use of functions is computing one or more results, which are entirely determined by the
#parameters passed to it. A function is set up such that it can be re-used throughout the program, increasing
#readability, and improving efficiency.

#functions can take one or more parameters (arguments).

startPoint = 10000
beans, jars, crates = secretFormula(startPoint)

#Remember that this is another way to start a string:
print("With a starting poing of: {}".format(startPoint))

#it's just like that with an f string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

startPoint = startPoint / 10

print("We can also do it this way:")
formula = secretFormula(startPoint)
#this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))
