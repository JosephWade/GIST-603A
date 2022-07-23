# -------------------------------------------------------------------------------
# Name:        Assignment1_withHints.py
# Purpose:     Script for Assignment1
# Author:      Dr. Yoganand Korgaonkar
# Student Name: Joseph Wade
# -------------------------------------------------------------------------------

# CORRECTIONS ARE ON LINES 69, 78 & 140
print("The Corrections are on lines 69, 78 and 140.")
#################################################################################
# TODO Q1: Your Full Name (5 points)
#  a) Create a variable to store your full name as a string and print it. (5 points)
# Please add comments to explain what you are coding
# Write your code below

# HINT: New variable that stores your full name as a string
FullName = "Joseph Wade"
# JW: I am assigning my Name as a string variable, or FullName

print(FullName)
# JW: I am printing my full name

# HINT: Print the string in the required format using the variable.
print('My name is {0}!'.format(FullName))
# JW: Using the .format() method I printed out my full name.
# The .format() method isn't exactly necessary since both the variable and the print statement are strings
# End Q1
#################################################################################
# TODO Q2: Formatting strings (10 points)
#  Use string concatenation or formatted strings (.format() or f-strings).
#   a) Create a variable to store the following string using the given variables.
#      Use single quotes to define the entire string literal. Your new string
#      must preserve the double quotes. (2 points)
#         "PARCEL_ID" = 143567
#   b) Create a variable to store the following string using the given variables.
#      Use double quotes to define the entire string literal. You new string
#      must preserve the double and single quotes. (2 points)
#          "OWNER" = 'City of Tucson'
#   c) Use the given variables to print the following string exactly as it is
#      shown below. (2 points)
#         Parcel 143567 is owned by 'City of Tucson'.
#   d) Use the given variables to print the following string exactly as it is
#      shown below. (2 points)
#         The area of parcel 143567 is 8652.35 square feet.
#   e) Use the given variables to print the following exactly as it is shown
#      below. (2 points)
#            PARCEL_ID |     OWNER      | AREA_SQFT
#               143567 | City of Tucson |   8652.35
#      HINT: Use two print statements and the justify methods for alignment. You will
#            also have to use the str() function to convert the numbers to string in
#            order to use the justify methods.
# Please add comments to explain what you are coding
# Write your code below

# Use the following variables to complete the tasks.
# The following are made-up column names and attributes from a made-up feature class.
column_id = "PARCEL_ID" # Name of column that stores the parcel id
column_owner = '"OWNER"' # Name of the column that stores the owner information for that parcel
column_area_sqft = "AREA_SQFT" # Name of the column that stores the area in square feet
par_id = 143567 # An example parcel id
par_area_sqft = 8652.35 # Area of the example parcel id
# JW: I had to add Double quotes around the single quotes, so the single quotes would be included in the string
par_owner = 'City of Tucson'# Owner of the example parcel id


# HINT: New variable that stores the string as: "PARCEL_ID" = 143567
# JW: I had to add single quotes, around the double quotes, so the double quotes would be a part of the string variable
# storagename = ' "PARCEL_ID = 143567" ' (Original Code)

# JW CORRECTION: I corrected the code to actually use the variables
storagename = '"{0}" = {1}'.format(column_id,par_id)

# HINT: New variable that stores the string as: "OWNER" = 'City of Tucson'
# JW: Both variables were combined, to create the desired result.
storageowner = column_owner +" = "+ par_owner

# HINT: Print the string as: Parcel 143567 is owned by 'City of Tucson'.
# JW: The .format method was used so the integer value of par_id could be combined with the string
# JW: CORRECTION: I changed the par_owner variable back to the original given variable, and used single quotes in " "
storageparcel = "Parcel {0}".format(par_id) +" is owned by '"+ par_owner+"'"
print(storageparcel)

# HINT: Print the string as: The area of parcel 143567 is 8652.35 square feet.
# JW: The .format method was used to the two integer values could be printed out as a string
storagearea = "The area of parcel {0} is {1} square feet.".format(par_id,par_area_sqft)
print(storagearea)

# Print the two lines as shown in the question.
# JW: The strip method was necessary to remove the quotes,
#   and the str() method was necessary to change the int values into string values
print(column_id.rjust(9) +" | " + column_owner.strip('"').center(15) + " | " + column_area_sqft.rjust(9))
print(str(par_id).rjust(9) +" | " + par_owner.strip("'").rjust(15) + " | " + str(par_area_sqft).rjust(9))

