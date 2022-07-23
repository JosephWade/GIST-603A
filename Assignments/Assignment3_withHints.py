# -------------------------------------------------------------------------------
# Name:        Assignment3_withHints.py
# Purpose:     Script for Assignment3
# Author:      Dr. Yoganand Korgaonkar
# Student Name: Joseph Wade
# -------------------------------------------------------------------------------
#################################################################################
# TODO: Instructions:
#  - The overall goal of this script is to copy existing polygon feature
#       classes into a new feature dataset in a new geodatabase, extract and store
#       fields from the copied feature classes in a dictionary and print out the
#       contents of the dictionary.
#  - Each goal is split into a specific task in each question given below.
#  - Note that the output/result from each task carries forward to the next task,
#       so there is a form of continuity to all the code that you will write.
#  - Your script should run error free and as one continuous block of code from
#       start to end.
#  - Remember to use a print statement to indicate what step is currently
#       executing in the code.
#  - Data required to test the script can be found on D2L.
#################################################################################

#################################################################################
# TODO Q1: Create a geodatabase (15 points)
#   a) Create a new variable "gdb_path" to store only the path for a new
#      geodatabase on your computer. (2 points)
#      For example: gdb_path = "c:\workspace\gist\"
#      Your path may be different based on your folder structure.
#   b) Using the arcpy.Exists() function, check if "Assignment3.gdb" exists in
#      gdb_path. If it exists, the code should print the message (5 points):
#           "Assignment3.gdb already exists."
#   c) If "Assignment3.gdb" does not exist in gdb_path, use the
#      CreateFileGDB tool with the following parameters: (5 points)
#       out_folder_path: gdb_path
#       out_name: "Assignment3"
#   d) Print out appropriate messages from CreateFileGDB tool execution. (3 points)
# Please add comments to explain what you are coding
# Write your code below

# Imports
import arcpy
import os
import arcpy

# Variable stores path for new geodatabase
gdb_path = 'F:\\XPS-PC\\Documents\\PYCHARMFILES\\data\\'
arcpy.env.workspace = gdb_path

# JW: Check if the Assignment 3 database exists. If it doesn't exist, then create it!
if arcpy.Exists('Assignment3.gdb'):
    print("Assignment3.gdb already exists. Deleting and Remaking")
    # JW: If it exists, it needs to be deleted because it creates an error if the polygons already exist.
    # JW: This will reduce errors further down in the code, and will simplify the whole code.
    # JW: I added this specifically for question 4, for the copying of the polygon shapefiles
    arcpy.Delete_management(gdb_path + "\\Assignment3.gdb")
    print("Recreating Assignment3.gdb.........")
    message_1 = arcpy.CreateFileGDB_management(gdb_path, "Assignment3")
else:
    print("Creating Assignment3.gdb.........")
    message_1 = arcpy.CreateFileGDB_management(gdb_path, "Assignment3")
    # JW: The print method for the message_1 has to be contained within the else, because if the geodatabase already
    # JW: exists, then the geodatabase won't need to be created, and the object won't exist
print(arcpy.Result.getMessages(message_1))



# End Q1
#################################################################################
# TODO Q2: Create a feature dataset (10 points)
#   a) Create a new variable "dataset_path" to store only the path for the new
#      feature dataset in gdb_path from Q1(a) (2 points)
#      For example: dataset_path = "c:/workspace/gist/Assignment3.gdb"
#      Your path may be different based on your folder structure.
#   b) Use the CreateFeatureDataset tool with the following parameters: (5 points)
#           out_dataset_path: dataset_path
#           out_name: polygon_fcs
#           spatial_ref: use North America Equidistant Conic (3 points)
#      HINT: You must create a spatial reference object to send to the tool
#            before setting up the CreateFeatureDataset tool.
#   c) Print out appropriate messages from tool execution.
# Please add comments to explain what you are coding
# Write your code below

# variable stores the path to the new geodatabase from Q1
dataset_path = 'F:\\XPS-PC\\Documents\\PYCHARMFILES\\data\\Assignment3.gdb'
# JW: variable stores the name of the new dataset
dataset_name = "polygon_fcs"
# JW: Creating a spatial reference object for "North America Equidistant Conic"
spatial_ref = arcpy.SpatialReference(102010)
# JW: We need to check if the polygon_fcs file currently exists, because if it does, it will throw an error if we try to
# JW: create it a 2nd time. This is why I am checking for the file.
if arcpy.Exists('Assignment3.gdb\\polygon_fcs'):
    print("polygon_fcs currently exists. Remaking File.......")
    # JW: If the polygon_fcs file already exists, delete it, and then remake it.
    arcpy.Delete_management(dataset_path + "\\polygon_fcs")
    message_2 = arcpy.CreateFeatureDataset_management(dataset_path, dataset_name, spatial_ref)

