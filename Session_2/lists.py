#Store multiple data points using lists
#Lists can contain different data types
#Lists are index-based starting from 0
# digits = [1,2,3,4,5]
# print(digits)
# digits.append(6)
# print(digits)
# digits.pop(0)
# print(digits)
# popped_element = digits.pop(0)
# #print(popped_element)
# digits [1] = 90
# print(digits)

# print(list_name)
# print(type(list_name))

# print(digits[4]) #IndexError: there's an index element out of range, fix it
# print(digits [-1]) #gives the very last index item ie. -1 last, -2 second last etc.

#Slicing a list
# print(digits[0:4]) #Start (inclusive) and End index (excluded)
# print(digits [0:5:2])

# print(len(digits)) #Length of list by index total

letters = ['a','b','c','d',['Emily','Julie']] #Nested list
print(letters[4][0]) #Selecting the element then 