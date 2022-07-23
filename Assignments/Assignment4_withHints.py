# -------------------------------------------------------------------------------
# Name:        Assignment4_withHints.py
# Purpose:     Script for Assignment4
# Author:      Dr. Yoganand Korgaonkar
# Student Name: Joseph Wade
# -------------------------------------------------------------------------------
#################################################################################
# TODO: Instructions:
#  - The overall goal of this script is to modify the attributes of the
#       Lake Austin watersheds using geoprocessing tools, csv files and cursors.
#  - You will make use of files, strings, lists, dictionaries, conditional
#       statements and looping structures in this assignment.
#  - Hard-coding string literals will be minimum in this script. You will rely
#       heavily on variables to move data across different lines of code.
#  - Note that the output/result from each question carries forward to the
#       next task, so there is a form of continuity to all the code that you
#       will write.
#  - Your script should run error free and as one continuous block of code
#  - To begin, you will use the watersheds feature class from
#       .../ExploringSpatialData/Austin.gdb/Environmental
#  - You will save all your outputs in the "A4_Results" folder. You may create
#       this folder outside of Python.
#  - The LakeAustin_ReachIntegrityScoreQuality.csv file can be found in the
#       Unit5/Assignment module on D2L.
#  - You are encouraged to write code to handle errors and exceptions.
#################################################################################

#################################################################################
# TODO Q1: Create a text file (10 points)
#   a) Open a file in write mode with the name "A4_Question1.txt". Use the "with"
#      statement. (3 points)
#   b) Write the following lines in the file, each on its own new line: (2 points)
#           "My name is <First_Name> <Last_Name>"
#           "What I like about Python:"
#               <List three things you like about Python>
#           "What I do not like about Python:"
#               <List three things you do not like about Python>
#   c) Open this same file in read mode. Use the "with" statement again. (3 points)
#   d) Use a for loop to print out all the lines in the file. (2 points)
# Please add comments to explain what you are coding
# Write your code below

# Open the A4_Question1.txt file in write mode using the "with" statement

# CORRECTIONS ARE ON LINES 140, 199, 257
print("The Corrections are on lines 140, 199, 257")

    # Write the given lines, each on its new line
# JW: This code below ensures that the file exists, and is made beforehand
new_file = open("F:\\XPS-PC\\Documents\\PYCHARMFILES\\Assignment_5\\A4_Question1.txt", "w")

# JW: Open the A4_Question1.txt file in writing "w" mode using the "with" statement. Technically the "a" could be used
# JW: Which allows for writing and appending.
with open("F:\\XPS-PC\\Documents\\PYCHARMFILES\\Assignment_5\\A4_Question1.txt", "w") as open_file:

    open_file.write("My Name is Joseph Wade!\n")
    open_file.write("What I like about Python:\n")
    open_file.write("   1.  I like it's relative simplicity.\n")
    open_file.write("   2.  I like the name and logo. The two snakes look quite silly. \n")
    open_file.write("   3.  I like how universal it is.\n")
    open_file.write("What I do not like about Python:\n")
    open_file.write("   1.  I dislike how lost you can get, but that's really just programming.\n")
    open_file.write("   2.  I dislike the time consumption of using it. \n")
    open_file.write("   3.  I dislike how some error codes are thrown completely in the wrong location.\n")

    # JW: Below sets the file to read, so that we can access it in the for loop, and for below. Otherwise an IO error
    # JW: would be thrown by the .read() attempting to read a "w" or write file.
    read_file = open("F:\\XPS-PC\\Documents\\PYCHARMFILES\\Assignment_5\\A4_Question1.txt", "r")

    # JW: Now we can successfully read into the file!
    read_file.read()

# JW: Below is for c). We will use "r" to read into the file
# JW: Below sets the file to read, so that we can access it in the for loop
read_file = open("F:\\XPS-PC\\Documents\\PYCHARMFILES\\Assignment_5\\A4_Question1.txt", "r")

# JW: The for loop below is going through each line in the file
for line in read_file:

    # JW: This is the actual line that does the printing, progressing to the next line afterward
    print(line[:-1])

# JW: Closing the files for practice
new_file.close()
read_file.close()

# End Q1
#################################################################################
# TODO Q2: Execute the Select tool (10 points)
#   a) Create three variables to store the inputs for the Select tool. (5 points)
#           in_features: .../ExploringSpatialData/Austin.gdb/Environmental/watersheds
#           out_feature_class: .../A4_results/watersheds.shp
#           where_clause = <select only those features who have RECV_WATER as Lake Austin>
#       Note: Above paths may change based on the location of data on your computer.
#   b) Execute the Select tool using the above variables and assign the output of
#       the Select tool to a variable called "select_result". Use select_result
#       to print out geoprocessing messages. (5 points)
# Please add comments to explain what you are coding
# Write your code below