else:
    # JW: This else will only be activated the first time this code is run, or if the polygon_fcs is manually deleted
    print("Creating polygon_fcs.......")
    message_2 = arcpy.CreateFeatureDataset_management(dataset_path, dataset_name, spatial_ref)

# JW: Printing out the result object messages afterwards. Always obtained due to the if statement
print(arcpy.Result.getMessages(message_2))




# End Q2
#################################################################################
# TODO Q3: List all polygon feature classes in Austin.gdb/Environmental (5 points)
#   a) Use an ArcPy List functions to create a list of all polygon feature classes
#      in the Environmental feature dataset in Austin.gdb. Store the list in a new
#      variable called list_of_fcs. Print the contents of the list. (3 points)
#   HINT: There should only be three feature classes in your list
#   b) Using the variable list_of_fcs and correct indices, use three print
#      functions to print the following lines exactly as they appear. (2 points)
#               Feature Class 1: geology
#               Feature Class 2: watersheds
#               Feature Class 3: soils
# Please add comments to explain what you are coding
# Write your code below


austin_path = R'F:\XPS-PC\Documents\PYCHARMFILES\data\ExploringSpatialData\Austin.gdb'
# JW: Set's the current workspace to Austin.gdb
arcpy.env.workspace = austin_path


# JW: list_of_dcs contains all of the different feature datasets. We only care about the Environments one though
# list_of_dcs = arcpy.ListDatasets(feature_type='feature')
# JW: This is why we set poly_feature_class to Environmental, so we only extract the data from the Environmental feature
poly_feature_class = "Environmental"
# JW: We need to create the list first, so that it can be filled up by the for loop
list_of_fcs = []
# JW: "fc" is the names of all the files contained within the "Environmental" feature dataset.
for fc in arcpy.ListFeatureClasses(feature_dataset=poly_feature_class):
    # JW: The description type of each file in environmental will be detected, and stored in desc.
    # JW: Describe throws out numbers, it has to be further processed by .shapetype to throw out "polygon" or "polyline"
    desc = (arcpy.Describe(fc))
    # JW: If the shapetype equals polygon, then it is one of the 3 polygon files we need to add to the list_of_fcs
    if (desc.shapeType == "Polygon"):
        # JW: Any sucessful polygons will be added to the end of the list_of_fcs list with append.
        list_of_fcs.append(fc)

# JW: By setting the initial index to 1, it will change everytime the for loop runs through, and increase by 1
index_of_fcs = 1
# JW: bc is the temporary variable. We will run through the list_of_fcs, and each index.
for bc in list_of_fcs:
    # JW: This will print out the list_of_fcs and their location in the index in the proper format
    print("Feature Class {0}: {1}".format(index_of_fcs,bc))
    # JW: This incrementally increases the number at the end of the loop
    index_of_fcs += 1



# End Q3
#################################################################################
# TODO Q4: Copy feature classes to empty geodatabase (10 points)
#   a) Using a for loop, loop through the list from Q3. (3 points)
#   b) In the loop, check for the "watersheds" polygon feature class and skip
#      the iteration of the loop for it. (2 points)
#   c) In the loop, create a new variable called out_fc and concatenate the
#      path to the polygon_fcs feature dataset with the name of the feature
#      class stored in the variable of the for loop. (1 point)
#   d) In the loop, use the CopyFeatures tool to copy the remaining feature
#      classes to the empty feature dataset created in Q2. Print out appropriate
#      messages from tool execution. (4 points)
#          Input Feature: use variable from for loop
#          Output Feature: use variable out_fc from (c)
#   HINT: There should only be two feature classes in the new geodatabase
# Please add comments to explain what you are coding
# Write your code below


gdb_path_2 = 'F:\\XPS-PC\\Documents\\PYCHARMFILES\\data\\Assignment3.gdb'
arcpy.env.workspace = gdb_path_2


