# -------------------------------------------------------------------------------
# Name:        Assignment5_withHints.py
# Purpose:     Script for Assignment5
# Author:      Dr. Yoganand Korgaonkar
# Student Name: Joseph Wade
# -------------------------------------------------------------------------------

#################################################################################
# TODO: Instructions:
#   - The overall goal of this part is to create a feature class using
#       coordinates from a csv file and then use this feature class to create
#       watersheds from an elevation raster.
#   - Hard-coding string literals will be minimum in this script. You will rely
#       heavily on variables to move data across different lines of code.
#   - Note that the output/result from each question carries forward to the
#       next task, so there is a form of continuity to all the code that you
#       will write.
#   - Your script should run error free and as one continuous block of code.
#   - You will use the elevation raster from
#       .../ExploringSpatialData/Sturgis.gdb/topo30m
#   - You will save all your outputs in the "A5_Results" folder. You may create
#       this folder outside of Python.
#   - The pourpoints.csv file can be found in the Unit6/Assignment module on D2L.
#   - You are encouraged to write code to handle errors and exceptions.
#################################################################################

# Imports - include all imports at the very beginning of the script.
import arcpy
import csv


# Environment Properties
# TODO IMP: Change this path to the "A5_results" folder on your computer
# JW: I have edited my workspace in my file folders permanently to more closely resemble your setup.
arcpy.env.workspace = "C:\\workspace\\gist\\results\\A5_results"


#################################################################################
# TODO Q1: Execute the CreateFeatureclass tool (10 points)
#   a) Create four variables to store the inputs for the CreateFeatureclass
#       tool. (5 points)
#       out_path: .../A5_Results
#       out_name: sturgis_points.shp
#       geometry_type: POINT
#       spatial_reference: NAD 1983 UTM Zone 13N (WKID = 26913)
#   b) Execute the CreateFeatureclass tool using the above variables and assign the
#       output of the CreateFeatureclass tool to a variable called "sturgis_pts".
#       Use sturgis_pts to print out geoprocessing messages. (5 points)
# Please add comments to explain what you are coding
# Write your code below

# JW: Variables store the inputs for the CreateFeatureclass tool. These are the Variables to be used in the tool
out_path = "C:\\workspace\\gist\\results\\A5_results"
out_name = "sturgis_points.shp"
geometry_type = "POINT"
spatial_reference = arcpy.SpatialReference(26913)

# JW: This simple .exists() will make sure that the file is deleted before it is attempted to be made, or errors occur
if arcpy.Exists("C:\\workspace\\gist\\results\\A5_results\\sturgis_points.shp"):
    print("sturgis_points.shp Already Exists. Remaking File.......")
    # JW: If the sturgis_points file already exists, delete it
    arcpy.Delete_management("C:\\workspace\\gist\\results\\A5_results\\sturgis_points.shp")
    # JW: WE aren't actually remaking the point file in this if statement, it happens afterwards

else:
    print("Creating sturgis_points.shp.......")

# JW: Execute the CreateFeatureclass tool and assign the result to the sturgis_pts variable
sturgis_pts = arcpy.CreateFeatureclass_management(out_path, out_name, geometry_type,spatial_reference=spatial_reference)

# JW: Print geoprocessing messages using the sturgis_pts variable and the GetMessages() tool
print(arcpy.Result.getMessages(sturgis_pts))

# End Q1
#################################################################################
# TODO Q2: Execute the AddField tool (10 points)
#   a) Execute the AddField tool using the following parameters. (5 points)
#           in_table = sturgis_pts
#           Field - name = WSHED, type = TEXT
#   b)  Assign the output of the AddField tool to a variable called
#       "add_field_result". Use add_field_result to print out geoprocessing
#       messages. (5 points)
# Please add comments to explain what you are coding
# Write your code below

# JW: Variables store the inputs for the AddField tool. Variables to be used in the tool
in_table = sturgis_pts # Do not change this line
Field_name = "WSHED"
type = "TEXT"

# JW: Execute the AddField tool and assign the result to the add_field_result variable
add_field_result = arcpy.AddField_management(in_table, Field_name, type)


