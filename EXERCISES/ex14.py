from sys import argv

script, user_name, age = argv
#when I run this, the script argument is already implied.  But I must add a user_name when calling the script in the command line

prompt = '- '
#this is the prompt key.  Change it here once and it populates throughout


print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me, {user_name}?")
likes = input(prompt)

print(f"Where do you live, {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.  You live in {lives}.  Not sure where that is.
But you're {age}, and you have a {computer} computer.   Nice.
""")

#ZORK - one of the assignments is to find and play Zork
