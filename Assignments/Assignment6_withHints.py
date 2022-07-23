# -------------------------------------------------------------------------------
# Name:        Assignment6_withHints.py
# Purpose:     Script for Assignment6
# Author:      Dr. Yoganand Korgaonkar
# Student Name: Joseph Wade
# -------------------------------------------------------------------------------
#################################################################################
# TODO: Instructions:
#   - You are free to experiment in Python Window if you like.
#   - Your code should still execute error free as a script in this file.
#   - The data can be found in the Assignment6 folder in the zip file provided
#       on D2L
#################################################################################

#################################################################################
# TODO Q1: ArcGIS Project Properties (10 points)
#   a) Open the .../Assignment6/UnitedStates/UnitedStates.aprx project in Python
#       and assign it to a variable. (2 point)
#   b) Save a copy of this project using the name UnitedStates_copy.aprx (2 point)
#   c) Open the UnitedStates_copy.aprx project in Python and assign it to a
#       variable called "aprx". You will use this variable throughout this code
#       to access the project. (2 point)
#   d) Access and print out the following ArcGIS Project properties using the
#       variable aprx from (c). (4 points)
#       - Date Saved
#       - Default Geodatabase
#       - File Path
#       - Home Folder
# Please add comments to explain what you are coding
# Write your code below

# Imports
import arcpy
from arcpy import mp

# CORRECTIONS ARE ON LINES 105, 153, 303, 386
print("The corrections for this assignment are on lines 105, 153, 303, and 386. Thanks!!!")

# JW: Setting the workspace to the United States folder
arcpy.env.workspace = "C:\\workspace\\gist\\data\\Assignment6\\UnitedStates"
# JW: Setting the ability to overwrite files to "True", so no errors are thrown
arcpy.env.overwriteOutput = True


# JW: Open the given UnitedStates.aprx ArcGIS project and assign it to the variable "current_project"
project_file_location = "C:\\workspace\\gist\\data\\Assignment6\\UnitedStates\\UnitedStates.aprx"
current_project = mp.ArcGISProject(project_file_location)
# JW: Save a copy of the project as UnitedStates_copy.aprx
current_project.saveACopy("C:\\workspace\\gist\\data\\Assignment6\\UnitedStates\\UnitedStates_copy.aprx")
# JW: Closes the project. Doesn't delete it!
del current_project

# Open the copied project and store in variable called aprx
aprx = mp.ArcGISProject("C:\\workspace\\gist\\data\\Assignment6\\UnitedStates\\UnitedStates_copy.aprx")

# JW: Returns the last date saved for the copied APRX project
print(aprx.dateSaved)

# JW: Returns the file Path for the copied APRX project
print(aprx.filePath)

# JW: Returns the default Geodatabase for the copied APRX project
print(aprx.defaultGeodatabase)

# JW: Returns the home folder for the copied APRX project
print(aprx.homeFolder)



# End Q1
#################################################################################
# TODO Q2: Fix Broken Data Sources (10 points)
#   a) Use the variable aprx from Q1 (c) to create a list of all layers with
#       broken data sources. Assign this list to a new variable. (2 points)
#   b) Setup a for loop to loop through this list. (2 points)
#   c) Inside this for loop, access and print the connection properties for each
#       layer with a broken data source. (2 points)
#   d) Inside the for loop, update the geodatabase path using the following
#       correct path and update the connection properties. (4 points)
#       Path = <your computer path>/Assignment6/Assignment6.gdb
# Please add comments to explain what you are coding
# Write your code below


# JW: Create a list of all datasets with broken data sources using the variable aprx, in a list called "broken_list"
broken_list = aprx.listBrokenDataSources()

