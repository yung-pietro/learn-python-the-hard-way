#print a string
print ("Mary had a little lamb.")
#print a string, then add a variable.  For some reason, doesnt need an f in the front.
print("It's fleece was white as {}.".format('snow'))

print("And everywhere that Mary went.")
#add ten periods
print("." * 10) # what'd that do?
#setting variables
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

#watch end = ' ' at the end.  Try removing it to see what happens
#printing variables
#one can add a space by creating a variable with an empty " "
# one can define and print a variable inline
print(end1 + end2 + end3 + end4 + end5 + end6, end='test')
print(end7 + end8 + end9 + end10 + end11 + end12)
