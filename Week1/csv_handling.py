#CSV Files
# CSV = Comma Seperated Values, it is the most commanly used file format used to store data

import csv

with open("students.csv","r") as file:
    reader = csv.DictReader(file)  # csv.DictReader makes each row as dictionary with column header as keys
    for i in reader:  ## the for loop will print the every row 
        print(i)
            
with open("Cities.csv","r") as file2:
    reader2 = csv.DictReader(file2)
    for i in reader2:
        print(i)
        print(i["name"])  # printing only name coloumn  in the file 
        print(i["column_id"]) # printing the coloumn_id below the name
        break
    
# the output is in Dictionary format {'key' : 'value'}