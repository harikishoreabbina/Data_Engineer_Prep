# FUNCTIONS
# a funciton is a BLock of code whihc can be used again and again whenever you need

def print_name(): #defining function
    print("Hari")
    
print_name()
 
 
def clean_age(age): #defining function with arguments
    if age == "":  #if input is empty return value 0
        return 0
    return int(age) #else return the age text into number

value = clean_age("25") # here we are calling the function and storing it in value variable
print(value)

#QUICK EXCERCISE
def upper_case(name): # defining the function with name as arguments
    print(name.upper()) # converting the lower case into upper case by using ".upper()" function

testing = input(str("enter the name:" )) # giving a user input string 
upper_case(testing)

#it is better to use functions because, BY using functions it improves the readability and the structure of the code. 
# if any change or bug needed to be fixed, only need to be maid in one place rather than across the multiple code blocks.
#it is important in large-scale applications like data pipelines, in which transformation logic may be applied multiple times.



def cleaning(number):
    if number == "":
        return "N/A"
    return number

test = input("enter the number:")
result = cleaning(test) 
print(result)