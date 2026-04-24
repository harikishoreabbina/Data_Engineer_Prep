import csv
import json

Task1_cleaned_data = []
duplicates = []
seen_product_names = set()
# reading the data
with open("Task1.csv", "r") as file1:
    reader = csv.DictReader(file1)
#cleanign the data and removing the spaces and lower cases
    original_header = reader.fieldnames
    cleaned_header = [header.strip().lower().replace(" ", "_") for header in original_header]

    for i in reader:
        cleaned_row = {} # saving new data in cleaned_row
# Replacing the old data with new cleaned data
        for old, new in zip(original_header, cleaned_header):
            cell_value = i[old]
            
            if cell_value is None:
                value = ""
            elif cell_value == "":
                value = ""
            else:
                value = cell_value.strip()
# checking fot the empty rows and filling with "0"
            if value == "":
                if new == "price":
                    value = "0"
                elif new == "stock":
                    value = "0"
                else:
                    value = "unknown"

            cleaned_row[new] = value

        # Duplicate check (by product_name)
        product_name = cleaned_row["product_name"].lower()

        if product_name in seen_product_names:
            duplicates.append(cleaned_row)
            continue
#
        seen_product_names.add(product_name)
#adding the cleaned into Task1_cleaned_data
        Task1_cleaned_data.append(cleaned_row)


# Print duplicates
print("Duplicates:")
for d in duplicates:
    print(d)

# Write cleaned data to JSON
with open("Task1_cleaned_data.json", "w") as file2:
    json.dump(Task1_cleaned_data, file2, indent=4)
print("Cleaned data saved to Task1_cleaned_data.json")