# End Q2
#################################################################################
# TODO Q3: Math Operations (20 points)
#  a) Create two variables to store any two integers and one variable to store
#     any floating point number of your choice. (3 points)
#  b) Determine the data type of each variable from (a) using Python code. Store
#     the data types in variables. You should have three new variables for each
#     of the numbers in this task. (3 points)
#  c) Create a new variable to store the multiplication of all three numbers
#     using the variables from (a). (2 points)
#  d) Create a new variable to store the addition of all three numbers
#     using the variables from (a). (2 points)
#  e) Use the .format() method and variables from (a), (b), (c) & (d) to print
#     the output in the following format. (10 points)
#       Integer 1 = <from (a)> | Type = <from (b)>
#       Integer 2 = <from (a)> | Type = <from (b)>
#       Float 1 = <from (a)> | Type = <from (b)>
#       Multiplication Result = <from (c)>
#       Addition Result = <from (d)>
# Please add comments to explain what you are coding
# Write your code below

# HINT: Create three variables - 2 for integers and 1 for floating point
# JW: I purposely mispelled float as flot to make it shorter. I'm not really sure why......
int_one = 111
int_two = 2222
flot_one = 11.1

# HINT: Determine the data type and store into three new variables for each of the above
# JW: By adding a decimal point to a value, it automatically makes it a float
int_one_type = (type(int_one))
int_two_type = (type(int_two))
flot_one_type = (type(flot_one))

# HINT: Create a new variable to store the multiplication of the three variables from (a)
multi = int_one * int_two * flot_one
# JW: Below I am testing my new format() print method in addition
# print ("All three variables multiplied together = {0}".format(multi))

# HINT: Create a new variable to store the addition of the three variables from (a)
# JW: adding the variables together will automatically make a float value due to flot_one
addi = int_one + int_two + flot_one
# HINT: Print the given lines from (e) in the same format using the .format() method
# JW: The .format() method is again necessary to combine strings and the FLOAT value
# print ("All three variables added together = {0}".format(addi))


# JW CORRECTION: I printed out the code as mentioned above, instead of how I did earlier.
print("Integer 1 = {0} | Type = {1}".format(int_one, int_one_type))
print("Integer 2 = {0} | Type = {1}".format(int_two, int_two_type))
print("Float 1 = {0} | Type = {1}".format(flot_one,flot_one_type))
print("Multiplication Result = {}".format(multi))
print("Addition Result = {}".format(addi))
# End Q3
#################################################################################
# TODO Q4: Strings (15 points)
#  Given the string literal python_string below, perform the following tasks:
#  a) Extract and print the word "gram" from the string. (2 points)
#  b) Extract and print the last four characters from the string. (2 points)
#  c) Extract and print "mm" from the string. (2 points)
#  d) Convert the string to all uppercase characters. (2 points)
#  e) Print the word "program" (all lowercase) from python_string. (2 points)
#  f) Replace the word "with" with "using". (2 points)
#  g) Extract the word "Python" and use one of the justify methods to print the
#     following. (3 points)
#      $$$$$Python$$$$$
# Please add comments to explain what you are coding
# Write your code below

# HINT: Use this variable for all questions
python_string = "Programming with Python"


# HINT: Use slicing to extract and print the word "gram" from the above string
# JW: I sliced from the 4th value to the 8th. Values start at 0, not at 1. So 3 = value 4.
print(python_string[3:7])
# HINT: Use slicing to extract and print the last four characters from the above string
# JW: I went back 4 indexes from the end, and printed out those
print(python_string[-4:])
# HINT: Use slicing to extract and print "mm" from the above string
# JW: I printed out indexes 7 and 8
print(python_string[6:8])

# HINT: Use a method to convert the string to all uppercase characters
# JW: The .upper() method converts all characters to uppercase letters within the string
print(python_string.upper())

# HINT: Use slicing and a method to extract and print the word "program" in all lowercase
# JW: Program takes the first 8 characters, and .lower converts all the characters to lowercase
print(python_string[0:7].lower())

