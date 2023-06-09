# Conditionals Exercises
sara_has_helmet = False
rei_has_rope = False

# Q1
#if sara_has_helmet == True:
    # print("Let's send it!")
# else sara_has_helmet == False:
#     print("No way, my brain is my moneymaker!")

# Q2
# if sara_has_helmet == True and rei_has_rope == True:
#     print("Let's send it!")
# if sara_has_helmet == False and rei_has_rope == True:
#     print("No way, my brain is my moneymaker")
# if sara_has_helmet == True and rei_has_rope == False:
#     print("Who's unprepared now, Rei?")
# if sara_has_helmet == False and rei_has_rope == False:
#     print("I guess let's just go hiking")

# Q3
# light_colour = "Red"
# car_detected = True


# if light_colour == "Red" and car_detected == True:
#     print("Flash!")
# else:
#     print("Do Nothing")

# Q4
# user_height = int(input("How tall are you?"))
# if user_height >= 120:
#     print("Hop on!")
# else:
#     print("Sorry, not today")

# Q5
# username = input("enter your username?")
# password = input ("enter your password")
# if username == "lucyg" and password == "quartzgleam?1":
#     print("Logged in successfully")
# else:
#     print("Access denied")

# Lists Exercises
# Q1
foods = ["orange","apple","banana","strawberry","grape","blueberry",["carrot", "cauliflower", "pumpkin"],"passionfruit","mango","kiwifruit"]
# print(foods.pop())
# print(foods[0:3])
# print(foods[7:9+1])

# Q2
variable_lyrics = [["Monica", "in my life"],["Erica", "by my side"],["Rita's", "all I need"],["Tina's", "what I see"],["Sandra", "in the sun"],["Mary", "having fun"],["Jessica", "here I am"]]
opening_lyrics = "A little bit of "
lyrics = opening_lyrics + variable_lyrics[0][0] + " " + variable_lyrics[0][1]
# print(lyrics)

# Q3
name_list = []

name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")
name3 = input("Enter the third name: ")

name_list.append(name1)
name_list.append(name2)
name_list.append(name3)

# print("Name list:", name_list)