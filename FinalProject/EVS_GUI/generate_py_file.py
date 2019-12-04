# Christian Piper
# 12/4/19
# This code will generate a python file for the coprocessor to run

pythonCode = ""
currentTagNum = 0

def generatePythonFile(tag_list, instance_list, raw_team_number, neural_compute_stick, printInfo, streamer, dashboard_confidence):
    
    # Create master string
    

    addString( 
    """import time
import edgeiq
import pyfrc
from networktables import NetworkTables
import logging

# Constant for the default confidence (0 being 0% sure and 1 being 100% sure)
default_conf_thres = .75

def main():
    # Allow Rio to boot and configure network
    time.sleep(5.0)

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

    addString("""\n
            # loop detection
            while True:
""")

    if dashboard_confidence:
        addString("""
                # Grab values for confidence from SmartDashboard, if it can't, use default
                confidence_thres = sd.getString('DB/String 3', default_conf_thres)

                try:
                    # Try converting string to a float
                    confidence_thres = float(confidence_thres)
                except:
                    # If that fails, set the confidence threshold to the default value
                    confidence_thres = default_conf_thres
    

""")

    addString("""
                frame = video_stream.read()
                results = obj_detect.detect_objects(frame, confidence_level = """)
    
    if dashboard_confidence:
        addString("confidence_thres)\n")
    else:
        addString("default_conf_thres)\n")

    if streamer:
        addString("                frame = edgeiq.markup_image(frame, results.predictions, colors = obj_detect.colors)")
    
    addString("""

                #Counters - they reset after every frame in the while loop \n""")

    for entry in range(0, len(tag_list)):
        addString("                " + str(tag_list[entry]) + "Counter = 0 \n")

    addString('''        
                # Update the EVS NetworkTable with new values
                for prediction in results.predictions:                                                                                                                        

                    center_x, center_y = prediction.box.center
                    # Code goes here
                    numValues = [center_x, center_y, prediction.box.end_x, prediction.box.end_y, prediction.box.area, (prediction.confidence * 100)]
                    
                    for entry in range(0, len(numValues) - 1):
                        numValues[entry] = round(numValues[entry], 3)

                    numValuesArray = np.asarray(numValues) \n\n''')

    
    for entry in range(0, len(tag_list)):
        buildLabelClassfier(tag_list[entry])
        

    addString("                # Sets the value after the last value to false. The Rio will stop when it finds a False\n")

    for entry in range(0, len(tag_list)):
        addString("                " + tag_list[entry] + "Tables[" + tag_list[entry] + "Counter].putBoolean('inUse', False)\n")

    addString("\n                evs.putBoolean('checked', False)\n")

    if streamer:
        addString('''                # Generate text to display on streamer
                text = ["Model: {}".format(obj_detect.model_id)]
                text.append("Inference time: {:1.3f} s".format(results.duration))
                text.append("Objects:")

                # Format and display values on localhost streamer
                for prediction in results.predictions:
                    text.append("{}: {:2.2f}%".format(
                        prediction.label, prediction.confidence * 100))

                streamer.send_data(frame, text))\n''')

    addString("                fps.update()\n")
    
    if streamer:
        addString('''
                if streamer.check_exit():
                    break\n''')

    addString('''    finally:
        fps.stop()
        print("elapsed time: {:.2f}".format(fps.get_elapsed_seconds()))
        print("approx. FPS: {:.2f}".format(fps.compute_fps()))

        print("Program Ending")


if __name__ == "__main__":
    main()''')


    # Pull pythonCode variable and print it
    global pythonCode
    print("Code Generated!")
    return pythonCode
    


def addString(string):
    global pythonCode
    pythonCode = pythonCode + string

def buildLabelClassfier(tagName):
    global currentTagNum

    if currentTagNum == 0:
        addString('                    if prediction.label == "' + tagName + '":')

    else: 
        addString('                    elif prediction.label == "' + tagName + '":')
    
    addString('''\n     
                        ''' + tagName + '''Tables[''' + tagName + '''Counter].putNumberArray('values', numValuesArray)
                        # Boolean asks to update
                        ''' + tagName + '''Tables[%Counter].putBoolean('inUse', True)

                        ''' + tagName + '''Counter += 1 \n\n''')