# Imports
import arcpy
import os


# Environment properties
austingdb = "F:\XPS-PC\Documents\PYCHARMFILES\data\ExploringSpatialData\Austin.gdb"
arcpy.env.workspace = austingdb


# JW: These variables store the paths to the watersheds
in_features = austingdb + "\Environmental\watersheds"

# JW: The Below if statement is so that I can run this file multiple times without error. If the watershed.shp already
# JW: exists, either I have to manually delete the files everytime, or I can code it to do it iself.
if arcpy.Exists("F:\XPS-PC\Documents\PYCHARMFILES\Assignment_5\A4_Results\watersheds.shp"):
    print("Watersheds Already Exists. Remaking File.......")
    # JW: If the watershed file already exists, delete it
    arcpy.Delete_management("F:\XPS-PC\Documents\PYCHARMFILES\Assignment_5\A4_Results\watersheds.shp")

    # JW: WE aren't actually remaking the watersheds file in this if statement, it happens afterwards
    out_feature_class = "F:\XPS-PC\Documents\PYCHARMFILES\Assignment_5\A4_Results\watersheds.shp"

else:
    print("Creating watersheds.......")
    out_feature_class = "F:\XPS-PC\Documents\PYCHARMFILES\Assignment_5\A4_Results\watersheds.shp"

# JW: I made the field name a separate varialble in order to ensure the correct quotation was used
fieldname = "RECV_WATER"

# JW: The where clause is checking to make sure the RECV_WATER fields are only = to "Lake Austin"
where_clause = """{} = 'Lake Austin'""".format(arcpy.AddFieldDelimiters(out_feature_class, fieldname))


# JW: Execute the Select tool using the in, out, and where clause from above. Store in select_result_variable
select_result = arcpy.Select_analysis(in_features, out_feature_class, where_clause)

# print(arcpy.Result.getMessages(select_result))
# JW: CORRECTION: Print the geoproccessing results with different order. Fixed 3 other getMessages() throughout file
print(select_result.getMessages())



# End Q2
#################################################################################
# TODO Q3: Execute the DeleteField tool (10 points)
#   a) Create two variables to store the inputs for the DeleteField tool. (5 points)
#           in_table = select_result - from Q1(b)
#           drop_field = OBJECTID_1, OBJECTID, SHAPE_LENG, DCM_CODE, RECV_WAT_1
#   b) Execute the DeleteField tool using the above variables and assign the
#       output of the DeleteField tool to a variable called "delete_field_result".
#       Use delete_field_result to print out geoprocessing messages. (5 points)
# Please add comments to explain what you are coding
# Write your code below

# Variables store the inputs for the DeleteField tool. Variables to be used in the tool.
in_table = select_result # Do not change this line
drop_field = ["OBJECTID_1", "OBJECTID", "SHAPE_LENG", "DCM_CODE", "RECV_WAT_1"]

# JW: Execute the DeleteField tool and assign the result to the delete_field_result variable
delete_field_result = arcpy.DeleteField_management(in_table, drop_field)

# JW: Print out the geoprocessing results using the delete-field_result variable
# print(arcpy.Result.getMessages(delete_field_result))
# CORRECTION
print(delete_field_result.getMessages())


# End Q3
#################################################################################
# TODO Q4: Execute the AddFields tool (10 points)
#   a) Execute the AddFields tool using the following parameters. (5 points)
#           in_table = delete_field_result
#           Field 1 - name = ACRES, type = DOUBLE
#           Field 2 - name = QUALITY, type = TEXT, length = 50
#   b)  Assign the output of the AddFields tool to a variable called
#       "add_fields_result". Use add_fields_result to print out geoprocessing
#       messages. (5 points)
# Please add comments to explain what you are coding
# Write your code below

# Inputs for AddFields tool. Variables to be used in the tool.
in_table = delete_field_result # Do not change this line

fieldname1 = "ACRES"
fieldname2 = "QUALITY"
fieldtype1 = "DOUBLE"
fieldtype2 = "TEXT"
fieldlength = 50

# JW: I originally made add_fields_result a list because I wasn't aware you could do multiple fields at once in python
# Jw: I had to put fieldname2 for the alias, becuase for some reason field_length = fieldlength wasnt working
add_fields_result = arcpy.management.AddFields(in_table,[[fieldname1, fieldtype1], [fieldname2, fieldtype2, fieldname2,
                        fieldlength]])

# JW: Each Geoprocessing message is printed out. First one is for ACRES
# print(arcpy.Result.getMessages(add_fields_result))
# CORRECTION, use add_fields_result.getMessages instead of previous line, like previous error in question 2
print(add_fields_result.getMessages())

