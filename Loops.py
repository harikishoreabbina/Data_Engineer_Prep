# A LOOP is a thing wihch is used to repeat the same work repetedly based
# on the required condition

# FOR loop

fruits = ["apple","banana","mango"]
for i in fruits:
    print(i)


num = [1,2,3,4,5,6,]
for i in num:
    print(i)
    
    
cities = ["chicago", "Dallas", "Seattle"]
for i in cities:
    print(i)
    
    

# while loop
a = 0

while a < 8: # while loops will  execuit the code until the given size
    print(a) 
    a += 1   # if we do not give the increment the loop will run infinitly
    
    
# Nested Loop
# this is a loop inside a loop

for i in range(5):
    for j in range(2):
        print(i, j)

# Why loops are useful when reading a CSV file

# according to my understanding by using loops we check each every row
# we can go through every row and perform cleaning, transformations.
# with out loops we have do deal manually each and every row 
