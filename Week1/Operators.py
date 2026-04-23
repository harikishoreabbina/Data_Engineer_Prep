# OPERATORS :
# they are used to compare or combine values.
# ARITHMRTIC OPERATORS
print("Arithmrtic operators")
a = 3
b = 9
print(a+b)
print(a-b)
print(a*b)
print(a/b)

# COMPARISON OPERATORS
print("Comparison operators")
print(a>b)
print(a<b)  # these kind of operators are used to compare 2 variables and give a TRUE or FALSE
print(a == b) # comparing equal 
print(a != b) # comparing not equal
print(a >= b) # greater than  or equal
print(a <= b) # less than or equal

# LOGICAL OPERATORS
print("Logical Operators")
x = True
y = False
print(x and y)
print(x or y)
# print(x not y)   we can not use "not" to compare to variables,
# it is a unary oprator ( works with one value)
print(not x) 
print( x and not y)

#ASSIGNMENT OPERATORS
print("Assignment operators")
a = 15  #  "=" is assaig value
a += 15  #  add and assign;  a = a + 15
print(a)
b = 15
b -= 15  #  substract and assign; b = b + 15
print(b)
c = 15
c *= 15  #  multiply and assign; c = c * 15
print(c)
d = 15
d /= 15   # divide and assign; d = d / 15
print(d)


# MEMBERSHIP OPERATORS
 # mostly use in loops , lists and strings
print("Membership operators")
numbers = [1, 2, 3]


# IDENTITY OPERATORS
# checks the memory location
print("Identity operators")
H = [1,2]
I = H

print(H is I) # I is also pointing to same list as H

J = [3,4,5]
K = [3,4,5]

print(J is K) # this  is comparing the memory locations, memory location is different
print(J == K) # this  is comparing values, so the values are same