# JW: Set up a  for loop on the list, named b_list
for b_list in broken_list:


    # JW: Access the connection properties for each layer, setting it to a variable "connection" so it can be printed
    connection = b_list.connectionProperties

    # JW: Print the connection properties using the variable "connection"
    print("FIRST=-=-=-=-=-=-=-=-=FIRST")
    print(connection)

    # JW: The Correct path to broken data sources is below!
    correct_path = "C:\workspace\gist\data\Assignment6\Assignment6.gdb"
    # Update the broken path from the original database to the correct_path. Incorrect path is taken in first, correct
    # 2nd
    #aprx.updateConnectionProperties('C:\\workspace\\gist\\data\\SUM21\\mgisdata\\Usa\\usdata.gdb',
    #                                correct_path)

    # JW CORRECTIONS, I made it so that the database is pulled from the dictionary within the connection properties
    aprx.updateConnectionProperties(connection['connection_info']['database'],correct_path)

    # Update the connection properties
    #updateConnectionProperties(current_connection_info, new_connection_info, {auto_update_joins_and_relates},
    #                           {validate}, {ignore_case})

    # JW: Print the connection properties to verify the change. The surrounding print lines helps me verify the change
    print("1+-=-=-=-=-=-=-=-1")
    print(connection)
    print("2+-=-=-=-=-=-=-=-2")

# JW: Save the project
aprx.save()

# End Q2
#################################################################################
# TODO Q3: Map Properties (10 points)
#   a) Access the "USA Map" from the project using the variable aprx and assign
#       the map to a new variable called "usa_map". (2 point)
#   b) Print out the following properties of "USA Map" map using the variable
#       usa_map. (8 points)
#       - Map Name
#       - Map Units
#       - Spatial Reference - Projected Coordinate System
#       - Spatial Reference - Central Meridian
#       - Spatial Reference - Latitude of Origin
#       - Spatial Reference - Standard Parallel 1
#       - Spatial Reference - Standard Parallel 2
#       - Spatial Reference - Linear Unit Name
# Please add comments to explain what you are coding
# Write your code below


# Access the USA Map from the project using the variable aprx, assign to variable usa_map
usa_map = aprx.listMaps()

# JW: Print Map properties using the usa_map variable
# JW: Even though there is only one item in the list, since it is a list, a for loop is needed
for usa_map in usa_map:
    # JW: Print Map Name.
    print(usa_map.name)

    # JW: Print Map Units
    print(usa_map.mapUnits)

    # JW: Print Map Spatial Reference - Projected Coordinate System
#    print(usa_map.spatialReference.name)
    # JW CORRECTION: I obtained the PCS from the spatialreference object as it's PCSName property/attribute
    # It's printing out twice to show two different methods that work, in case one is the incorrect answer
    print(getattr(usa_map.spatialReference, 'PCSName'))
    print(usa_map.spatialReference.PCSName)

    # JW: Print Map Spatial Reference - Central Meridian
    print(usa_map.spatialReference.centralMeridian)

    # JW: Print Map Spatial Reference - Latitude of Origin
    print(usa_map.spatialReference.latitudeOfOrigin)

    # JW: Print Map Spatial Reference - Standard Parallel 1
    print(usa_map.spatialReference.standardParallel1)

    # JW: Print Map Spatial Reference - Standard Parallel 2
    print(usa_map.spatialReference.standardParallel2)

    # JW: Print Map Spatial Reference - Linear Unit Name
    print(usa_map.spatialReference.linearUnitName)


# End Q3
#################################################################################
# TODO Q4: Layer Properties (25 points)
#   a) Use the variable usa_map from Q3 (a) to create a list of all layers in the
#       map. Assign this list to a new variable. Setup a for loop to loop through
#       this list. (3 points)
#   b) Inside the for loop from (a), use an if condition to check if the layer
#       "supports" the "name" property. Print the name of the layer using the
#       "name" property when the condition is True. (5 points)
#   c) Inside the if statement from (b), use the "name" property and an if
#       statement to check for the "States" layer. Turn on the labels using the
#       "labels" property for the "States" layer. (5 points)
#   d) Inside the if statement from (b), use the "name" property and an if statement
#       to check for the "Cities" layer. Hide the "Cities" layer using the "visible"
#       property. (4 points)
#   e) Inside the for loop from (a), use an if condition to check if the layer
#       "supports" the "brightness" property. Print the brightness of the layer
#       using the "brightness" property when the condition is True. (4 points)
#   f) Inside the for loop from (a), use an if condition to check if the layer
#       "supports" the "transparency" property. Print the transparency of the layer
#       using the "transparency" property when the condition is True. (4 points)
# Please add comments to explain what you are coding
# Write your code below

