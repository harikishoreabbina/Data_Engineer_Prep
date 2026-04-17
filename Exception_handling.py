# EXCEPTION HANDLING
#    it gives us the backup plan,
#    insted of letting it crash when their is a error or broken data

age_text = "Hari"  # the given input is string

try:                        # in try block we are coding to convert text into int
    age = int(age_text) 
    print(age)
except:                     # in except block we are giving a solution if the try block fails 
    print("Invalid input")  #  insted of crashing the program it prints invalid input
    
    
    
price_text1 = input()       # giving 2 inputs
price_text2 = input()

for i in [price_text1, price_text2]: # usinf for loop to check all the price_texts
    try:                             # in try block price is converting into float
        price = float(i)
        print("Converted price: $", price)
    except:                         #  in except we are giving the sloution if the try block fails
        print("Invalid input: ", i)
        
# if we don't use try and except the program crashes after firts error
# the Second input never runs

# in a data pipeline try and except allows the processing of multiple inputs safely by handling the errors
# insted of failing the entire process
# by this we are not hiding the error, insted we are detecting it, recording it and continuing the process