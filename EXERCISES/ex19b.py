#more function practice

#first line defines our function, cheese_and_crackers.  It takes two inputs that are also variables:
#cheese_count and boxes_of_crackers.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    #after definition, to encapsulate your function, you'll indent.  Atom does this automatically.
    print(f"You have {cheese_count} cheeses!")
    #These are f print strings, letting us output both strings and variables.
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    #normal print function
    if cheese_count >= 10:
        print("Man, that's enough for a party!")
    #normal print function, adding a \n as a line break - similar to <br> in html
        print("Get a blanket.\n")
    else:
        print("You might try to find some more cheeses.")

#prints, then runs our functins based on variables that we define.
print("Hey.  How many cheeses did you find?")
#inputs read submissions as strings by default.  In this case, I'm needing to define the input as an integer to make my function run correctly.
amount_of_cheese = int(input())
print("And crackers?")
amount_of_crackers = int(input())

#print("OR, we can use variables from our script:")

cheese_and_crackers(amount_of_cheese, amount_of_crackers)
