pythonCode = ""

def generatePythonFile(tag_list, instance_list, raw_team_number, neural_compute_stick, printInfo, streamer, dashboard_confidence):
    
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
        if tag_entry == 0:
            subtables_string = subtables_string + "    " + tag_list[tag_entry] + "Tables = []"
        else:
            subtables_string = subtables_string + " \n\n    " + tag_list[tag_entry] + "Tables = []"
        for instance_entry in range(0, instance_list[tag_entry]):
            subtables_string = subtables_string + "\n"
            subtables_string = subtables_string + "    " + tag_list[tag_entry] + str(instance_entry) + " = EVS.getSubTable('" + tag_list[tag_entry] + str(instance_entry) + "')"
            subtables_string = subtables_string + "\n    " + tag_list[tag_entry] + "Tables.append(" + tag_list[tag_entry] + str(instance_entry) + ")"

    addString(subtables_string)

    addString('''\n
    # Setup EdgeIQ
    obj_detect = edgeiq.ObjectDetection(
            "alwaysai/mobilenet_ssd")
    obj_detect.load(engine=edgeiq.Engine.DNN''')

    if neural_compute_stick == True:
        addString("_OPENVINO")

    addString(")")

    if printInfo == True:
        addString('''\n \n''')
        addString('''
    # Print out info
    print("Loaded model:\\n{}\\n".format(obj_detect.model_id))
    print("Engine: {}".format(obj_detect.engine))
    print("Accelerator: {}\\n".format(obj_detect.accelerator))
    print("Labels:\\n{}\\n".format(obj_detect.labels))"''')

    if streamer == True:
        addString('''\n
    # Get the FPS
    fps = edgeiq.FPS()''')

    if dashboard_confidence == True:
        addString('''\n
    # Put the default confidence on the SmartDashboard
    sd.putString('DB/String 3', default_conf_thres)''')

    addString('''\n
    try:
        with edgeiq.WebcamVideoStream(cam=0) as video_stream)''')

    if streamer == True:
        addString(""", \\
                edgeiq.Streamer() as streamer""")

    addString(""": \n            
            # Allow Webcam to warm up
            time.sleep(2.0)
            fps.start()""")

    for entry in range(0, len(tag_list)):
        addString('''\n
            for i in range(0,''' + str(instance_list[entry] - 1) + '''): \n''')
        addString('''                ''' + tag_list[entry] + '''Tables[i].putBoolean('inUse', False)''')


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
printInfo = True
streamer = True
dashboard_confidence = True

generatePythonFile(tag_list, instance_list, raw_team_number, neural_compute_stick, printInfo, streamer, dashboard_confidence)