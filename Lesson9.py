# #python dictionaries
# #{key:value}
# #eg
# programming_dictionary = {
# "bug": "An error in a program to prevent it from running"}
# #To select an item from the dictionary

# print(programming_dictionary["bug"])#use the right datatype when retrieving

# #adding new items
# programming_dictionary["Loop"] = "doing something repeatedly"
# print(programming_dictionary)

# #You could also create an empty dictionary and add items later
# #editing an entry

# programming_dictionary["bug"]= "a moth in your computer"

# #looping through a dictionary
# for thing in programming_dictionary:
#     print(thing)#just prints the key
#     print(programming_dictionary[thing]#prints key and value)


# student_scores= {
#     "harry" : 81,
#     "ron": 78,
#     "hermione": 99,
#     "draco": 74,
#     "neville": 62,
# }

# student_grades={}
# for student in student_scores:
#     score = student_scores[student]
#     if score > 90:
#         student_grades[student] = "outstanding"
#     elif score>80:  
#         student_grades[student] = "welldone"
#     elif score > 70:
#         student_grades[student] = "acceptable"
#     else:
#         student_grades[student] = "fail"          

# print(student_grades)
 

#nesting lists and dictionaries
capitals = {
    "france": "paris",
    "germany" : "berlin",
}
travel_log ={#dictionaries have just one key so we need to use a nested list to keep more than one vaalue in a dictionary
    
"france": ["paris","lists","dijon"]
}