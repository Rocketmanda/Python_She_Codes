# Function - an activity that is natural to or the purpose of a person or thing.
# Functions we've already seen
# input(), len(), int(), print() 

# name = input("What is your name?")
# age = input("How old are you?")
# if age >= 18:
#     print("Welcome")
# else:
#     print("You can not enter.")

# Task Seperation
def ask_user_name():
    # print("Now function is entered")
    name = input("What is your name?")
    print(name)
    return name 
    print("Hello") # doesn't get executed

# Function definition
# Calling a function

# print("Hello")
# answer = ask_user_name() #user_input = input("tell me your name")
# print(answer)
# print("Hi")


# def ask_user_age():
#     age = input("How old are you?")
#     if age >= 18:
#         print("Welcome")
#     else:
#         print("You can not enter.")

# Parameters
total = 0 # Global variable
def add(number1, number2): # number1 = 2 , number2 = 3
    #print(total)
    #result = number1 + number2 # result is a local variable
    return (number1 + number2, 5, "This is the calculation")

#print()
#print(total)
print(add(2,3))
answer = add(2,3) #
print(answer)
#name = input("What's your name")
#print(answer)
#print(result) # Local variable 