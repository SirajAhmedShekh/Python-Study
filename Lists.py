## Lists Of Python
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

list = [2, 1, 3]

list.append(4)             # adds one element at the end.
print(list)                # [2, 1, 3, 4]

list.sort()                # sorts in ascending order.
print(list)                # [1, 2, 3, 4]

list.sort(reverse= True)   # sorts in descending order.
print(list)                # [4, 3, 2, 1]

list.reverse()             # reverses list
print(list)                # [1, 2, 3, 4]

list.insert(1, 5)          # insert element at index
print(list)                # [1, 5, 2, 3, 4]    



