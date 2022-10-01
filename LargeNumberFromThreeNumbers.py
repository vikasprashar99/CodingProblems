# Program To find the largest number among the three numbers in python

# Lets Assume
n1 = 11
n2 = 15
n3 = 13

# If you want take input from user then uncomment following comments
#n1 = float(input("Enter first number: "))
#n2 = float(input("Enter second number: "))
#n3 = float(input("Enter third number: "))

if (n1 >= n2) and (n1 >= n3):
   largest = n1
elif (n2 >= n1) and (n2 >= n3):
   largest = n2
else:
   largest = n3

print("The largest number is", largest)
