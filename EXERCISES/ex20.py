from sys import argv

script, input_file = argv
#defines the function print_all
def print_all(f):
    print(f.read())
#defining the function rewind, using the buil-in function, seek (seek relates to bytes)
def rewind(f):
    f.seek(0)
#defines the function, print_a_line, with inputs line_count and f
def print_a_line(line_count, f):
    #looks like line_count and readline are built-in functions
    print(line_count, f.readline())
#sets the variable current_file to open input_file
current_file = open(input_file)
#prints, with a line break
print("First, let's print the whole file:\n")

print_all(current_file)

print("Now, let's rewind.  Kind of like a tape")
#runs the rewind function
rewind(current_file)

print("Let's print three lines:")

current_line = 1
#print_a_line is a function that prints a single line.
print_a_line(current_line, current_file)

#this loops through and increments the value of the variable 'current_line'
current_line += 1
#the above is just a contraction, equating to current_line = current_line + 1
#print_a_line seems to print the literal line, vs the count of the line.
print_a_line(current_line, current_file)


current_line += 1
print_a_line(current_line, current_file)