# JW: Print geoprocessing messages using the add_field_result variable
print(arcpy.Result.getMessages(add_field_result))
# End Q2
#################################################################################
# TODO Q3: Add features to the empty feature class. (30 points)
#   In this task, we will create point objects from coordinates that are given
#       in the pourpoints.csv file. The CSV file contains 4 columns - W_ID,
#       X_COORD, Y_COORD, NAME. We will insert these point objects, along with
#       their ID & NAME into our empty feature class from above.
#   a) Open the pourpoints.csv file in read mode. Use the "with" statement. (3 points)
#   b) Create a DictReader object to access its contents and use the for loop to
#       loop through each row of the DictReader object. (5 points)
#   c) Inside the for loop, create four variables id, wshed, x_coord & y_coord
#       to store the W_ID, NAME, X_COORD & Y_COORD, respectively, from the
#       iteration. Note that the X & Y coordinates are stored as strings in the
#       dictionary. You will have to use the float() function to convert the
#       X & Y coordinates to floats while assigning to the variables. (5 points)
#   d) Inside the for loop, create an arcpy.Point object using
#       the variables x_coord & y_coord from (c) and assign it to a variable
#       called "pt_obj". (3 points)
#   e) Inside the for loop, create an arcpy.PointGeometry object using the
#       variable pt_obj from (d) and assign this object to a variable called
#       "pt_geom" (3 points)
#   f) Inside the for loop, setup an InsertCursor on the attribute table of
#      sturgis_points.shp using the following parameters. Use the "with"
#      statement. (5 points)
#           in_table = sturgis_pts ... from Q2 (a)
#           field_names: "SHAPE@", "ID", & "WSHED" (Note: this order matters)
#   g) Inside the for loop, create a list that stores three variables as items and
#       assign this list to a variable called "in_row" in the given order. (3 points)
#           Item 1: pt_geom ... from (d)
#           Item 2: id ... from (c)
#           Item 3: wshed ... from (c)
#   h) Inside the for loop, use the .insertRow() method with in_row from (e) to
#       insert the record into the attribute table. (3 points)
# Please add comments to explain what you are coding
# Write your code below


# Open the given csv file in read mode using the "with" statement
csvfile = "C:\\workspace\\gist\\results\\pourpoints.csv"

# JW: Opens the given csv file in read mode using the "with" statement.
with open(csvfile, "r") as open_csv:

    # JW: Creates a DictReader object called csv_dict.
    csv_dict = csv.DictReader(open_csv)


    # JW: Access each row as a dictionary from the DictReader object using a for loop
    for dict in csv_dict:
        print(dict)
        # JW: Variables stores the values from each column based on their keys
        id = dict["W_ID"]
        wshed = dict["NAME"]
        # JW: Variables for the coordinates are floats, due to the endless decimal points
        x_coord = float(dict["X_COORD"])
        y_coord = float(dict["Y_COORD"])
        # Using column names to access each item from the dictionary, Column names are keys in the dictionary

        # JW: Create a Point object using the Point class and variables x_coord & y_coord for PART D
        pt_obj = arcpy.Point(x_coord, y_coord)

        # JW: Create a Point Geometry object using the variables pt_obj for PART E
        pt_geom = arcpy.PointGeometry(pt_obj)


        # JW: Inputs for the insert cursor: in_table & field_names. Variables to set up the cursor
        in_table = sturgis_pts # Do not change this line
        field_names = ["SHAPE@", "ID", "WSHED"]

        # JW: PART F) Setup the Insert Cursor to access records using the "with" statement, taking in our fieldnames
        with arcpy.da.InsertCursor(in_table, field_names) as cursor:
            # JW: PART G: Below is the list for the insert row, containing the variables created earlier.
            in_row = [pt_geom, id, wshed]

            # JW: PART H: We need to use the above list to insert the information into each row, using InsertRow()
            cursor.insertRow(in_row)



