# Creating a tip bill generator
print("Welcome to the tip calculator")
bill = input("what was the bill?")

people = input("How many people are paying?")

tip = input("What is the tip for each person?")

new_bill=float(bill)
new_people=int(people)
new_tip = float(tip)

newer_tip = new_tip/100
each_to_pay = new_bill/(new_people)

#Adding tips 

new_each_to_pay = each_to_pay + newer_tip

print(f"Everyone is paying {new_each_to_pay}")
