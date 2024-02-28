#namespace local and global scope
#local scope--exists within functions

def drink_potion():
    potion_strength = 2
    print(potion_strength)
drink_potion()    

#global variables are defined on top of functions and are available everywhere
#python does not have block scope especially with the various loops.
#to modify a global scope just add the keyword global to it in a local scope and use it from there

#global scopes are very important for defining the value of constants and are uppercase