# HINT: Use a method to replace the word "with" with "using"
# JW: .replace() finds the word in the string, and replaces it with the 2nd string
print(python_string.replace("with","using"))

# HINT: Use slicing and a method to print out $$$$$Python$$$$$ using the given string
# JW: I used the center method, and replaced the default space with the money symbol
print(python_string[-6:].center(16,'$'))

# End Q4
#################################################################################
# TODO Q5: Strings & Paths (4 points)
#  Given the string literals below, perform the following tasks:
#  a) Concatenate the workspace and streets_shapefile variables using the + operator
#     to represent the following path. Store the concatenation in a new variable
#     and print the contents of this variable. (2 points)
#       "C:/workspace/gist/assignment1/streets.shp"
#  b) Concatenate workspace and zoning_shapefile variables using the .format()
#     method to represent the following path. Store the concatenation in a new
#     variable and print the contents of this variable. (2 points)
#       "C:/workspace/gist/assignment1/zoning.shp"
# Please add comments to explain what you are coding
# Write your code below

# Given string literals
workspace = "C:/workspace/gist/assignment1/"
streets_shapefile = "streets.shp"
zoning_shapefile = "zoning.shp"

# HINT: Concatenate the two variables using the + operator and store in a new variable
# JW: This is very simple! Combining two strings is straight forward, just use +
combined_1_shapefile = workspace + streets_shapefile
print(combined_1_shapefile)


# HINT: Concatenate the two variables using the .format method() and store in a new variable

# JW: You can concentiate two variables by putting them next to each other like this using the .format() method
combined_2_shapefile = "{0}{1}".format(workspace,zoning_shapefile);

# HINT: Print the contents of the new variable
# JW: Simple printing
print(combined_2_shapefile)

# End Q5
#################################################################################
# TODO Q6: Lists (20 points)
#  a) Create a list with your first and last name as two items. (2 points)
#  b) Using this list, print only your first name. (2 points)
#  c) Create a new variable to store the item at index 1 in the list. Print the
#     contents of this variable. (2 points)
#  d) Remove your last name from the list and print the list. (2 points)
#  e) Add the name of your state to the end of the list. (2 points)
#  f) Add the name of your city before the state name in the list. (2 points)
#  g) Add your last name after your first name in the list. (2 points)
#  h) Print the index of your city name from the list. (2 points)
#  i) Convert the list to a string separated by commas and print it. (4 points)
# Please add comments to explain what you are coding
# Write your code below

# Create a new variable to store your first and last name as two items in a list
# You will use this variable to perform all of the following tasks
name = ["Joseph", "Wade"]

# HINT: Using the above variable, print your first name
# JW: My first name is index 0 (remember 0 = index 1)
print(name[0])

# HINT: Create a new variable to store item at index one from the variable in (a)
# JW: Index one is really the 2nd index, so that is my last name
last_name = name[1]

# HINT: Print the contents of this new variable
print(last_name)

# HINT: Use the del statement or the remove method to remove your last name from the list
# JW: The delete method completeley removes it from the list, after this line in the code
del name[1]

# HINT: Print the contents of the list
# JW: Now only my first name prints out
print(name)

# HINT: Use a method to add the name of your state to the end of the list
# JW: New Mexico is now index 1, since my Last name was removed
name.append("New Mexico")

# HINT: Use a method to add the name of your city before the state name in the list
# JW: Now Albuquerque is index 1, and New Mexico index 2
name.insert(1,"Albuquerque")

# HINT: Use a method to add your last name after your first name in the list
# JW: Now "Wade" is index 1, Albuquerque index 2, and New Mexico is index 3
name.insert(1,"Wade")

# HINT: Use a method to print the index of your city name from the list
# JW: Fancy print out method stating that Albuquerque is index 3
print("The Index of my city is {0}".format(name.index("Albuquerque")))

# HINT: Use a method to convert the list to a string where all words are separated by commas
# JW: The Separating variable is defined as the comma with the space
print(*name, sep = ", ")

