import csv
import logging

#logging set up
logging.basicConfig(filename = "Task3_Logged_data.log", level = logging.ERROR, format = "%(asctime)s - %(levelname)s - %(message)s")


# reading the file one row at a time 
with open("Task3.csv","r") as file:
    reader = csv.DictReader(file) 
    
    for row_number, row in enumerate(reader,start = 1):
            print(f"checking row {row_number}")
# checking the missing values
            invalid_row = False
            for key,value in row.items():
                if value is None or value.strip() == "":
                    print(f"Row {row_number}: Missing value in {key}")
                    logging.error(f"Row {row_number}: missing value in {key}")
                    invalid_row = True
                    
            if invalid_row:
                continue
            
            age_text = row["age"]
            try:
                age = int(age_text)
                print(f"valid row {row_number}")    

            except:
                print(f"ROw {row_number}, has invalid age: {age_text}")
                logging.error(f"Row {row_number}, has invalid age: {age_text}")
                continue
            