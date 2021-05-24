import csv
import icedetection

lidar = []
radar = []

f = open('lidar1.txt', newline='')
dataset = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in dataset:
    rowlist = []
    for value in row:
        rowlist.append(value)
    lidar.append(rowlist)
f.close()

f = open('radar1.txt', newline='')
dataset = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in dataset:
    rowlist = []
    for value in row:
        rowlist.append(value)
    radar.append(rowlist)
f.close()