# -------------------------------------------------------------------------------
# Name:        Assignment2_withoutHints.py
# Purpose:     Script for Assignment2
# Author:      Dr. Yoganand Korgaonkar
# Student Name: Joseph Wade
# -------------------------------------------------------------------------------

# CORRECTIONS WERE MADE ON LINES 184, 252, 266, 309
print("Lines 184, 252, 266 and 309 were Corrected!")
#################################################################################
# TODO Q1: Check if file exists (5 points)
#   a) Create a variable to store a file and its path. You may use any file and
#      path to test your code (1 point)
#   b) Using conditional statements, the arcpy.Exists() function, and the above
#      variable, check if the file exists. (2 points)
#   c) Print appropriate messages to indicate whether the file exists or
#      not. (2 points)
# Please add comments to explain what you are coding
# Write your code below

# Imports
from pathlib import Path
import os

# Input file
input_file = Path("C:/workspace/gist/arizona/tuscon/test_file.shp")

# Check if the files exists
if(os.path.isfile(str(input_file))):
    # JW: Print message if file exists
    print("The file exists")
else:
    # JW: Print message if file does not exist
    print("The file does NOT exist")








# End Q1
#################################################################################
# TODO Q2: Comparing numbers (10 points)
#   Using the given two integer variables, conditional statements and logical
#   operators:
#   a) Add the two numbers if both are less than 20.
#       Print the result in an appropriate format. (5 points)
#   b) Multiply the two numbers if any one of them is greater than 50.
#       Print the result in an appropriate format. (5 points)
#   Test your code using the following combinations of var_a and var_b.
#   You should get the following results
#   var_a = 5, var_b = 10 -> Addition = 15, Multiplication = N/A
#   var_a = 5, var_b = 25 -> Addition = N/A, Multiplication = N/A
#   var_a = 25, var_b = 25 -> Addition = N/A, Multiplication = N/A
#   var_a = 60, var_b = 70 -> Addition = N/A, Multiplication = 4200
#   var_a = 60, var_b = 15 -> Addition = N/A, Multiplication = 900
# Please add comments to explain what you are coding
# Write your code below

# Two variables that store integers
# You may change their values to test your code
var_a = 60
var_b = 15


# JW: Check if BOTH numbers are less than 20 using an if statement
if (var_a < 20) and (var_b < 20):
    var_addition = var_a + var_b
else:
    # JW: If both aren't less than 20, then var_addition will be 0
    var_addition = "N/A"
# JW: Print out the variable var_addition, it's value will be determined by the if statement, and is outside of it
print ("var_a = {0}, var_b = {1} -> Addition = {2}".format(var_a,var_b,var_addition))

# JW: Check if either variable is greater than 50, not both with the OR statement
if (var_a > 50) or (var_b > 50):
    var_multiplied = var_a * var_b
else:
    # JW: If one of the variables isn't greater than 50, then var_multiplied will be 0
    var_multiplied = "N/A"
# JW: Print out the variable var_multiplied, it's value will be determined by the if statement, and is outside of it

print ("var_a = {0}, var_b = {1} -> Addition = {2}, Multiplication = {3}".format(var_a,var_b,var_addition,var_multiplied))


# End Q2
#################################################################################
# TODO Q3: Check for file extensions (15 points)
#  Given the following variable that stores a file and its path, perform the
#  following tasks:
#  a) Extract the filename along with the extension (i.e. zip.shp) into a new
#     variable "file_name" using slicing. (3 points)
#  Using conditional statements and teh variable from (a), check the file extension
#  using the .endswith() method:
#  b) If the file is a shapefile (.shp), print the following text: (3 points)
#       "<file_name> is a shapefile"
#  c) Else if the file is a text file (.txt), print the following text: (3 points)
#       "<file_name> is a text file"
#  d) Else if the file is a csv file (.csv), print the following text: (3 points)
#       "<file_name> is a csv file"
#  e) For all other file types, print the following text: (3 points)
#       "<file_name> has an unknown extension"
#     Replace <file_name> with the actual file name and extension using the
#     variable from (a)
# Please add comments to explain what you are coding
# Write your code below

# Given string literals
# You may change the extension to test your code
in_file = "c:/workspace/gist/assignment2/zip.shp"
# JW: Slicing method below! I only sliced out the last 7 indexes
file_name = in_file[-7:]
print(file_name)

