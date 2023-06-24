#Store multiple data points, can take different data types
digits =  [1,2,3,4,5]  #str, int,float,list
# print(list_name)
# print(type(list_name))
#print(len(digits))
#Lists are index based which starts from 0.
#print(digits[5]) #IndexError: list index out of range
#print(digits[-1]) #give very last element
#Slicing a list
#print(digits[0:4]) # Start (inclusive)and End index(exclusive)
#print(digits[-2:5]) 
#print(digits[0:5:2]) 

digits =  [1,2,3,4,5]
#print(digits)
digits.append(6)
#print(digits)
popped_element = digits.pop(0)
#print(popped_element)
digits[1] = 90
#print(digits)

letters = ['a','b','c','d',['Emily','Julie']]
#print(letters[4][0]) #Get the first list, then get the first element from second(inner) list
outer_list = letters[4]
print(outer_list[0])
# Check if 'a' exists in list letters
# if 'a' in letters:
#     print("It is in the list")