# JW: The out_workspace will be used in the copy features method, so that we know where to output the copied features
out_workspace = gdb_path_2 + "\\polygon_fcs"
# JW: We need to temporarily change the workspace back to the previous Austin.gdb to copy the features
arcpy.env.workspace = austin_path
poly_feature_class_2 = "Environmental"
# JW: We need a for loop to detect the features we want to copy over. This will be features from the Environmental group
for ab in arcpy.ListFeatureClasses(feature_dataset=poly_feature_class_2):

    desc2 = (arcpy.Describe(ab))
    if (desc2.shapeType == "Polygon"):

        # JW: Any sucessful polygons will be added to the end of the list_of_fcs list with append.
        # JW: We do NOT want to copy over the watershed polygon, so if it is detected, we will continue
        if (ab == "watersheds"):
            # JW: The continue function doesn't break out of the loop, but skips this iteration if the condition is met
            continue
        else:
            print(str(ab) + " polygon copied")
            # JW: This is part c of the question, where the file location is concated to the name
            out_fc = os.path.join(out_workspace, os.path.splitext(ab)[0])
            # JW: We will store the results of the tool in message_3
            message_3 = arcpy.CopyFeatures_management(ab, out_fc)
            # JW: We will print out message_3 below
            print(arcpy.Result.getMessages(message_3))
            print(out_fc)









# End Q4
#################################################################################
# TODO Q5: List feature classes in Assignment3.gdb/polygon_fcs (5 points)
#   a) Use an ArcPy List functions to create a list of both the polygon feature
#       classes in the polygon_fcs feature dataset in Assignment3.gdb. (2 points)
#   b) Use a for loop to print the contents of this list. (3 points)
# Please add comments to explain what you are coding
# Write your code below

# JW: Sets the current workspace to Assignment3.gdb. We already know it exists from the 1st question
dataset_path = 'F:\\XPS-PC\\Documents\\PYCHARMFILES\\data\\Assignment3.gdb'
poly_fcs_name = "\\polygon_fcs"
arcpy.env.workspace = dataset_path
# JW: Remember that we created polygon_fcs in question 2

# JW: This is the empty list for the polygon feature classes in the polygon_fcs feature dataset
list_of_pfcs = []
# JW; This for loop will look for polygon_fcs in the Assignment3.gdb, and then add those items to the list_of_pfcs
for abc in arcpy.ListFeatureClasses(feature_dataset="polygon_fcs"):
    list_of_pfcs.append(abc)

# JW: Below is for b), a for loop that will print out all of the items in the newly created list from polygon_fcs
for printlist in list_of_pfcs:
    print(printlist)


# End Q5
#################################################################################
# TODO Q6: Access fields from the soils feature class (10 points)
#   a) Use an ArcPy List function to access all "Single" fields from the "soils"
#       feature class. (3 points)
#   b) Create an empty list that will be used later in the code to store field
#       names. Use the variable "soils_field_names" to store this empty list. (1 points)
#   c) Setup a for loop to loop through the list of "Single" fields. (1 points)
#   d) In this loop, access the name of each field and append it to the
#       "soils_field_names" list from Q6(c). (2 points)
#   e) In the same loop, print the name and length of each field as follows (3 points):
#         Field Name = <name_of_field> | Length = <length_of_field>
# Please add comments to explain what you are coding
# Write your code below

# JW: Full path to soils feature class. We know it exists because we just transferred it. I will access the polygon_fcs
soils_path = 'F:\\XPS-PC\\Documents\\PYCHARMFILES\\data\\Assignment3.gdb\\polygon_fcs\\soils'
# JW: Below is the List function for all the single fields in the soils feature class, stored in single_fields
# JW: The 2nd input is the wildcard, so I just put in a blank star, which represents 0
single_fields = arcpy.ListFields(soils_path, "*","Single")

# JW: Below is the empty list for b)
soils_field_names = []
# JW: Below is the for loop for c), where we will cycle through the single fields and append them to the list
for fields in single_fields:
    # JW: Below is where we will append the single field names to soils_field_names
    soils_field_names.append(fields)
    # JW: Below Prints the name and length of the field
    print("Field Name = {0} | Length = {1}".format(fields.name,fields.length))


# Use ListFields to create a list of Single fields from the soils feature class
#
#
# # Empty list to store field names
#
#
# # Loop through the soils field objects
#
#     # Append names to the list
#
#


# End Q6
#################################################################################
# TODO Q7: Access fields from the geology feature class (10 points)
#   a) Use an ArcPy List function to access all "String" fields from the "geology"
#       feature class. (3 points)
#   b) Create an empty list that will be used later in the code to store field
#       names. Use the variable "geology_field_names" to store this empty list. (1 points)
#   c) Setup a for loop to loop through the list of "String" fields. (1 points)
#   d) In this loop, access the name of each field and append it to the
#       "geology_field_names" list from Q6(c). (2 points)
#   e) In the same loop, print the name and length of each field as follows (3 points):
#         Field Name = <name_of_field> | Length = <length_of_field>
# Please add comments to explain what you are coding
# Write your code below

