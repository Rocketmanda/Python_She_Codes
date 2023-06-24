# Lists 
# numbers = [1,2,3]
# numbers[0]
# Dictionary
# Keys are unique
# Values can be any data type
# Keys can only be immutable data types 
# Immutable - Strings, integers, floats, booleans
# student_phonebook = {
#     "Cindy":111,
#     "Tracey":123,
#     "Pauline":444
#     }
# print(student_phonebook)
# del student_phonebook["Tracey"]
# student_phonebook["Cindy"] = 555
# print(student_phonebook)
# print(student_phonebook["Asli"])
# student_phonebook["Yara"] = 555
# print(student_phonebook)
# print(type(student_phonebook))

student_phonebook = {
    "Cindy":111,
    "Tracey":123,
    "Pauline":444
    }

# Iterate all the values in a dictionary
# for value in student_phonebook.values():
#     print(value)

# Iterate all the key-value pairs
# for key in student_phonebook:
#     print(key, student_phonebook[key])

# a,b,c = [1,2,3]
# print(a)
# print(b)
# print(c)

# for key,value in student_phonebook.items():
#     print(key,value)

# Q1
groceries = {
    "Baby Spinach": 2.78,
    "Hot Chocolate": 3.70,
    "Crackers": 2.10,
    "Coffee": 9.00,
    "Carrots": 0.56,
    "Oranges": 3.08
}
total_cost = 0

for item in groceries:
    quantity = int(input(f"How many {item} would you like? "))
    cost = groceries[item] * quantity
    total_cost += cost
print(f"${total_cost}")

# Q2
colour_counts = {
    "blue": 0,
    "green": 0,
    "yellow": 0,
    "red": 0,
    "purple": 0,
    "orange": 0,
    }