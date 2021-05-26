import csv
import icedetection
import matplotlib

lidar_set1 = []
radar_set1 = []
lidar_set2 = []
radar_set2 = []


f = open('lidar1.txt', newline='')
dataset_lidar1 = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in dataset_lidar1:
    rowlist_lidar1 = []
    for value in row:
        rowlist_lidar1.append(value)
    lidar_set1.append(rowlist_lidar1)
f.close()
        
        
f = open('radar1.txt', newline='')
dataset_radar1 = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in dataset_radar1:
    rowlist_radar1 = []
    for value in row:
        rowlist_radar1.append(value)
    radar_set1.append(rowlist_radar1)
f.close()
     

f = open('lidar2.txt', newline='')
dataset_lidar2 = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in dataset_lidar2:
    rowlist_lidar2 = []
    for value in row:
        rowlist_lidar2.append(value)
    lidar_set2.append(rowlist_lidar2)
f.close()
        
        
f = open('radar2.txt', newline='')
dataset_radar2 = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in dataset_radar2:
    rowlist_radar2 = []
    for value in row:
        rowlist_radar2.append(value)
    radar_set2.append(rowlist_radar2)
f.close()


def model1():
    matplotlib.pyplot.xlim(0, 299) # Environment needs to be set
    matplotlib.pyplot.ylim(0, 299)
    matplotlib.pyplot.imshow(lidar_set1)
    
def model2():
    matplotlib.pyplot.xlim(0, 299) # Environment needs to be set
    matplotlib.pyplot.ylim(0, 299)
    matplotlib.pyplot.imshow(lidar_set2)
    
model2()