# JW: The very long statement begins below, searching to see if the end matches with any of the available conditions
if file_name.endswith(".shp"):
    print(file_name +" is a shapofile")
elif file_name.endswith(".txt"):
    print(file_name +" is a text file")
elif file_name.endswith(".csv"):
    print(file_name +" is a commad separated values file ")
else:
    #If it manages to make it through all of the previous conditions unscathed, this is spit out
    print(file_name + " has an unknown extension")




# End Q3
#################################################################################
# TODO Q4: Conditional Statements and Lists (15 points)
#  Given the following string literal and list, perform the following tasks:
#   a) If item "rivers" exists in the given list. Concatenate the variable
#      workspace and the item "rivers" to represent the following path. Store
#      the concatenation in a new variable and print the contents of this
#      variable. (5 points)
#      "C:/workspace/gist/Assignment2.gdb/rivers"
#   b) Compare the second item in the list with the string "parcels". If they are
#      the same . Remove the second item from the list and store it in a new
#      variable. Print the contents of this variable. (5 points)
#   c) If item "soils" does not exist in the given list. Append the item
#      "soils" to the list. Print the contents of the list. (5 points)
# Please add comments to explain what you are coding
# Write your code below

# Given string literal
workspace = "C:/workspace/gist/Assignment2.gdb/"
# Given list
list_of_fcs = ["streets", "parcels", "geology", "rivers", "precipitation"]

# JW: I check if rivers exists, and then it is appended to list_of_fcs
if "rivers" in list_of_fcs:
    workspace_two = workspace + "rivers"
    print(workspace_two)

# JW: If the 2nd index equals parcels, then it will be removed from the list and added to a variable with pop()
if list_of_fcs[1] == "parcels":
    parcel = list_of_fcs.pop(1)
print(parcel)

# JW: If the string "soils" doesn't exist in the list, then it will be added to the end of the list
if "soils" not in list_of_fcs:
    list_of_fcs.append("soils")
print(list_of_fcs)



# End Q4
#################################################################################
# TODO Q5: Spatial Reference (15 points)
#   a) Create a spatial reference object for the Geographic Coordinate System
#       NAD 1983/2011 using its WKID/Factory Code. (3 points)
#   b) Print out the name. (3 points)
#   c) Print out the datum. (3 points)
#   d) Print out the angular unit name. (3 points)
#   e) Print out the spheroid name. (3 points)


# JW: The arcpy package has to be imported in order to use the spatial reference tools
import arcpy

# Create a spatial reference object using the factory code for GCS_NAD_1983_2011
# JW: Searching online, the factory code for the spatial reference is 104223
# JW CORRECTION: I replaced 104223 with 6318 as the Spatial Reference
py_module = arcpy.SpatialReference(6318)
# JW: For the name, it's simply .name
print(py_module.name)
# JW: For the datum name, it's simply .datumName
print(py_module.datumName)
# JW: For the angular unit name, it's simply .angularUnitName (this is rather simple)
print(py_module.angularUnitName)
# JW: For the spheroid name, it's simply .spheroidName
print(py_module.spheroidName)
# End Q5
#################################################################################
# TODO Q6: Run the Clip tool (10 points)
#   a) Set up environment variables for workspace and overwriting output. (2 points)
#   b) Create two variables to store the following names of shapefiles and
#      their paths, depending on where you have downloaded the data. (3 points)
#           Input Features: hospitals.shp
#           Clip Features: zip.shp
#   c) Run the Clip tool using the above variables and the following: (3 points)
#           Output: hosp_zip_clip.shp in the workspace set in (a)
#   d) Print out appropriate messages from tool execution. (2 points)
#   Shapefiles can be found in Data.zip folder on D2L.
# Please add comments to explain what you are coding
# Write your code below

# Imports
import arcpy
# JW: Importing env will allow "env.()" without saying arcpy.env.()
from arcpy import env
# JW: This sets up environment properties, and the workspace location
env.workspace = "F:\XPS-PC\Documents\PYCHARMFILES\data"
# JW. This allows the files to be overwritten
env.overwriteOutput = True
# JW: This stores the first .shp file for clipping
hospital = "F:\XPS-PC\Documents\PYCHARMFILES\data\hospitals.shp"
# JW: Thos stores the second .shp file for clipping
zip_feature = "F:\XPS-PC\Documents\PYCHARMFILES\data\zip.shp"
# JW: This is what the output will be called, as well as whereit will output
clip_feature = "F:\XPS-PC\Documents\PYCHARMFILES\data\hosp_zip_clip.shp"
# JW: The clip analysis tool first takes in the two .shp files that will be clipped, and then the output location
zip_clip = arcpy.Clip_analysis(hospital,zip_feature,clip_feature)
# JW: GetMessages() gets the last geoprocessing messages from the last used tool
print(arcpy.GetMessages())


