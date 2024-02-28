# print("Welcome to the roller coaster!")
# height = input("Please enter your height: ")
# new_height = int(height)

# if new_height >= 120:  #if follows a condition and then a colon then the else statement also ending with a colon.
#     print("Have a nice ride!")
#     age = int(input("Please enter your age: "))
#     if age < 12:
#         print("Your ticket is $5")
#     elif age <= 18:
#         print("Your price is $7")        
#     else:
#         print("Your ticket is $15")    
# else:
#     print("Please grow taller before you can ride!") 

#Comparison operators
#== - Equal to
#!= - Not equal to
# = --Assigning a value
# == -- Comparing two values
    
#Write a program to determine whether the input of a user is an even number.

# print("Welcome to the even number detector")
# number = int(input("Please enter a number: "))

# if number % 2 == 0 :
#     print("Congratulations this is an even number!!")
# else:
#     print("Sorry this is an odd number..better luck next time!")  

#Nested if statements and elif statements
#  if condition :
#     print("message")
#     if another condition:
#       print("message")
#     elif:
#     print("message")
# else:

#multiple if statements
# You could set a variable to zero and make changes to it in the code later under the various other conditions
# Eg.. bill = 0     
    
print("Thank you for choosing python pizza deliveries!")
pizza_size = input("What pizza size do you want? S, M or L")
pepperoni =input("Do you want pepperoni? ..Y or N")
extra_cheese = input("Do you want extra cheese?")
bill = 0 # this keeps track of all purchases to be made by each customer

if pizza_size == "S":
    bill += 15
elif pizza_size == "M": #this whole section deals with pizza size so the else statement can end without any sentence
    bill += 20
else:
    bill += 25


# For the pepperoni section, we need to use nested ifs since the decision will be added to the size
if pepperoni == "Y":
    if pizza_size == "S":
      bill = bill + 2
    else:
        bill = bill + 3

if extra_cheese == "Y":
    bill += 1         


print(f"Your final bill is: ${bill}. ")

#Logical operators
# for AND -- if one is false all is false
# for OR -- if one is true all is true 