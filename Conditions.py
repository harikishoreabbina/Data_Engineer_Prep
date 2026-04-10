# CONDITIONALS are used to make decisions based on conditions
#  IF CONDITION
age1 = 70

if age1 >= 18:  # only prints the output if the condition satisfied
    print("Adult")  
   
    
# IF ELSE CONDITION
age2 = 15

if age2 >= 18:      # if IF condition is not satisfied it will go for ELSE condition
    print("Adult")
else:
    print("Minor")
    
# QUICK EXCERCISE
price = int(input("enter the price:"))

if price > 100:
    print(" the price is greater than 100")
else:
    print(" the price is not greater than 100")
    
    
# What happens when a required field is empty
price2 = input("enter the price:")

if price2 == "":
    print("Error, unexpected input")
else:
    print("the price is",price2)