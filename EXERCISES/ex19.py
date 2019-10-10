#more function practice

#first line defines our function, cheese_and_crackers.  It takes two inputs that are also variables:
#cheese_count and boxes_of_crackers.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    #after definition, to encapsulate your function, you'll indent.  Atom does this automatically.
    print(f"You have {cheese_count} cheeses!")
    #These are f print strings, letting us output both strings and variables.
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    #normal print function
    print("Man, that's enough for a party!")
    #normal print function, adding a \n as a line break - similar to <br> in html
    print("Get a blanket.\n")
#prints, then runs our function.
print("We can just give the function numbers directly:")
cheese_and_crackers(20,30)

#prints, then runs our functins based on variables that we define.
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#prints, then runs our function with math based inputs
print("We can even do math inside too:")
cheese_and_crackers(10+20, 5+6)

#prints, then runs our function with variables and math based inputs
print("And we can combine two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
