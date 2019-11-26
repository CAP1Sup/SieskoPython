pythonCode = ""

def generatePythonFile(tag_list, instance_list, raw_team_number, neural_compute_stick, streamer, dashboard_confidence):
    
    # Create master string
    

    addString( 
    """import time
import edgeiq
import pyfrc
from networktables import NetworkTables
import logging

# Constant for the default confidence (0 being 0% sure and 1 being 100% sure)
default_conf_thres = .5

def main():

    # Setup logging for the NetworkTables messages
    logging.basicConfig(level=logging.DEBUG)

    # Setup NetworkTables
    NetworkTables.initialize(server = '10."""
    )


    if raw_team_number < 1000:
        string_team_number = str(raw_team_number)
        formatted_team_number = string_team_number[0] + "." + string_team_number[1] + string_team_number[2]
    else:
        string_team_number = str(raw_team_number)
        formatted_team_number = string_team_number[0] + string_team_number[1] + "." + string_team_number[2] + string_team_number[3]
        
    addString(
        formatted_team_number
    )

    addString(
        """.2')

    # Create table for values
    EVS = NetworkTables.getTable('EVS')
    sd = NetworkTables.getTable('SmartDashboard')

    # Create sub-tables and append them to arrays
"""
    )

    
    subtables_string = ""
    
    for tag_entry in range(0, len(tag_list)):
        if tag_entry == 1:
            subtables_string = subtables_string + "     " + tag_list[tag_entry] + "Tables = []"
        else:
            subtables_string = subtables_string + " \n\n    " + tag_list[tag_entry] + "Tables = []"
        for instance_entry in range(0, instance_list[tag_entry]):
            subtables_string = subtables_string + "\n"
            subtables_string = subtables_string + "    " + tag_list[tag_entry] + str(instance_entry) + " = EVS.getSubTable('" + tag_list[tag_entry] + str(instance_entry) + "')"

    addString(subtables_string)



    global pythonCode
    print("")
    print(pythonCode)
    


def addString(string):
    global pythonCode
    pythonCode = pythonCode + string


tag_list = ("hatch", "ball", "tape") 
instance_list = (3, 3, 6)
raw_team_number = 834
neural_compute_stick = True
streamer = True
dashboard_confidence = True

generatePythonFile(tag_list, instance_list, raw_team_number, neural_compute_stick, streamer, dashboard_confidence)