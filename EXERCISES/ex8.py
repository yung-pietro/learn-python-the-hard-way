#sets formatter to the four brackets
formatter = "{} {} {} {} "

#inserts  1234 and then prints formatter
print(formatter.format(1, 2, 3, 4))
#inserts values one, two, three, four, then prints
print(formatter.format("one", "two", "three", "four"))
#same thing here.   adding true false true false true
print(formatter.format(True, False, False, True))
# adding original variable to itself
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
            "These keys of mine",
            "Sometimes they shine",
            "But other days",
            "It's just a haze.",
            "It's ok. "


))
