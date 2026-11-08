
## CONDITIONAL STATEMENT

##  if-elif-else (SYNTAX)
#     if(condition):
#          Statement 1
#     elif(condition):
#         Statement 2
#     else:
#        Statement N

# age =27

# if(age >= 18):
#     print("can vote")
# else:    
#     print(" cannot vote")


# light = "red"

# if(light == "red"):
#     print("stop")
# elif(light == "green"):
#     print("go")
# elif(light == "yellow"):   
#     print("look")
# else:
#     print("light is broken")    

## EXAMPLE.

# 1. Grade student based on marks.

# marks = int(input("enter your marks: "))

# if(marks >= 90):
#     grade = "A"
# elif(marks >= 80 and marks < 90):
#     grade = "B"
# elif(marks >= 70 and marks < 80):
#      grade = "C"
# elif(marks >= 50 and marks < 70):
#     grade = "D"
# else:
#      grade = "Fail"
     
# print("Grade of tha student => ", grade)

## NESTING CONDITION EXAMPLE

# 1. man drive based on age.
 
# age = 80

# if(age >= 18):
#     if(age >= 60):     #----->  nested condition for age limit
#         print("can not drive")
#     else:
#         print("can drive")
# else:
#     print("can not drive")

## MINI PROJECT PRACTICE

# Q 1. WAP to check if a number by the user is odd or even.

# num = int(input("enter your number: "))

# if(num % 2 == 0):
#     number = "this is even number"
# else:
#     number = "this is odd number"
    
# print(number)

# Q 2. WAP find the greatest of 3 numbers entered by user.

# n1 = int(input("enter first number: "))
# n2 = int(input("enter second number: "))
# n3 = int(input("enter third number: "))

# if(n1 > n2 and n1 > n3):
#     print("n1 is greater: ",n1)
# elif(n2 > n3):
#     print( "n2 is greater ",n2)
# else:
#     print("n3 is greater: ",n3)

# Q 3. WAP find the greatest of 4 numbers entered by user.

# a = int(input("enter first number: "))
# b = int(input("enter second number: "))
# c = int(input("enter third number: "))
# d = int(input("enter forth number: "))

# if(a >= b and a >= c and a >= d):
#     print("a is greater: ",a)
# elif(b >= c and b >= d):
#     print("b is greater: ",b)
# elif(c >= d):
#     print("c is greater: ",c)
# else:
#     print("d is greater: ",d)

# Q 4. WAP to check if a number is a multiple of 7 or not.

# a = int(input("enter your number: "))

# if(a % 7 == 0):
#     print("number is a multiple of 7: ",a)
# else:
#     print("number is not a multiple of 7: ",a)


