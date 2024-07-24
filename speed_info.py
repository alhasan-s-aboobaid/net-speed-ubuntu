from heapq import merge
from sched import scheduler
from traceback import print_tb
import schedule
import time
import pprint

def getData():
    
    # Define the path to the file containing network statistics
    path = "/proc/net/dev"

    # Read all lines from the file
    lines = open(path,"r").readlines()

    # Extract column headers for received and transmitted data
    columnLine = lines[1]
    _, receiveCols , transmitCols = columnLine.split("|")

    # Prefix column headers for differentiation
    receiveCols = map(lambda a:"recv_"+a, receiveCols.split())
    transmitCols = map(lambda a:"trans_"+a, transmitCols.split())

    # Merge the receive and transmit column headers into a single iterable
    cols = merge(receiveCols, transmitCols)

    # Initialize a dictionary to store data for each network interface
    faces = {}

    # Process each line corresponding to network interface statistics
    for line in lines[2:]:
        if line.find(":") < 0: continue # Skip lines that don't contain valid data

        # Split the line into interface name and data
        face, data = line.split(":")

        # Create a dictionary for the current interface's data
        faceData = dict(zip(list(cols), data.split()))

        # Store the data in the faces dictionary, removing spaces from the interface name
        faces[face.replace(' ','')] = faceData

    # Pretty-print the resulting dictionary of network interface data
    pprint.pprint(faces)

# Schedule the getData function to run every second
schedule.every(1).seconds.do(getData)

# Infinite loop to keep the script running and executing scheduled tasks
while True:
    schedule.run_pending() # Run any pending scheduled tasks
    time.sleep(1) # Sleep for 1 second before checking again