# JW: Access all layers form the map using the variable usa_map
usa_layers = usa_map.listLayers()

# JW: Fancy intro print statement to show me the layer names
print("Below are the USA Map Layers")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

# JW: Seting up a for loop to access the list of layers amd print them out
for usa in usa_layers:

    # JW: Check if the name property is supported by the layer using the has attribute
    # JW: Please note that [ if (hasattr(usa,'name')): ] works as well below

    if (usa.supports("name")):

        # JW: Print the name if the property is supported
        print(usa.name)
        print(usa.dataSource)

        # JW: Use an if condition to check if the layer name is "States"
        if (usa.name == "States"):

            # JW: Setting the show labels to True
            usa.showLabels = True

            # JW: List the Label Classes for the States Layer using a for loop to access the "list of labels"
            for lbl_name in usa.listLabelClasses():
                # JW: Print the label.name
                print(lbl_name.name)
        if (usa.name == "Rivers"):
            reference = usa
        if (usa.name == "Interstates"):
            move_me = usa

        # Use an if condition to check if the layer name is "Cities"
        if (usa.name == "Cities"):
            # JW: Hide the "Cities" layer using the "visible" property. This essentailly means the box is unchecked
            usa.Visible = False




    # JW: Check if the brightness property is supported by the layer
    if (usa.supports("brightness")):


        # JW: Print the brightness if the property is supported
        print("The Brightness of the layer is {}".format(usa.brightness))

    # JW: Check if the transparency property is supported by the layer
    if (usa.supports("transparency")):

        # JW: Print the transparency if the property is supported
        print("The Transparency of the layer is {}".format(usa.transparency))




# JW: Save the project
aprx.save()


# End Q4
#################################################################################
# TODO Q5: Moving Layers (20 points)
#   a) Create two layer objects for the "Interstates" & "Rivers" layers in the
#       map and assign each of them to a variable. (4 points)
#   b) Move the "Interstates" layer to a position after the "Rivers" layer using
#       the variables form (a). (4 points)
#   c) Create two layer objects for the "Counties" & "States" layers in the
#       map and assign each of them to a variable. (4 points)
#   d) Move the "Counties" layer to a position before the "States" layer using
#       the variables form (c). (4 points)
#   e) Create a layer object for the "climatestations" layer in the map and assign to
#       a variable. (2 points)
#   f) Remove the "climatestations" layer from the map using the variable
#       from (e). (2 points)
# Please add comments to explain what you are coding
# Write your code below




# JW: Create a layerfile object for the "Rivers" layer using the path and assigning it to "reference"
reference = usa_map.listLayers("Rivers")[0]

# JW: Create a layerfile object for the "Interstates" layer using the path and assigning it to "move_me"
move_me = usa_map.listLayers("Interstates")[0]



# JW: Move the interstates layer after rivers (Write line twice because of bug)
usa_map.moveLayer(reference,move_me,"AFTER")
usa_map.moveLayer(reference,move_me,"AFTER")

# JW: Create a layer object for the "Counties" layer using the path and assigning it to "reference_2"
move_me_2 = usa_map.listLayers("Counties")[0]

# JW: Create a layer object for the "States" layer using the path and assigning it to "move_me_2"
reference_2 = usa_map.listLayers("States")[0]

# JW: Make sure that the Counties layer is moved before the states layer (Write line twice because of bug)
usa_map.moveLayer(reference_2,move_me_2,"BEFORE")
usa_map.moveLayer(reference_2,move_me_2,"BEFORE")

# JW CORRECTION: I used a variable from 2 questions earlier that accessed usa_map.listLayers(), so I copied it here for
# Clarity
usa_layers = usa_map.listLayers()
# JW: Create a layer object for the "climatestations" layer and assign to a variable
for usa in usa_layers:
    if (usa.name == "climatestations"):

        remove_me = usa
