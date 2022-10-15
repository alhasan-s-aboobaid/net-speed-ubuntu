from heapq import merge
from sched import scheduler
from traceback import print_tb
import schedule
import time

def getData():

    path = "/proc/net/dev"
    lines = open(path,"r").readlines()

    columnLine = lines[1]
    _, receiveCols , transmitCols = columnLine.split("|")
    receiveCols = map(lambda a:"recv_"+a, receiveCols.split())
    transmitCols = map(lambda a:"trans_"+a, transmitCols.split())
    cols = merge(receiveCols, transmitCols)
    faces = {}
    for line in lines[2:]:
        if line.find(":") < 0: continue
        face, data = line.split(":")

        faceData = dict(zip(list(cols), data.split()))
        faces[face.replace(' ','')] = faceData

    import pprint
    pprint.pprint(faces)
    print((int(faces["lo"]["recv_bytes"])+int(faces["lo"]["trans_bytes"]))/1024)


schedule.every(1).seconds.do(getData)
while True:
    schedule.run_pending()
    time.sleep(1)