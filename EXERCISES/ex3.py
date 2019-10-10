print("I will now count ")
#this does some simple arithmetic, combining text and math.
print("Hens",  25.0 + 30.0 / 6)
#here is a modulo.  A couple things about our friend the modulo: 1.  If it is divided by 0, then it returns undefined.
#if it is a smaller number divided by a larger number, then the whole first operand is the result.  ie 3%4 returns 3.
print("Roosters", 100 - 25 * 3 % 4)

print("Now I will count the eggs:")
#order of operations: *, /, then %, then + and -
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

print("Is it true that 3 + 2 < 5 - 7")
#comparisons result: True or False
print(3 + 2 < 5 - 7)
#one can type text and arithmetic in the same line
print("What is 3 + 2?", 3 + 2)
print("What is 5 - 7?", 5 - 7)

print("Oh, that's why it's false.")

print("How about some more.")

print("Is it greater?", 5 > -2)
print("Is it greater or equal?",  5  >=  -2)
print("Is it less or equal?",  5  <= -2)
