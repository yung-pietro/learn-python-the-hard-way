class Song(object):
#Song class
    def __init__(self, lyrics_variable):
        self.lyrics = lyrics_variable

    def sing_me_a_song(self):
        for line in self.lyrics_variable:
            #this is just a generic variable, and loops through each line b/c each line is actually just a list item.  The variable coould be called 'a'
            print(line)
        print('-----------------')
        print(line)
        #How would I print the number of lines in each song?





happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

perfect = Song(["I found a love",
                "foooor me",
                "Darling just dive right in, follow my lead.",
                "I found a girl, beautiful and sweet.",
                "Well I never knew you were the someone waiting for me."])

perfect.sing_me_a_song()

variable_test = (["I don't know this song",
                "But it serves to test my variable",
                "Is it working?"
                "Looks like, yes."])

# How can I output as a variable?