# End Q6
#################################################################################
# TODO Q7: Strings, Lists & Paths (16 points)
#  Given the following string literal and list, perform the following tasks:
#  a) Create a variable to store the second item ("parcels") from the list. Print
#     the contents of this variable. (2 points)
#  b) Concatenate the variable workspace and the variable from (a) using the
#     + operator to represent the following path. Store the concatenation in a
#     new variable and print the contents of this variable. (3 points)
#       "C:/workspace/gist/Assignment1.gdb/parcels"
#  c) Create a variable to store the last item ("precipitation") from the list
#     Print the contents of this variable. (2 points)
#  d) Concatenate the variable workspace and the variable from (c) using the
#     .format() method to represent the following path. Store the concatenation
#     in a new variable and print the contents of this variable. (3 points)
#       "C:/workspace/gist/Assignment1.gdb/precipitation"
#  e) Remove the item "geology" from the list and store it in a new variable.
#     Print the contents of this variable. (3 points)
#  f) Remove the first item ("streets") from the list and store it in a new
#     variable. Print the contents of this variable. (3 points)
# Please add comments to explain what you are coding
# Write your code below

# Given string literal
workspace = "C:/workspace/gist/Assignment1.gdb/"
# Given list
list_of_fcs = ["streets", "parcels", "geology", "rivers", "precipitation"]

# HINT: Create a new variable to store the second item from the above list
# JW: The 2nd item is index 1
new_variable = list_of_fcs[1]

# HINT: Print the contents of this new variable
print(new_variable)

# HINT: Create a new variable to store the concatenation of workspace and the new variable
# HINT: from (a). Concatenate using the + operator
# JW: Simple concentiation with +
newer_variable = workspace + new_variable

# HINT: Print the contents of this new variable
print(newer_variable)

# HINT: Create a new variable to store the last item from the above list
# JW: Saying -1 pulls the last item from the list.
last_variable = list_of_fcs[-1]

# HINT: Print the contents of this new variable
print(last_variable)

# HINT: Create a new variable to store the concatenation of workspace and the new variable
# HINT: from (c). Concatenate using the .format() method
# JW: Concentiating the two variables like I did earlier, putting them next to each other in the .format() method
newest_variable = "{0}{1}".format(workspace,last_variable)

# HINT: Use a method to remove the item "geology" from the list and store in a new variable
# JW: I assumed that you wanted the geology variable to be stored, not the list without geology
geology_variable = list_of_fcs.pop(-3)

# HINT: Print the contents of this new variable
print(geology_variable)

# HINT: Use a method to remove the first item from the list and store in a new variable
# JW: The pop() method removes the first item and stores it in a new variable, perfect for this question
first_var = list_of_fcs.pop(0)

# HINT: Print the contents of this new variable
print(first_var)

# End Q7
#################################################################################
# TODO Q8: Errors (10 points)
#  Identify and fix all errors in the following lines of codes.
#  Only fix errors in each line. Do not replace the lines with your own code.
#  Please add comments to explain what you fixed and why.
# HINT: Fix the errors in the code below

# TODO Q8 a) Variable stores integer number. (2 points)
# JW: I rearranged the order so that the variable could properly be assigned
var_pi = 314


# TODO Q8 b) Print the value of Pi (2 points)
# JW: I added str() to turn the integer into a string, so that they could be printed
print( "Pi = "+str(var_pi/100.0) )


# TODO Q8 c) String to store path name to schools shapefile. (2 points)
# JW: Python 3's pathlib fixes the problem of the escaping characters I.E. /a, /t present in this string
#     This is a better solution than the os.path.join() method, as it doesn't require us to put each directory
#     into it's own string in the method call

from pathlib import Path
schools_shp = Path("C:/workspace/gist/arizona/tuscon/schools.shp")

print(schools_shp)
# Hint: What are the three different ways of correctly writing paths in Python?

# TODO Q8 d) Concatenate the two strings (2 points)
# JW: I removed the # Symbol because it makes things into a comment, therefore voiding the variable assigning
#     I also moved the & symbol because it is useless where it was placed, it has to be placed within the quotes
string_1 = "Errors"
string_2 = "& Exceptions"
print(string_1 + string_2)



# TODO Q8 e) Extract the fifth element from the list. (2 points)
# JW: One of the Quotes for Earth Was missing, making the list void, so I added one
# JW: Also, I changed the index from 5 to 4, because that index is out of bounds. Earth = 0, and Heart = 4
captain_planet = ["Earth", "Fire", "Wind", "Water", "Heart"]
print("The fifth element is = " + captain_planet[4])



# End Q8
#################################################################################
# End of Assignment 1
#################################################################################