# Full path to geology feature class
# JW: Full path to geology feature. We know it exists because we just transferred it. I will access the polygon_fcs
print("=-=-=-=-=-=-=-=-=-=QUESTION_7=-=-=-=-=-=-=-=-=-=")
geology_path = 'F:\\XPS-PC\\Documents\\PYCHARMFILES\\data\\Assignment3.gdb\\polygon_fcs\\geology'

# Use ListFields to create a list of String fields from the geology feature class
# JW: Below is the List function for all the string fields in the geology feature class, stored in single_fields

string_fields = arcpy.ListFields(geology_path, "*","String")
# JW: Below is the empty list for b)
geology_field_names = []

for fields in string_fields:
    # JW: Below is where we will append the single field names to geology_field_names
    geology_field_names.append(fields)
    # JW: Below Prints the name and length of the field. Exactly the same as the previous question
    print("Field Name = {0} | Length = {1}".format(fields.name,fields.length))




# End Q7
#################################################################################
# TODO Q8: Add lists to a dictionary (10 points)
#   a) Create an empty dictionary that will be used later in the code to store
#       the soils_fields and geology_fields list from above. Use the variable
#       "poly_dict" to store this empty dictionary. (2 points)
#   b) Store the "soils_field_names" list in this dictionary with key "soils". (4 points)
#   c) Store the "geology_field_names" list in the same dictionary with key
#       "geology". (4 points)
# Please add comments to explain what you are coding
# Write your code below

# JW: Creating an empty dictionary, (for a)
poly_dict = {}


# Below adds both the soils and geology lists to the dictionary with the proper keywords
poly_dict = {
    "soils": soils_field_names,
    "geology": geology_field_names
}

# Add the geology list to the dictionary with key "geology"


# End Q8
#################################################################################
# TODO Q9: Print contents of dictionary (5 points)
#   a) Setup a for loop to loop through the "poly_dict" dictionary from Q8 (2 points)
#   b) Print out the keys and values from the dictionary in the following
#       format: (3 points)
#       Feature Class = <fc1_name>
#           Fields = <list_of field_names>
# Please add comments to explain what you are coding
# Write your code below

# JW: Below is a printline to help identify Question 9's output
print("=-=-=-=-=-=-=-=-=-=QUESTION_9=-=-=-=-=-=-=-=-=-=")
# JW: Both the key, and the values will be run through in this for loop. This spits out the tuple pairs of key and value
for key,value in poly_dict.items():
    print("Feature Class = {0}".format(key))
    # JW: The 2nd loop uses the previos loops feature class, and runs through all of the field names of that feature
    for item in value:
        print("     Fields = {0}".format(item.name))




# End Q9
#################################################################################
# TODO Q10: Dictionaries (10 points)
#  Given the following list of dictionaries, this task requires you to print three
#  columns populated by the values in the dictionaries.
#   a) Print the following lines exactly as it appears. (3 points)
#          ID |     WATERSHED     | RECEIVING WATERSHED
#        ---- | ----------------- | -------------------
#      IMPORTANT: Note the formatting on these three columns
#         Column 1: ID - right aligned, width = 5 characters
#         Column 2: WATERSHED - center aligned, width = 19 characters
#         Column 3: RECEIVING WATERSHED - left justified, width = 21 characters
#   b) Set up a for loop to loop on the given list of dictionaries. (2 points)
#   c) Use the for loop and a single print function to print the following
#      exactly as it appears. You may create variables to facilitate the
#      formatting of the print function. (5 points)
#           88 |       RINARD      | ONION CREEK
#           58 |  HARPER'S BRANCH  | TOWN LAKE
#           75 |        MAHA       | CEDAR CREEK
#           74 |      LOCKWOOD     | WILBARGER
#           47 |        ELM        | GILLELAND CREEK
#      IMPORTANT: The alignment and column widths should be the same as in (a).
#                 All strings must be uppercase.
#                 Do not hardcode any of these strings. Use variables and keys.
# Please add comments to explain what you are coding
# Write your code below

