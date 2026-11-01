# STRING IN PYTHON
# Ans=> string is data type that stores a secquence of characters.
# # basic operations
# 1. Concatenation and length str, ("hello" + "world" => "helloworld" ,).
# str1 = "siraj"
# len1 = len(str1)
# print(len1)

# str2 = "ahmad"
# len2 = len(str2)
# print(len2)

# final_str = str1 + " " + str2
# print(final_str)
# print(len(final_str))

# # INDEXING OF STRING  
# S I R A J   A H M A D  (STRNIG SPACE WILL BE COUNTED IN INDEXING)
# 0 1 2 3 4 5 6 7 8 9 10

# name = "SIRAJ AHMAD"   
# print(name[2])       
# print(name[5])
# print(name[6])
# print(name[8])

# # SLICING OF STRING 
# Ans=> accessing parts of string
# name = "siraj ahmad"
# print(name[1:4])            # IRA
# print(name[0:4])            # SIRA
# print(name[0:5])            # SIRAJ
# print(name[:5])             # SIRAJ [0:5] AUTO FILL INDEX
# print(name[6:10])           # AHMA
# print(name[6:11])           # AHMAD
# print(name[6:])             # AHMAD [6:len(name)] AUTO FILL INDEX
# print(name[6:len(name)])    # AHMAD [6:len(name)]

## Negative Index    (index start of back side -1 not 0)
#  A  P  P  L  E
# -5 -4 -3 -2 -1
# str = "apple"           
# print(str[-3:-1]) 
# print(str[-5:-2]) 
# print(str[-4:-1]) 

## STRING FUNCTIONS

# 1. str.endswith("xyz")     # returns true if string ends with xyz
# str = "i am studying python"
# print(str.endswith("hon"))   # True
# print(str.endswith("ing"))   # False

# 2. str.capitalize()      # capitalize 1st char of sentence
# print(str.capitalize())
# print(str)          # original string nat cheng
# str = str.capitalize()  # cheng original string this way
# print(str)

# 3. str.replace(old, new)   # replace all character of old
# print(str.replace("y", "a"))
# print(str.replace("python", "javascript"))

# 4. str.find(world)    # returns 1st index of 1st character
# print(str.find("y"))
# print(str.find("am"))
# print(str.find("Q"))

# 5. str.count("xyz")     # counts the character of xyz
# print(str.count("t"))
# print(str.count("am"))
# print(str.count("y"))

# # mini program practice
# Q.1 WAP to input user's first name & print its length.
# name = input("enter first name: ")
# print(len(name))

# Q.2 WAP to find the occurrence of '$' in a string.
# str = "hi, i $am a $ symble $45.5"
# print(str.count("$"))