# JW: Use RemoveLayer to remove the climatestations layer from the usa map copy project
usa_map.removeLayer(remove_me)
# Remove the climatestations layer


# JW: Save the project
aprx.save()


# End Q5
#################################################################################
# TODO Q6: Working with Symbology (25 points)
#   a) Create a layer objects for the "Counties" layer in the map and assign it
#       to a variable. (2 points)
#   b) Access the symbology of the layer using the variable from (a) and assign
#       the symbology object to a new variable. (2 points)
#   c) Use the variable from (b) and an if condition to to check if the symbology
#       has a "renderer" attribute. (2 points)
#   d) Update the symbology of the "Counties" layer as follows when the condition
#       is True. (3 points)
#       - Renderer: UniqueValueRenderer
#       - Renderer Field: STATE_NAME
#   e) Create a layer objects for the "Rivers" layer in the map and assign it
#       to a variable. (2 points)
#   f) Access the symbology of the layer using the variable from (e) and assign
#       the symbology object to a new variable. (2 points)
#   g) Use the variable from (f) and an if condition to to check if the symbology
#       has a "renderer" attribute. (2 points)
#   h) Update the symbology of the "Rivers" layer as follows when the condition
#       is True. (10 points)
#       - Renderer: GraduatedSymbolsRenderer
#       - Renderer Classification Field: MILES
#       - Renderer Classification Method: QUANTILE
#       - Renderer Break Count: 8
#       - Renderer Minimum Symbol Size: 1
#       - Renderer Maximum Symbol Size: 10
#       - Renderer ColorRamp: <Any of your choice>
# Please add comments to explain what you are coding
# Write your code below

# Create a layer object for the "Counties" layer and assign to a variable

# JW: Create a layer object for the "Counties" layer using the path, and the previous counties variable "move_me_2"
# JW: and assigning it to "counties"
# counties = move_me_2
counties = usa_map.listLayers("Counties")[0]
# JW: Access the symbology of the layer and assign to a new variabl, counties_sym
counties_sym = counties.symbology

# JW: Check if the counties_sym object has a renderer attribute
if hasattr(counties_sym,"renderer"):

# JW: Update the renderer to UniqueValueRenderer
    counties_sym.updateRenderer("UniqueValueRenderer")

    # JW: Set the renderer field to STATE_NAME
    counties_sym.renderer.fields = ['STATE_NAME']

    # JW: Apply the modified symbology back to the layer
    counties.symbology = counties_sym

# JW: Create a layer object for the "Rivers" layer and assign to the variable "rivers"
rivers = usa_map.listLayers("Rivers")[0]

# JW: Access the symbology of the layer and assign to the new variable "rivers_sym"
rivers_sym = rivers.symbology

# JW: Check if the symbology has a renderer attribute
if hasattr(rivers_sym,"renderer"):


    # JW: Update the renderer to GraduatedSymbols
    rivers_sym.updateRenderer("GraduatedSymbolsRenderer")

    # JW: Set the Classification field to MILES
    # JW: CORRECTION: I removed the brackets [] around the string 'MILES'
    rivers_sym.renderer.fields = 'MILES'


    # Set the Classification method to QUANTILE
    rivers_sym.renderer.classificationMethod = 'Quantile'

    # Set the Break Count to 8
    rivers_sym.renderer.breakCount = 8

    # Set the Minimum Symbol Size to 1
    rivers_sym.renderer.minimumSymbolSize = 1

    # Set the Maximum Symbol Size to 10
    rivers_sym.renderer.maximumSymbolSize = 10


    # JW: Access a color ramp from the project color ramps and assign to a variable
    color_ramp = aprx.listColorRamps("Cyan to Purple")[0]
    # JW: Set the renderer color ramp to the above color ramp
    rivers_sym.renderer.colorRamp = color_ramp




    # JW: Apply the modified symbology back to the layer

    rivers.symbology = rivers_sym
# JW: Save the project
aprx.save()


# End Q6
#################################################################################
# End of Assignment 6
#################################################################################