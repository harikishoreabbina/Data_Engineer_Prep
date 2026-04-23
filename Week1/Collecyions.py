#COLLECTIONS help us to store more than one value

# LISTS
# a list is a built-in data structure used to store multiple items in a single variable
# it keeps the items in order, the are mutable(can be changed) and allows duplicates

Name = ["Hari","Ravi","Ram","Lokesh","Mohan","Vamsi","Rahul","Hari"]

print(Name) # printing the every element in list
print(Name[2]) # printing the 2nd position element( 3rd element)
print(Name[0:3]) # printing the 0th position element to 2nd position element (1st,2nd and 3rd)
print(Name[::2]) # printing every 2nd element(0,2,4,6,8...)
print(Name[::3]) # every 3rd element

for i in Name:  # for loop give helps to print the every element row by row
    print(i)
    
Name.remove("Ram") # removing the the element
print(Name)

# TUPLES
# A Tuples will keep the elements in order, immutable(can not be changed), Allows duplicates
# Tuples aloows different data types
Cities = ("Dallas","Chicago","Normal","Pitman","Glassboro",5,8,8)
print(Cities)
print(Cities[2])
print(Cities[5])
print()

# NAMED TUPLE is like putting labels on each item
# we have to import it from collections module
from collections import namedtuple

Student = namedtuple('Student', ['name','age','Marks'])
                    # typename  [list of the attributes]
exam = Student('hari',24,88)

print(exam.name)
print(exam.age)


# SETS they are unordered and keep only unique values(No duplicates)

Names = {"Hari", "Mark", "elsa", "peter"}
print(Names)

fruits = {"apple", "banana", "pear", "avacado"}
fruits.add("pineapple")
fruits.remove("apple")
print(fruits)
print(len(fruits))


#DICTIONARY
# it store the key-value pairs,

capitals = {"USA":"D.C.", "India": "New delhi", "China":"Bejing","Russia": "Moscow"}

print(capitals["USA"]) # it gives  the value stored under the key name


product = {'id':'190402','nama':'chicken','category':'meat','price':7.99}
print(product['id'])

for i in product.keys():
    print (i)  # printing only the key names
    
# lists uses the positions and dictionary uses the names
# list  is index based, we have to use number
# Dictionary is Key-value based, have to  use name