from sys import argv

script, fruit, veggies, meats  = argv

print("The script is called:", script)
print("The fruit is called:", fruit)
print("The veggies are called:", veggies)
print("The meats are called:", meats)
favorite = input("What's your favorite snack?")

print(f"Cool!  I love {favorite} too!")