# End Q6
#################################################################################
# TODO Q7: Run the Union tool (10 points)
#   a) Create three variables to store the following names of shapefiles and
#      their paths, depending on where you have downloaded the data. (3 points)
#           Input Feature 1: parks.shp
#           Input Feature 2: geology.shp
#   b) Create a variable to store a list containing both variables from (b) as
#      items. (1 point)
#   c) Run the Union tool using the following parameters: (2 points)
#           Input features: variable that stores the list from (c)
#           Output: parks_geology_union.shp in the workspace set in (a)
#   d) Ensure that "gaps" in the output are created as features. (2 points)
#   e) Print out appropriate messages from tool execution. (2 points)
#   Shapefiles can be found in Data.zip folder on D2L.
# Please add comments to explain what you are coding
# Write your code below

# Imports
import arcpy
from arcpy import Result

# JW CORRECTION: Environment Setup, and overwrite output is set to True
arcpy.env.overwriteOutput = True
arcpy.env.workspace = "F:\XPS-PC\Documents\PYCHARMFILES\data"


# Two Variable stores two input features for union too;
parks = "F:\XPS-PC\Documents\PYCHARMFILES\data\parks.shp"
geology = "F:\XPS-PC\Documents\PYCHARMFILES\data\geology.shp"
# JW: Stores the above two variables as two items in a list and then assigns to a variable list_pargeo
list_pargeo = [parks,geology]
# JW: This is where the union shhapefile will be outputted, and it's file name
pargeo_union = "F:\XPS-PC\Documents\PYCHARMFILES\data\parks_geology_union.shp"
# JW: The results of the union tool will be stored in union_results.
# JW: The Union methpd takes in two shapefiles
# JW CORRECTION: "GAPS" was added as the 5th input. This creates features for the gaps
union_results = arcpy.Union_analysis(list_pargeo, pargeo_union, "ONLY_FID", 0.0003, "NO_GAPS")
# JW: arcpy.Result, or Result. gives you access to more methods
print(Result.getMessages(union_results))

# End Q7
#################################################################################
# TODO Q8: Run the AverageNearestNeighbor tool (10 points)
#   a) Create a variable to store the following name of the input shapefile and
#      its paths, depending on where you have downloaded the data. (1 point)
#            Input Feature: facilities.shp
#   b) Run the AverageNearestNeighbor tool using the following parameters: (3 points)
#            Input features: variable from (b)
#            Distance Method: Euclidean
#            Generate Report: Yes
#      Save the tool execution to a variable called ann_result.
#   c) Use the above variable (ann_result) to print out geoprocessing messages
#      from tool execution. (2 points)
#   d) Print out the Nearest Neighbor Ratio, the Z-score and the location of the HTML
#       report file using the results object stored in ann_result. (4 points)
#   Shapefiles can be found in Data.zip folder on D2L.



# JW: I had to do double slashes to avoid escape characters
facility = 'F:\\XPS-PC\\Documents\\PYCHARMFILES\\data\\facilities.shp'


print("+++++++++++++++++++++++++++")
# JW: Executes the AverageNearestNeighbor tool using the above variables as parameters and stores the result
# JW: in a new variable. The ++++++'s are to separate the output's so I can see what is being outputted and where
ann_result = arcpy.AverageNearestNeighbor_stats(facility, "EUCLIDEAN_DISTANCE", "GENERATE_REPORT")
print("+++++++++++++++++++++++++++")

# JW: This prints out the geoprocessing messages (below)
# JW: The -=-=-=-=-=-=-'s are to separate the outputs for analysis.
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print(ann_result.getMessages())
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

# JW: This prints out all the nearest neighbor data as well as the location of the html file
print(Result.getMessages(ann_result))

# JW CORRECTIONS: Below is to print out the Nearest Neighbor Ration, Zscore, and HTML location. Variable changed from
# nn_result to ann_result as well
print("Nearest Neighbor Ration:{}".format(ann_result[0]))

