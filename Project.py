# Each Vendor has different Field names
# So we have fix a single format and should map the all vendor data accordingly

import csv
import json

Final_Cleaned_data = [] # to store the Final cleaned data 
seen_products = set() # for duplicates 

def reading(file_name):
    data = []
    
    with open (file_name, "r") as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            data.append(row)
            
    return data
    

# Cleaning the data from Vendor 

def cleaning(data,mapping):
    cleaned = []
    
    for row in data:
       
        price = row[mapping["price"]]
        
        #checking the missing price values  
        if price == "" or price is None:
            price = "0"
        
        cleaned.append({
            "product_id": row[mapping["product_id"]],
            "product_name": row[mapping["product_name"]],
            "category": row[mapping["category"]],
            "price": price
        })# mapping all the fieldheader to standard format
    return cleaned


# function to remove the duplicate values 
def duplicates(data):
    result = []
    duplicates_list = []
    seen_products = set()

    for row in data:
        prodid = row["product_id"]

        if prodid in seen_products:
            duplicates_list.append(row)
            continue

        seen_products.add(prodid)
        result.append(row)

    return result, duplicates_list

# Mapping with every vendor data

vendor1_map = {
    "product_id": "Product ID",
    "product_name": "Product Name",
    "category": "Category",
    "price": "Price"
}

vendor2_map = {
    "product_id": "id",
    "product_name": "name",
    "category": "category",
    "price": "price"
}

vendor3_map = {
    "product_id": "item_code",
    "product_name": "item_name",
    "category": "item_group",
    "price": "cost"
}

# read files
v1 = reading("Mini Project/Vendor1.csv")
v2 = reading("Mini Project/Vendor2.csv")
v3 = reading("Mini Project/Vendor3.csv")

#cleaningt the file using function
v1_clean = cleaning(v1, vendor1_map)
v2_clean = cleaning(v2, vendor2_map)
v3_clean = cleaning(v3, vendor3_map)

# merging the 3 vendor datas
final_data = v1_clean + v2_clean + v3_clean

# removing the duplicates using the function
Final_Cleaned_data, duplicates_data = duplicates(final_data)

for row in Final_Cleaned_data:
    print(row)
    

print("\n--- DUPLICATE RECORDS ---\n")
for row in duplicates_data:
    print(row)
    
    
# Loading the value into json file

path = "Mini Project/Final_Cleaned_Data.json"

with open(path, "w") as json_file:
    json.dump(Final_Cleaned_data, json_file, indent=4)