# End Q3
#################################################################################
# TODO Q4: Create watersheds. (25 points)
#   You are given a variable "in_dem" that stores the path and name of the
#   topo30m raster available in ../ExploringSpatialData/Sturgis.gdb. You will
#   create watersheds using this dem and points from the previous question.
#   a) Execute the Fill tool using the following parameters, and assign the output
#       raster of the Fill tool to a variable called "dem_fill". Save the output
#       raster object permanently on disk in the A5_results folder using the name
#       "topo_f". Print geoprocessing messages using arcpy.GetMessages(). (5 points)
#           in_surface_raster = in_dem
#   b) Execute the FlowDirection tool using the following parameters, and assign
#       the output raster of the FlowDirection tool to a variable called "flow_dir".
#       Save the output raster object permanently on disk in the A5_results folder
#       using the name "topo_fd". Print geoprocessing messages using
#       arcpy.GetMessages(). (5 points)
#           in_surface_raster = dem_fill ... from (a)
#   c) Execute the FlowAccumulation tool using the following parameters, and assign
#       the output raster of the FlowAccumulation tool to a variable called
#       "flow_acc". Save the output raster object permanently on disk in the
#       A5_results folder using the name "topo_fa". Print geoprocessing messages
#       using arcpy.GetMessages(). (5 points)
#           in_flow_direction_raster = flow_dir ... from (b)
#   d) Execute the SnapPourPoint tool using the following parameters, and assign
#       the output raster of the SnapPourPoint tool to a variable called
#       "snap_pts". Save the output raster object permanently on disk in the
#       A5_results folder using the name "topo_pts". Print geoprocessing messages
#       using arcpy.GetMessages().(5 points)
#           in_pour_point_data = stur_pts ... from Q3(a)
#           in_accumulation_raster = flow_acc ... from (c)
#           snap_distance = 50
#   e) Execute the Watershed tool using the following parameters, and assign the
#       output raster of the Watershed tool to a variable called "watershed".
#       Save the output raster object permanently on disk in the A5_results folder
#       using the name "sheds". Print geoprocessing messages using
#       arcpy.GetMessages().(5 points)
#           in_flow_direction_raster = flow_dir ... from (b)
#           in_pour_point_data = snap_pts ... from (d)
# Please add comments to explain what you are coding
# Write your code below

# Variable stores the path and name of the input dem raster.
# TODO IMP: Change this path to the "../ExploringSpatialData/Sturgis.gdb/topo30m"
#  folder on your computer

in_dem = "C:\\workspace\\gist\\data\\ExploringSpatialData\\Sturgis.gdb\\topo30m"

# JW: There is no need to re-set the workspace, since it is still the same from earlier

# JW: PART A) Execute the Fill tool using the in_dem variable as input.
# JW: The Fill tool requires the Spatial Analyst  Module, hence the arcpy.sa
dem_fill = arcpy.sa.Fill(in_dem)

# JW: We want to make sure that the file can be overwritten if it already exists
arcpy.env.overwriteOutput = True

# JW: Save the raster output to disk as "topo_f". This will create the file
dem_fill.save("C:\\workspace\\gist\\results\\A5_results\\topo_f")

# JW: Print geoprocessing messages using arcpy.GetMessages(), this defaults to the last tool used. End of Part A)
print(arcpy.GetMessages())


# JW: Start of Part B) Execute the FlowDirection tool using the dem_fill variable, and Normal Force flow
flow_dir = arcpy.sa.FlowDirection(dem_fill, "NORMAL")
# JW:  The directory for the output, which is topo_fd
flow_dir.save("C:\\workspace\\gist\\results\\A5_results\\topo_fd")

# JW: Print geoprocessing messages using arcpy.GetMessages(), this defaults to the last tool used. End of Part B)
print(arcpy.GetMessages())


# JW: Start of Part C) Execute the FlowAccumulation tool using the variable flow_dir
flow_acc = arcpy.sa.FlowAccumulation(flow_dir)
# JW:  The directory for the output, which is topo_fa
flow_acc.save("C:\\workspace\\gist\\results\\A5_results\\topo_fa")

# JW: Print geoprocessing messages using arcpy.GetMessages(), this defaults to the last tool used. End of Part C)
print(arcpy.GetMessages())


# JW: STart of Part D) Execute the SnapPourPoint tool using the variables sturgis_pts,flow_acc and a snap_distance of 50
snap_pts = arcpy.sa.SnapPourPoint(sturgis_pts, flow_acc, 50)
# JW:  The directory for the output, which is topo_pts
snap_pts.save("C:\\workspace\\gist\\results\\A5_results\\topo_pts")

# JW: Print geoprocessing messages using arcpy.GetMessages(), this defaults to the last tool used. End of Part D)
print(arcpy.GetMessages())


# JW: Part E) Execute the Watershed tool using the variables flow_dir and snap_pts
watershed = arcpy.sa.Watershed(flow_dir, snap_pts)
# JW:  The directory for the output, which is sheds
watershed.save("C:\\workspace\\gist\\results\\A5_results\\sheds")

