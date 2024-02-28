#for loops

# fruits = ["Apple", "Banana", "Guava","Melons","Oranges"]

# for shit in fruits: #it has assigned a value called fruits to each element of the list at the top
#     print(shit) 
#     print(shit + " Pie")

#write a program that works out the highest number from a list of numbers.
# student_scores = input().split()

# for n in range(0, len(student_scores)):
#  student_scores[n] = int(student_scores[n])
    


# highest_score = 0
# for score in student_scores:
#     if score > highest_score:
#         highest_score = score
#         # print("highest_score")
# print(f"The highest score in the class is:{highest_score}")  

#range function is used when generating a range of numbers to loop through      
# for number in range(a,b):
# print(number)
# for shit in range(1,20,3):#to include 20 end at 21
#     print(shit)#the third one is the step
# total = 0
# for number in range(1,51):
#    total = total + number
#    print(total) an accumulator

target = 100
for number in range(1, target + 1):
   if number % 3 ==0 and number % 5 == 0:
      print("FizzBuzz")
   elif number % 3 ==0:
      print("Fizz")
   elif number % 5 == 0:
      print("Buzz")  
   else:
      print(number)    


      