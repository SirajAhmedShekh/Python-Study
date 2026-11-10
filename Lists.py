## Lists in Python (mutable /(add, remove and change items))
# Ans => A built-in data type that stores set of value
# it can store elements of different types (integer, float, string, etc.)

# marks = [87, 64, 33, 95, 76]    # marks[0], marks[1]...
# print(marks)
# print(type(marks))

# student = ["siraj", 26, "Mumbai"] #student[0], student[1]
# print(student)
# print(student[0])    # "siraj",  allowed in python
# print(len(student))   # returns length
# student[0] = "shaikh"
# print(student)




## List Slicing    => ending idx is not included.

# Syntex of slice
# list_name[starting_idx : ending_idx]

# num = [20, 40, 30, 60, 70]  # [20, 40, 30, 60, 70]
                              #  -5  -4  -3  -2  -1
# print(num[1:4])        # [40, 30, 60]
# print(num[:4])         # [20, 40, 30, 60]
# print(num[1:])         # [40, 30, 60, 70]
# print(num[-3:-1])      # [30, 60]
# print(num[:-1])        # [20, 40, 30, 60]
# print(num[-3:])        # [30, 60, 70]

## List Methods 

# list = [2, 1, 3]

# list.append(4)             # adds one element at the end.
# print(list)                # [2, 1, 3, 4]

# list.sort()                # sorts in ascending order.
# print(list)                # [1, 2, 3, 4]

# list.sort(reverse= True)   # sorts in descending order.
# print(list)                # [4, 3, 2, 1]

# list.reverse()             # reverses list
# print(list)                # [1, 2, 3, 4]

# list.insert(1, 5)          # insert element at index
# print(list)                # [1, 5, 2, 3, 4]    

# list2 = [2, 1, 3, 1]

# list2.remove(1)              # removes first occurrence of element
# print(list2)                 # [2, 3, 1]

# list2.pop(2)                 # removes element at idx
# print(list2)                 # [2, 3]

## Tuples in Python (Immutable / cannot be changed after creation)
# Ans => A built-in data type that lets us create immutable sequences of value.

tup = (50, 20, 80, 70, 30)

# mt_tup = ()      # valid tuples
# mt_tup = ("siraj",)      # valid tuples
# print(type(mt_tup))      # (,) Commas are required after single values in tuples.

# tup[0] = 10           # 'tuple' object does not support item assignment
# print(type(tup))
# print(tup[0])
# print(tup[1])

## Slicing in Tuple

# print(tup[1:3])         # as string

## Tuple Methods

# tup1 = (2, 3, 1, 4, 2, 1, 5, 1)

# print(tup1.index(5))        # returns index of first occurrence
# print(tup1.index(4))
# print(tup1.count(1))        # counts total occurrence
# print(tup1.count(2)) 

## MINI PROJECT PRACTICE

# Q 1. WAP to ask the user to enter names of thier 3 favoirite movies & store them in a list.

# movies = []

# type - 1
# m1 = input("enter first movie name: ")
# m2 = input("enter second movie name: ")
# m3 = input("enter third movie name: ")

# movies.append(m1)
# movies.append(m2)
# movies.append(m3)

# type - 2
# mov = input("enter first movie name: ")
# movies.append(mov)
# mov = input("enter second movie name: ")
# movies.append(mov)
# mov = input("enter third movie name: ")
# movies.append(mov)


# type - 3
# movies.append(input("enter first movie name: "))
# movies.append(input("enter second movie name: "))
# movies.append(input("enter third movie name: "))
# movies.append(input("enter forth movie name: "))
# movies.append(input("enter five movie name: "))

# print(movies)





