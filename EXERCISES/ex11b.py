#task: explore inputs and create another form for users
#there are two kinds of inputs, standard input() and raw_input().  Input is used for integers and rawinput is used for strings

print("Name:", end=' ')
name = input()

# name = raw_input("Name: ")
# type(name)

print("Phone:" , end=' ')
phone_number = input()
print("Email:", end=' ')
email=input()
print("Orders per month?:",  end=' ')
orders=input()

print(f"Thanks {name}.  We'll get back to you shortly.")