# JW: Print geoprocessing messages using arcpy.GetMessages(), this defaults to the last tool used. End of Part E)
print(arcpy.GetMessages())


# End Q4
#################################################################################
# TODO Q5: Reclassify the watersheds. (10 points)
#   In this task, you will reclassify the 9 watersheds to only 6 watersheds.
#   Watersheds with values 2, 3, 6 & 8 will be combined into a single watershed.
#   a) Use the sa.RemapValue class to create a RemapValue object to reflect the
#       following reclassification. Assign the RemapValue object to a variable
#       called "remap_value". (6 points)
#       Old Value --> New Value
#               1 --> 1
#               2 --> 2
#               3 --> 2
#               4 --> 3
#               5 --> 4
#               6 --> 2
#               7 --> 5
#               8 --> 2
#               9 --> 6
#   b) Execute the Reclassify tool using the following parameters, and assign
#       the output raster of the Reclassify tool to a variable called "r_ws".
#       Save the output raster object permanently on disk in the A5_results
#       folder using the name "r_sheds". (4 points)
#           in_raster = watershed ... from Q (e)
#           reclass_field: "VALUE"
#           remap = remap_value ... from (a)


watershed_raster = "C:\\workspace\\gist\\results\\A5_results\\sheds"

# JW: Part A) Create a remap_value object based on the given reclassification
remap_value = arcpy.sa.RemapValue([[1,1],[2,2],[3,2],[4,3],[5,4],[6,2],[7,5],[8,2],[9,6]])

# JW: Part B) Execute the Reclassify tool using the variables watershed, remap_value.
r_sheds = arcpy.sa.Reclassify(watershed, "VALUE", remap_value)


# JW: Save the raster output to disk as "r_sheds"
r_sheds.save("C:\\workspace\\gist\\results\\A5_results\\r_sheds")

# JW: Get the Geoprocessing Messages from the last tool
print(arcpy.GetMessages())


# End Q5
#################################################################################
# TODO Q6: List rasters and their properties (15 points)
#   a) Use an ArcPy List functions to create a list of all rasters in the
#       A5_results folder (2 points)
#   b) Setup a for loop to loop through this list. (2 points)
#   c) Inside this for loop, create a raster object for each raster in the
#       iteration. Assign the raster object to a variable called "ras". (3 points)
#   d) Inside the for loop, using the variable ras, print out the following
#       properties of the raster. (8 points)
#           1) Name
#           2) Coordinate System Name
#           3) Coordinate System Type
#           4) Coordinate System Linear Unit Name
#           5) Mean Cell Height
#           6) Mean Cell Width
#           7) Height
#           8) Width
# Please add comments to explain what you are coding
# Write your code below

# Create a list of rasters located in A5_results using an arcpy List function
# JW: The empty list that we will be filling with the raster names
raster_list = []

# JW: All raster files found in the workspace environment will be read and added to the list raster_list
for raster_files in arcpy.ListRasters("*"):
    raster_list.append(raster_files)

print(raster_list)
index_value = 0
for raster_name in raster_list:
    # JW: Using the workspace and adding the current index raster name from the list, we create a Raster Object for each
    # JW: Raster file location below
    ras = arcpy.sa.Raster("C:\\workspace\\gist\\results\\A5_results\\" + raster_name)

    # JW: I made the line below to make each individual raster info spit out more obvious
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

    # JW: Full Directory of the Current Raster in the loop
    print(ras)

    # JW: The name of the current raster in our loop
    print(ras.name)

    # JW: To obtain the coordinate system name and type, we need to describe the coordinate system as a spatial object
    out_coor_system = arcpy.Describe(ras).spatialReference

    # JW: The .name function is used to convert the spatial reference object gibberish into meaningful words
    print(out_coor_system.name)

    # JW: The .type function will obtain the type from the spatial reference object
    print(out_coor_system.type)

    # JW: The coordinate system units used
    print(out_coor_system.linearUnitName)

    # JW: Print out the mean cell height!
    print(ras.meanCellHeight)

    # JW: Print out the mean cell width!
    print(ras.meanCellWidth)

    # JW: Print out the raster height!
    print(ras.height)

    # JW: Print out the raster width!
    print(ras.width)

raster_output = (dem_fill + flow_dir) / flow_acc
raster_output.save("C:\\workspace\\gist\\results\\A5_results\\fun_raster")


# End Q6
#################################################################################
# End of Assignment 5
#################################################################################