# # While Loop Q1
# # Solution 1
# # number = input("Enter a number")
# # number_list = []
# # while number != '':
# #     number_list.append(int(number))
# #     number = input("Enter another number")
# # if number == '':
# #     print(f"Your numbers sum to {sum(number_list)}")

# # While Loop Q1
# # Solution 2
# # number = input("Gimme a number")
# # sum = 0
# # while number:
# #     sum = sum + int(number)
# #     number = input("gimme another number")
# # print(sum)

# # While Loop Q2 (with for loop)
# number = input("Enter a number")
# list_of_numbers = range(int(number)+1)
# odd_numbers_list = []
# for number in list_of_numbers:
#     if number % 2 == 0:
#         pass
#     else:
#         odd_numbers_list.append(number)
# print(odd_numbers_list)


# While Loop Q2 (with while loop)
# solution 1
# print("The first number is 0")
# large_number = int(input("Enter a number: "))
# while (large_number > 0):
#     if(large_number % 2 != 0):
#         print(large_number)
#     large_number = large_number - 1

# While Loop Q2 (with while loop)
# solution 2
# number=0
# integer_number= int(input("Please enter a number"))

# while number<= integer_number:
#     if number%2==1:
#         print(number)
#     number = number+1

# While Loop Q3
# print("Guess the random number!")
# number = 76
# guess_attempt = int(input("Make a guess!"))

# while guess_attempt != number:
#     if guess_attempt < number:
#         print("Too low...") # You can ask right away also
#     else:
#         print("Too high...")
#     guess_attempt = int(input("Make another attempt"))

# print("You get it right!")


# For Loop Q1
# to_multiply = int(input("Give me a number"))
# for number in range(1,11):
#     print(f"{to_multiply} x {number} = {to_multiply*number}")

# For Loop Q2

# max_number = int(input("Enter a number"))
# total = 0

# for number in range(0, max_number+1):
#     # print("This is the variable number first time", number)
#     # print(total)
#     total += number  # 0+1+2+3
#     # print(number)
#     # print(total)

# print(total)

# For Loop Q2
# Second Solution
# user_number = int(input("Enter a number"))
# list_of_numbers = []

# for number in range(0,user_number+1):
#     list_of_numbers.append(number)# [0,1,2,3,4,5,6]

# total = sum(list_of_numbers) # total = 0,1,3,6,10...
# print(total)


# For Loop Q3
# my_numbers = []
# my_numbers = [3, 5, 9, 1]
# total = 0
# for element in my_numbers:
#     total += element
# print(total)

# For Loop Q4
# lyrics = [
#     ["Monica", "in my life"],
#     ["Erica", "by my side"],
#     ["Rita's", "all I need"],
#     ["Tina's", "what I see"],
#     ["Sandra", "in the sun"],
#     ["Mary", "having fun"],
#     ["Jessica", "here I am"]
# ]
# for i in lyrics:
#     name,text = i
#     song = "A little bit of " + name + " " + text + ";"
#     print(song)
# print(f"A little bit of you makes me your man (ah!)")
# print(f"*trumpet solo")

# Nested Loop Q1
# groceries = [
# 	["Baby Spinach", 2.78],
# 	["Hot Chocolate", 3.70],
# 	["BBQ Shapes", 9.00],
# 	["Bread", 2.10],
# 	["Carrots", 0.56],
# 	["Oranges", 3.08]
# ]

# sum = 0

# for item in groceries:
#     quantity = int(input(f"Enter a quantity for {item[0]}: "))
#     sum = sum + (quantity * item[1])
# print(f"Thank you your total is ${sum}")

# Nested Loop Q2
# number = 84
# repeat = 'yes'
# while repeat != 'no':
#     guess = int(input("Make a guess: "))
#     while number != guess:
#         if guess < number:
#             print("Too low! Try again")
#         else:
#             print("Too high. Try again")
#         guess = int(input("Make another guess: "))
#     print("You got it right!")
#     repeat = input("Do you want to play again? Type 'no' to exit the game")