# End Q8
#################################################################################
# TODO Q9: Errors (10 points)
#  Each of the following code blocks uses lists and conditional statements.
#  Each of them have at least one syntax error, one exception, and one logical error.
#  Identify and fix all errors in each code block.
#  Please add comments to identify the type of error, explain what you fixed, and why.
# Fix the errors in the code below

# TODO Q9 a) Shopping: Fix all errors. (2 points)

# My shopping list
shopping_list = ["apples", "milk", "bread", "bananas", "spinach"]
# JW: The List is small is number of items is less than 3, as tested by the condition below
if len(shopping_list) < 3:
     print ("The list is small")
# JW: I changed the second test to <6, since nothing can be >3 and <3.
elif len(shopping_list) > 3 and len(shopping_list) < 6:
     print ("The list is medium")
# List is large is number of items is greater than 6
else:  # JW: This was missing a colon
     print ("The list is large")
# JW: Below I added a str() method to turn the list length into a string
print ("Total number of items: " + str(len(shopping_list)))
# HINT: We are trying to concatenate here and both should be strings.

# TODO Q9 b) MSGIST Courses: Fix all errors. (2 points)

# List of course numbers as strings
msgist_courses = ["601A", "601B", "602A", "602B", "603B", "604A", "604B", "909", "910"]
# If 603A is not in the list, insert it after 602B
if not "603A" in msgist_courses:
    print("603A is required course, must be in the list")
    # JW: I added a +1 to the index, to make it correctly placed AFTER
    msgist_courses.insert(msgist_courses.index("602B")+1, "603A")
# Description of 909
if "909" in msgist_courses:
    print("909 focuses on a capstone project.")
# Remove 910 from the list
if "910" in msgist_courses: # JW: "in" is the correct operator"
    print("Program does not have a 910 course, remove from list.")
    # JW: The correct index of 910 was 8 before 603A is added, but becomes 9 afterwards
    msgist_courses.pop(9) # HINT: What is the correct index of "910"?
print("Required MSGIST Courses: {}",format(msgist_courses))

# TODO Q9 c) Paths: Fix all errors. (2 points)

workspace = "C:\\gist\\featureclasses"
feature_classses = ["census_2020", "counties", "cities", "states"]
# Create the path to the census_2020 feature class and print it
if "census_2020" in feature_classses:
    # JW: I addded [0] to only reference the first index in the list
    census_path = workspace + "\\" + feature_classses[0]
    print(census_path)
# Create the path to the counties feature class and print it
if "counties" in feature_classses:
    # JW: Workspace was spelt "workspce"
    # JW: The order of the workspace was incorrect. We need the \\ before the featureclass (or counties)
    counties_path = "{}{}".format(workspace + "\\",feature_classses[1])
    print(counties_path)

# TODO Q9 d) Conversions : Fix all errors. (2 points)

# List contains numbers and strings
floats = ["4.58", "9.687"]
# Check if the type of first item is str
# JW: The float list variable name was incorrect, I changed it to floats below
if type(floats[0]) is str:
    # Replace the string with float
    floats[0] = float(floats[0])
# Check if the type of second item is str
# JW: I had to schange the "string" to str in order for the conditional to function
if type(floats[1]) is str:
    # Replace the string with float
    # JW: We want to check if index 2 is a string, and replace it with a float type. Not replace index 1 like before,
    # JW: so I changed the floats[0] below to a floats[1] to replace the correct index for this condition
    floats[1] = float(floats[1])
print(floats)
# Multiply the two numbers and print the result
print("Multiplication = {}".format(floats[0] * floats[1]))

# TODO Q9 e) Math: Fix all errors. (2 points)

# my list of numbers
my_numbers = [21, 10, 11]
# Check if 21 is greater than 10
if my_numbers[0] > my_numbers[1]: # JW: I added a greater than symbol since that is what we are trying to verify
    # JW: I added the str() method to the strings to make it work
    print(str(my_numbers[0]) + "[0] is greater than [1]" + str(my_numbers[1]))
else:
    # JW: The code below would initally spit out 21 is less than 11 if successful due to incorrect indexing,
    # JW: All I had to do is change the 2 to a 1, in the reference to my_numbers
    print("{} is less than {}".format(my_numbers[0], my_numbers[1]))


# End Q9
#################################################################################
# End of Assignment 2
#################################################################################