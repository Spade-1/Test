# i = 1
# j= 1
# while i<=5:
#     while j<=i:
#         print("*")
#         j = j+1
#     i= i+1
#     print("\n")

# secret_no = 9
# guess_count = 0
# while guess_count<3:
#     guess = int(input("Guess : "))
#     guess_count +=1
#     if guess==secret_no:
#         print("You won!")
#         break
# else:
#     print("Sorry You Failed!")
# for item in "Python":
#     print(item)

# for item in range(5, 10,):
#     print(item)
# prices = [10, 20, 30]
# total = 0
# for item in prices:
#     total = total+item
# print(f"Total = {total}")

# for x in range(3):
#     for y in range(3):
#         print(f"{x},{y}")

# numbers = [5, 2, 5, 2, 2]

# for x_count in numbers:
#     output = ""
#     for x in range(x_count):
#         output+="x"
# 
#     print(output)

#finding the largest number
# number = [2, 4, 5, 9, 8]
# max = number[0]

# for x in number:
#     if max < x:
#         max = x
# print(f"Largest Number = {max}")

#2D Lists

# matrix = [
#     [2,3,4],
#     [5,4,2],
#     [8,9,10],
# ]

# for row in matrix:
#     for item in row:
#         print(item)

#List Methods
#numbers=[2,3,4,5]
    #To add something in list at the last position
# numbers.append(45)
# print(numbers)
    #to add something in anywhere
# numbers.insert(2, "h")
    #to remove
# numbers.remove(2)
    #to remove all items
#numbers.clear()
# numbers.sort()
# numbers.reverse()
# print(numbers)

#delete duplicate
# numbers = [2,2,3,4,6,7,4,6,7,3,3]
# unique=[]
# for number in numbers:
#     if number not in unique:
#         unique.append(number)
# print(unique)

#unpacking
# coordinate = (1,2,3)

# x,y,z =coordinate
# print(f"{x}{y}{z}")

 #input phone number
# ph = input("Phone Number :")

# digit_mapping = {
#     "0" : "Zero",
#     "1" : "One",
#     "2" : "Two",
#     "3" : "Three",
#     "4" : "Four",
#     "5" : "Five",
#     "6" : "Six",
#     "7" : "Seven",
#     "8" : "Eight",
#     "9" : "Nine"
# }
# output = ""
# for ch in ph:
#     output += digit_mapping.get(ch, "!")+" "
# print(output)

#emoji converter

# message = input(">")

# words = message.split(" ")
# emoji = {
#     ":)" : "😊",
#     ":(" : "😢"
# }
# output = ""
# for word in words:
#     output += emoji.get(word, word)+" "
# print(output)

#function
# def greet_user(f_name, l_name):
#     print(f"Hello {f_name} {l_name}")
#     print("Wlcome abroad!")


# print("Start")
# greet_user(l_name= "Smith", f_name="John")
# print("End")


#Exception
# try:
#     age = int(input("Age : "))
#     income = 2000
#     risk = 2000/age
#     print(age)
# except ZeroDivisionError:
#     print("Age cannot be zero")
# except ValueError:
#     print("Invalid value")
