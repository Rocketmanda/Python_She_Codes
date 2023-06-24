conditionals.py
# Boolean 
name = "Asli"
age = 19
height = 1.5
is_raining = True
my_variable2 = False
# print(is_raining)
# print(type(is_raining))

# Boolean Expressions - Expressions that produce a boolean value in return
# Comparison Operators
# == is equal to
# != is not equal to
# > greater than
# < less than
# >= greater or equal to
# <= less than or equal to
# print(5 > 3)
# print(3.5 > 6.3)
# print("Asli" == "asli")

# Mathematical Operators - Addition, Division, Substraction, Multiplication
# Boolean Operators - not, and, or
is_sunny = True
is_warm = False

#print(not is_sunny)
#print(is_sunny != is_warm)
#print(is_sunny or is_warm)
# True

#answer = is_sunny or is_warm
#print(answer)
# print(True or True)
#print(False)

temperature = 18
# syntax / semantics 

if temperature <= 18: 
    print("Weather is too cold!")
    print("I want to stay home.")
elif temperature > 28: #if statement false, it will check elif
    print("Weather is too hot!")
else:
    print("Weather is nice!")

#multiple if statements, will check the expression truthness regardless 

# else:
#     print("Weather is nice!")

#print("My dog looks cute.")

