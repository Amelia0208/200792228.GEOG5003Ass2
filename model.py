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
    
    volume = 0
    
    for i in range(299):
        for j in range(299):
            if radar_set1[i][j] >= 100:
                radar_set1[i][j] = 1
                volume = volume + lidar_set1[i][j]
            else:
                radar_set1[i][j] = 0
                
    mass = volume * 900
    
    if mass <= 36000000:
        can_pull = 'yes'
        for i in range(299):
            for j in range(299):
                if radar_set1[i][j] == 1:
                    radar_set1[i][j] = 2
    else:
        can_pull = 'no'
    
    print('Volume: ' + str(volume) + '\nMass: ' + str(mass) + '\nCan be pulled: ' + str(can_pull))
    
    matplotlib.pyplot.imshow(radar_set1)
    
def model2():
    matplotlib.pyplot.xlim(0, 299) # Environment needs to be set
    matplotlib.pyplot.ylim(0, 299)
    
    vol = 0
    volume = []
    
    for i in range(299):
        for j in range(299):
            if radar_set2[i][j] >= 100:
                radar_set2[i][j] = 1
            else:
                radar_set2[i][j] = 0
    
    for i in range(1, 298):
        for j in range(1, 298):
            if radar_set2[i - 1][j] != 0:
                pass
            else: 
                if radar_set2[i][j - 1] != 0:
                    pass
                else:
                    if radar_set2[i][j] != 0:
                        for m in range(j, 299):
                            if radar_set2[i][m] == 0:
                                break
                            else:
                                for k in range(i, 299):
                                    if radar_set2[k][m] == 0:
                                        break
                                    else:
                                        vol = vol + radar_set2[k][m]
                        volume.append(vol)
                        vol = 0
                                    
    print(volume)
    
    matplotlib.pyplot.imshow(radar_set2)
    
model2()
