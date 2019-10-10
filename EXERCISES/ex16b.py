from sys import argv

script, filename = argv

print(f"We're going to read {filename}.")
choice =input("Is that ok? (Y/N)")
if choice.lower().startswith("y"):
    print("Ok, let's continue...")
elif choice.lower().startswith("n"):
    print("Bye-bye...!")
    exit()

target = open(filename, 'r')

print("The contents of your file are the following:")

file_contents = target.read()
print(file_contents)
target.close()