# End Q4
#################################################################################
# TODO Q5: Update attributes from a CSV file (20 points)
#   In this task, we will update the values in the "QUALITY" column in the
#      attribute table of watersheds.shp using the values in the "QUAL" column of
#      the LakeAustin_ReachIntegrityScoreQuality.csv. This csv file only has a few
#      DCM_NAMEs in it.
#   a) Open the LakeAustin_ReachIntegrityScoreQuality.csv file in read mode. Use
#      the "with" statement. (3 points)
#   b) Create a DictReader object to access its contents and use the for loop to
#      loop through each row of the DictReader object. (5 points)
#   c) Inside the for loop, create two variables csv_name & csv_qual to store the
#      name and quality, respectively, from the iteration. (2 points)
#   d) Inside the for loop, setup an UpdateCursor on the attribute table of
#      watersheds.shp using the following parameters. Use the "with"
#      statement. (5 points)
#           in_table = add_fields_result
#           field_names: "QUALITY"
#           where_clause: DCM_NAME equals csv_name
#   e) Inside the for loop, setup another for loop to iterate over the records
#      returned by the update cursor. (2 points)
#   f) Inside this second for loop, update the values for the field QUALITY in
#      the attribute table using the value stored in the csv_qual variable from
#      Q5(c). Remember to use the .updateRow() method to save changes. (3 points)
#   You may change the order of these tasks as long as you use the "QUAL" values
#       from the csv file to update the "QUALITY" column in the attribute table.
# Please add comments to explain what you are coding
# Write your code below

# Imports
import arcpy
import csv

# JW: Variable stores the path and name of the input CSV file
csvfile = "F:\XPS-PC\Documents\PYCHARMFILES\Assignment_5\LakeAustin_ReachIntegrityScoreQuality.csv"

# JW: Opens the given csv file in read mode using the "with" statement.
with open(csvfile, "r") as open_csv:

    # JW: Creates a DictReader object called csv_dict.
    csv_dict = csv.DictReader(open_csv)

    # JW: The for loop below prints out each individual line from the csv_dict (part b)
    for dict in csv_dict:
        print(dict)

        # JW: Variable stores the value in first column of CSV file, i.e. NAME. This is for part c
        csv_name = dict["NAME"]

        # JW: Variable stores the Value in second column of CSV file, i.e. QUAL. This is for part c
        csv_qual = dict["QUAL"]

        watershedfile = "F:\XPS-PC\Documents\PYCHARMFILES\Assignment_5\A4_Results\watersheds.shp"
        fieldname3 = "DCM_NAME"

        # JW: The where clause is checking to make sure the DCM_NAME field is only = to "csv_name"
        # CORRECTION:
        where_clause2 = """{0} = '{1}'""".format(arcpy.AddFieldDelimiters(watershedfile, fieldname3),csv_name)

        in_table = add_fields_result # Do not change this line

        #JW: This is for part d, where the cursor will overwrite the QUALITY column
        with arcpy.da.UpdateCursor(in_table, "QUALITY", where_clause2) as cursor:

            # JW: This for loop is needed to get through the QUALITY data
            for row in cursor:

                # JW: This updates the QUALITY Rows using the csv_qual variable
                csv_qual = row
                cursor.updateRow(row)


# End Q5
#################################################################################
# TODO Q6: Delete records from the attribute table (10 points)
#    In this task, we want to delete the records with DCM_NAMEs "Bear Creek West"
#       and "Huck's Slough" from the attribute table of watersheds.shp.
#    a) Setup an UpdateCursor on the attribute table of watersheds.shp using the
#       following parameters. Use the "with" statement. (3 points)
#           in_table = add_fields_result
#           field_names: "DCM_NAME"
#    b) Setup a for loop to iterate over the records returned by the update
#       cursor. (2 points)
#    c) Inside the for loop, use an if statement to check if the DCM_NAME is
#       "Bear Creek West" or "Huck's Slough". (3 points)
#    d) Delete the record inside the if statement when the condition is True. (2 points)
# Please add comments to explain what you are coding
# Write your code below

# Inputs for the update cursor: in_table & field_names. Variables to set up the cursor.
in_table = add_fields_result # Do not change this line

# JW: Setting the field name to check to DCM_NAME
field_names = "DCM_NAME"

# JW: We will access the files using Update Cursor and a with statement again
with arcpy.da.UpdateCursor(in_table, field_names) as cursor:

    # JW:We iterate through each row
    for row in cursor:

        # JW: The DCIM_NAME has to equal Bear Creek West or Huck's Slough to be true
        # JW: This will delete the current row that the cursor is on IF it makes it through the IF statement
        if (row[0] == "Bear Creek West" or row[0] == "Huck's Slough"):

            # JW: This will delete the rows that make the above conditional statement true
            cursor.deleteRow()