# The following list stores 5 dictionaries.
# Each dictionary stores 5 records from the attribute table of the watersheds
# feature class in the Austin.gdb/Environmental dataset
# The keys in these dictionaries are the column names
# The values correspond to the attributes in the respective columns
list_of_dicts = [
    {"DISPLAY" : "Rinard" , "RECV_WATER" : "Onion Creek" , "WATERSHED_" : 88},
    {"DISPLAY" : "Harper's Branch" , "RECV_WATER" : "Town Lake", "WATERSHED_" : 58},
    {"DISPLAY" : "Maha" , "RECV_WATER" : "Cedar Creek", "WATERSHED_" : 75},
    {"DISPLAY" : "Lockwood" , "RECV_WATER" : "Wilbarger", "WATERSHED_" : 74},
    {"DISPLAY" : "Elm" , "RECV_WATER" : "Gilleland Creek", "WATERSHED_" : 47}
]

print("=-=-=-=-=-=-=-=-=-=QUESTION_10=-=-=-=-=-=-=-=-=-=")

# JW: I am using the .format alignment to print out these messages.
print("{:>5} | {:^19} | {:<21}".format("ID","WATERSHED","RECEIVING WATERSHED"))

# JW: I am only printing out 19 dashes for the final column, since that is shown above
print("{:->5} | {:-^19} | {:-<19}".format("","",""))






# JW: Using a for loop, we will go through the list of dicts
for dict in list_of_dicts:

    # JW: Using the same formatting from earlier, we refer to each index in the dict by it's key (WATERSHED for example)
    # JW: The .upper() methods convert the lowercase titles to uppercase.
    print("{:>5} | {:^19} | {:<21}".format(dict["WATERSHED_"], (dict["DISPLAY"]).upper(), (dict["RECV_WATER"]).upper()))





# End Q10
#################################################################################
# TODO Q11: Errors (10 points)
#  Identify and fix all errors in the code below.
#  Only fix errors by modifying the lines of code, do not add your own lines.
#  Please add comments to identify the type of error, i.e. Syntax, Exception or Logical.
#  Please add comments to explain what you fixed
#  Please add comments to explain why you fixed that error
# Fix all the errors in the code below

# imports
# JW: The arcpy module can't be capitalized. It has to be lowercase when imported
# JW: I made arcpy lowercase. This was a syntax error
import arcpy

# Setting environment properties
# JW: I fixed the path, since it was different on my computer, and I lowercased the W on workspace.
# JW: This was a syntax error, and a logical error
arcpy.env.workspace = "F:/XPS-PC/Documents/PYCHARMFILES/data/ExploringSpatialData/Austin.gdb/Environmental"


# List all line feature classes in the workspace
# JW: I added the star for the wildcard, since it is required. This is a logical error. I removed the last index,
# JW: I also changed the feature type from point to Line since we are looking for a line type
list_of_line_fcs = arcpy.ListFeatureClasses("*", "Line", "")
print(list_of_line_fcs)
# Access and print the name of the first feature class in the list
# JW: The first index is 0, not 1. This is a logical error. I changed the 1 to a 0
first_line_fc = list_of_line_fcs[0]

# JW: For the format method, the {0} was never added. This is a syntax error, but no error is thrown
print("\nFirst feature class in the list is {0}".format(first_line_fc))

# Empty dictionary to use later
# JW: In order to create a dictionary, it has to be {}, not [], which instead creates a list
# JW: I fixed the curly brackets. This was a syntax error
line_dictionary = {}

# Loop through all feature classes one-by-one
# JW: The for loop needs to be reversed. The temporary variable is created first, then it is in list_of_line_fcs
for line_fc in list_of_line_fcs:
    print("\nFull path of feature class:")
    # Concatenate the full path of the feature class
    # JW: Again, there were no numbers in the format method, which are necessary. This is a logical error
    # JW: It is syntaxically correct. because {} default to the first element.
    line_path = "{0}+{1}".format(arcpy.env.workspace, line_fc)
    # Print the path
    print(line_path)
    print(line_fc)
    print(type(line_fc))
    # Save the path to the dictionary using the name as the key
    line_dictionary[line_fc] = line_path

# Print all the keys from the dictionary
print("\nKeys: ")
for key in line_dictionary.keys():
    # JW: Below was a syntax error, because the variable we need to refer to is key, not "keys" as it was before
    print(key)

# Print all the values from the dictionary
print("\nValues: ")
# JW: Below has to be .values() in order to work properly, as opposed to .keys()
for value in line_dictionary.values():
    print(value)

# End Q11
#################################################################################
# End of Assignment 3
#################################################################################