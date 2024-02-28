#Data types
#strings
# print("hello"[3])

#integer-- numbers without decimals..whole numbers
# print(123+345)
#234_234

#float--34.5..

#Boolean- true or false

# name = len(input("What is your name?\n"))
#print("Your name has" + name + "characters")

#type()function can be used to check the datatype of characters
#type casting is changing from one datatype to another
# new_name_we_want = str(variable we want to convert) 

# new_name = str(name)

# print("Your name has" +" "+ new_name +" " + "characters")

# a = str(123) #string data type
# print(type(a))

# a = 123   #integer data type
# print(type(a))


# a = float(123)  #Answer is 323 since it is a float
# print(a + 200)

#Mathematical operations
# 3 + 5....7-3....6/4....3**3(3 exponent 3) 
#Python evaluation with priority ..PEMDAS
#parentheses exponents multiplication division
#  Thonny.org for visualization..

# Calculating Body Mass index.

height = input("Please enter your height in meters\n")
weight = input("Enter your weight in kg\n")


new_weight = int(weight)
# print(type(new_weight))

new_height=float(height)
bmi = new_weight/(new_height**2)#we must note since for bodmas parentheses is evaluated before the rest we need to specify


# print(type(bmi))
new_bmi=str(bmi)
print("Your BMI is" + " " + new_bmi )

#Round function is used to round numbers
#print(round(8/3,2))#2 at the end is the number of places we want to round

#manipulating values based on previous values
#score = 0 

#user scores a point 
#score += 1 #score = score + 1

#F-string----mixing different datatypes to be displayed
#print(f"your score is {score}, your height is {height}") put the variable in curly braces and begin the quotation with f


#coding exercise
age = input("please enter your age\n")

new_age = int(age)

years_left = 90 - new_age 

weeks_left = years_left * 52

print(f"You have {weeks_left}+" " + weeks left to live")