# End Q6
#################################################################################
# TODO Q7: Calculate values using the update cursor (10 points)
#    In this task, we want to calculate values for the ACRES column using the
#       "SHAPE@AREA" field in the attribute table of watersheds.shp. The area in
#       "SHAPE@AREA" is in square feet based on the coordinate system of
#       watersheds.shp.
#       Conversion Factor: 1 Acre = 43560 Sq Ft
#    a) Setup an UpdateCursor on the attribute table of watersheds.shp using the
#       following parameters. Use the "with" statement. (3 points)
#           in_table = add_fields_result
#           field_names: "SHAPE@AREA" and "ACRES"
#    b) Setup a for loop to iterate over the records returned by the update
#       cursor. (2 points)
#    c) Inside the for loop, access the area in sq ft for each record using the
#       "SHAPE@AREA" field, convert it to acres and update the "ACRES" field.
#       Remember to use the .updateRow() method to save changes. (5 points)
# Please add comments to explain what you are coding
# Write your code below

# Inputs for the update cursor: in_table, field_names. Variables to set up the cursor.

in_table = add_fields_result # Do not change this line

field_names = ["SHAPE@AREA", "ACRES"]

# JW: Setup the Update Cursor to access records using the "with" statement
with arcpy.da.UpdateCursor(in_table, field_names) as cursor:

    for row in cursor:

        # JW: This will calculate the ACRES field using the Square feet from SHAPE@AREA
        row[1] = row[0] / 43560

        # JW: This saves the updated data permanently
        cursor.updateRow(row)

        # JW: Pretty output for the SHAPE@AREA and ACRES fields
        print("Square Feet = {0}, Acres = {1}".format(row[0],row[1]))



# End Q7
#################################################################################
# TODO Q8: Create a CSV file from attributes (20 points)
#   In this task you will create a CSV file with 4 columns: "FID", "DCM_NAME",
#       "ACRES" & "QUALITY". You will populate this file from the attribute table
#       of watersheds.shp.
#    a) Open a csv file in write mode with the following path & name
#       .../A4_Results/LakeAustinWatersheds.csv. Use the "with" statement. (3 points)
#    b) Create a variable called "column_names" to store the following column
#       names as a list: "FID", "DCM_NAME", "ACRES", & "QUALITY" (2 points)
#    c) Setup a DictWriter object to write rows in the CSV file from Q8(a) with
#       column names from Q8(b). Use the .writeHeader() method to write the
#       column names into the file. (3 points)
#    d) Setup a SearchCursor on the attribute table of watersheds.shp using the
#       following parameters. Use the "with" statement. (3 points)
#           in_table = add_fields_result
#           field_names: column_names
#    e) Setup a for loop to iterate over the records returned by the search
#       cursor. (2 points)
#    f) Inside the for loop, create a dictionary to store values from the
#       records returned by the search cursor, using strings "FID", "DCM_NAME",
#       "ACRES" & "QUALITY" as keys. (5 points)
#    g) Inside the for loop, write the above dictionary into the csv file using
#       the DictWriter.writeRow() method. (2 points)
# Please add comments to explain what you are coding

# JW: New CSV File path is defined
csvfile = "F:\XPS-PC\Documents\PYCHARMFILES\Assignment_5\A4_Results\LakeAustinWatersheds.csv"

# JW: Open a CSV file in write mode using the "with" statement
with open(csvfile, "w") as open_csv:



    # JW: Variable column_names in a list, for part b
    column_names = ["FID","DCM_NAME", "ACRES", "QUALITY"]

    # JW: Setting up the DictWriter object for the csv file and column names for part c
    reader = csv.DictWriter(open_csv,fieldnames = column_names)

    # JW: Write header to CSV file using the list of column names, column_names
    reader.writeheader()

    # Inputs for the search cursor: in_table, field_names
    in_table = add_fields_result # Do not change this line
    field_names = column_names # Do not change this line

    # JW: Set up the search cursor to read the attribute table using the "with" statement
    with arcpy.da.UpdateCursor(in_table, field_names) as cursor:

        # JW: Access each record returned by the search cursor using a for loop
        for row in cursor:

                # JW: Four variables to access each value in each column of the record. Each row refers to the indexes in
                # JW: The list above, FID, DCIM_NAME, "ACRES", "QUALITY".
                valuefield_1 = row[0] # FID
                valuefield_2 = row[1] # DCM_NAME
                valuefield_3 = row[2] # ACRES
                valuefield_4 = row[3] # QUALITY

                # Create a dictionary using the above variables, column names are keys, above variables are values
                new_dict = {
                    "FID": valuefield_1,
                    "DCM_NAME": valuefield_2,
                    "ACRES": valuefield_3,
                    "QUALITY": valuefield_4
                }

                # JW: Write the dictionary as a row to the CSV file.
                reader.writerow(new_dict)


# End Q8
#################################################################################
# End of Assignment 4
#################################################################################