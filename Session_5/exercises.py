# Q1
import csv

# with open(file="colours_20_simple.csv", mode="r", encoding="utf-8") as my_file:
#     csv_reader = csv.reader(my_file, delimiter=" ")
#     for row in csv_reader:
#         print(row)

# nested_list [['I', 'think', 'dogs', 'are,', 'awesome!']
# ['My,', "dog's", 'name', 'is,', 'Jett!']
# []
# ['I', 'love', 'him!']]
# with open(file="hello.csv", mode="w") as my_file:
#     csv_writer = csv.writer(my_file)
#     csv_writer.writerow(["Hello","Hi"])

# with open(file="2016_pilbara.csv") as csv_file:
#     csv_reader = csv.reader(csv_file)
#     for line in csv_reader:
#         print(line)

colours = []

# Q2
with open(file="colours_20_simple.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        colours.append(row)
        print(colours)

# # for age_group in population:
# #     print(f"{age_group[0]} * {age_group[1]}")

# with open(file="population.csv", mode="w") as csv_file:
#     csv_writer = csv.writer(csv_file,delimiter="-")

#     for age_group in population:
#         # age_group,frequency = age_group
#         # print(age_group)
#         # print(type(age_group))
#         # print(frequency)
#         # print(type(frequency))
#         csv_writer.writerow([age_group[0], age_group[1]])