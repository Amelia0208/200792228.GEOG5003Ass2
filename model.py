import csv
import matplotlib

lidar_set = []
radar_set = []
volume = []
mass = []
can_pull = []


def identify_ice():
    for i in range(299):
        for j in range(299):
            if radar_set[i][j] >= 100:
                radar_set[i][j] = 1
            else:
                radar_set[i][j] = 0
                    
                    
def calc_volume():
    vol = 0
    for i in range(1, 298):
        for j in range(1, 298):
            if radar_set[i - 1][j] != 0:
                pass
            else: 
                if radar_set[i][j - 1] != 0:
                    pass
                else:
                    if radar_set[i][j] != 0:
                        for m in range(j, 299):
                            if radar_set[i][m] == 0:
                                break
                            else:
                                for k in range(i, 299):
                                    if radar_set[k][m] == 0:
                                        break
                                    else:
                                        vol = vol + lidar_set[k][m]
                        volume.append(vol)
                        vol = 0
                            
                            
def calc_mass():
    for i in range(len(volume)):
        ice_mass = volume[i] * 900
        mass.append(ice_mass)
            
            
def calc_can_pull():
    for i in range(len(volume)):
        if mass[i] <=36000000:
            can_pull_ice = 'yes'
        else:
            can_pull_ice = 'no'
        can_pull.append(can_pull_ice)
            
def print_results():
    for i in range(len(volume)):
        print('Iceberg ' + str(i + 1) + ':\nVolume: ' + str(volume[i]) + '\nMass: ' + str(mass[i]) + '\nCan be pulled: ' + str(can_pull[i]) + '\n\n')
        
def plot():
    matplotlib.pyplot.xlim(0, 299) # Environment needs to be set
    matplotlib.pyplot.ylim(0, 299)  
    matplotlib.pyplot.imshow(radar_set)


def model1():    
    f = open('lidar1.txt', newline='')
    dataset_lidar = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in dataset_lidar:
        rowlist_lidar = []
        for value in row:
            rowlist_lidar.append(value)
        lidar_set.append(rowlist_lidar)
    f.close()
        
        
    f = open('radar1.txt', newline='')
    dataset_radar = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in dataset_radar:
        rowlist_radar = []
        for value in row:
            rowlist_radar.append(value)
        radar_set.append(rowlist_radar)
    f.close()
    
    identify_ice()
    calc_volume()
    calc_mass()
    calc_can_pull()
    print_results()
    plot()
    
    


def model2():
    matplotlib.pyplot.xlim(0, 299) # Environment needs to be set
    matplotlib.pyplot.ylim(0, 299)
    
    f = open('lidar2.txt', newline='')
    dataset_lidar = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in dataset_lidar:
        rowlist_lidar = []
        for value in row:
            rowlist_lidar.append(value)
        lidar_set.append(rowlist_lidar)
    f.close()
        
        
    f = open('radar2.txt', newline='')
    dataset_radar = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in dataset_radar:
        rowlist_radar = []
        for value in row:
            rowlist_radar.append(value)
        radar_set.append(rowlist_radar)
    f.close()
    
    identify_ice()
    calc_volume()
    calc_mass()
    calc_can_pull()
    print_results()
    plot()
    
model2()
    
