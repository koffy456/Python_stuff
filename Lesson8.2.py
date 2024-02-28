#functions with multiple inputs

# def greet_with(name,location):
#     print(f"hello, {name} ")
#     print(f"What is it like in {location} ?")


# greet_with("kofi", "Accra")
# #positional argument occurs when we do not specify where arguments should be
# #keyword arguments we specify which parameter we want our argument to be

# greet_with(name="kofi",location="Accra") 

#Exercise 
#You are painting a wall. 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you will need to buy
# import math





# def paint_calc(height,width,cover):


#     num_cans= (height*width)/cover
#     round_up_cans = math.ceil(num_cans)
#     print(f"You'll need{round_up_cans} cans of paint.")


# test_h =int(input("What is the height of your wall")) #height of wall
# test_w = int(input("What is the width of your wall"))#width of wall
# coverage=5


# paint_calc(height=test_h, width=test_w,cover=coverage)



#prime number checker

def prime_checker(number):
    is_prime = True
    for i in range(2,number):
        if number  %  i == 0 :
         is_prime = False
    if  is_prime:
          print("It is a prime number.")
    else:
        print("It is not a prime number")

n=int(input("Check this number"))
prime_checker(number=n)