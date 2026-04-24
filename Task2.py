import csv

# expected column structure
expected_columns = ["product_id", "product_name", "category", "price", "stock"]


def validation_function():

    missing = []  # store missing columns
    count = 0     # row counter

    with open(r"C:\Users\Harik\Desktop\Data Engineer Prep\Week 1\Task 2\Task2.csv", "r") as file:
        reader = csv.DictReader(file)

        original_columns = reader.fieldnames

        # schema validation
        # checking if all expected columns are present in file
        for c in expected_columns:
            if c not in original_columns:
                missing.append(c)  # we will add all the missing fields to missing[] file and check the length 

        # counting rows in file
        for row in reader:
            count += 1
        print("total numner of rows in file are :",count)

    # if no missing columns, file is valid
    if len(missing) == 0:
        valid = True
    else:
        valid = False

    result = {
        "valid": valid,
        "missing_columns": missing,
        "rows": count
    }

    return result

print(validation_function())
# in our data Stock column is missing so the schema is invalid