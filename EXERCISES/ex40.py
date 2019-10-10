# You can think of a module as a specialized dictionary, where I can store code
# and access it with the . operator

# Similarly, a Class is a way of taking a grouping of functions and data and place
# them in a similar container so as to access with the . (dot) operator

# The difference being, a module is used once, and a class is used to make many things,
# including other classes or sub-classes.

#If a class is like a mini-module, there has to be a concept similar to 'import'
# That concept is called Instantiate - an obnoxious way of saying 'create'
# When you Instantiate a class, you get an Object.  You Instantiate / create a class
# by calling the class like it's a function.

class MyStuff(object):
    """docstring for MyStuff."""

    def __init__(self):
        self.tangerine = "And now a thousand years between!"
        #Sets the tangerine instance variable

    def apple(self):
        print("I AM CLASSY APPLES!")
        #This is an apple function.  What it does, I have no idea.

# And then to instantiate the class, we call it like a function
thing = MyStuff()
thing.apple()
print(thing.tangerine)
# Python looks for MyStuff and sees it's a class we're definining
# Python crafts an empty object with all the functions I've specified in the class using def
# Python looks to see if we've used the magic __init__ function, and if so, calls the function to iniitialize the newly created Object
# In the MyStuff function __init__, I get this extra variable, self - which is the 
# empty object that python made, and I can set variables on it, just like I would with a module, dictionary, or other Object
# In this case, I set self .tangerine to a song lyric, and then I've initialized the Object
# Now python can take this newly minted object and assign it to the thing variable to work with.

#Remember that this is NOT giving us the class, but instead, using the class as a blueprint for building a copy of that type of thing.

""""
• Classes are like blueprints or definitions for creating new mini-modules.
• Instantiation is how you make one of these mini-modules and import it at the same time. ”In- stantiate” just means to create an object from the class.
• Theresultingcreatedmini-moduleiscalledanobject,andyouthenassignittoavariabletowork with it. ```
""""
