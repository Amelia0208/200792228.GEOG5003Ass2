import matplotlib
import csv

class Ice:
    # Set variables
    def __init__(self):
        self.x = 0
        self.y = 0
        self.radar_set = []
        self.lidar_set = []
        self.vol = 0
        self.volume = []
        self.mass = []
        self.can_pull = []
        
  
  # Read data for model 1 
  def call_1_():
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
        
        
    # Read data for model 2
    def call_2_(self, radar_set, lidar_set):
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
        
        
    # Reclassify radar data to show ice / no ice
    def identify_ice():
        for i in range(299):
            for j in range(299):
                if radar_set[i][j] >= 100:
                    radar_set[i][j] = 1
                else:
                    radar_set[i][j] = 0
                    
                    
    # Create an array of volumes for each iceberg in data
    def calc_volume():
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
                            
                            
    # Create an array of mass for each iceberg
    def calc_mass():
        for i in range(len(volume)):
            ice_mass = volume[i] * 900
            mass.append(ice_mass)
            
            
    # Create an array for abaility to pull each iceberg
    def calc_can_pull():
        for i in range(len(volume)):
            if mass[i] <=36000000:
                can_pull_ice = 'yes'
            else:
                can_pull_ice = 'no'
            can_pull.append(can_pull_ice)
            
    # Print out volume, mass and ability to pull for each iceberg
    def print_results():
        for i in range(len(volume)):
            print('Iceberg ' + str(i + 1) + ':\nVolume: ' + str(volume[i]) + '\nMass: ' + str(mass[i]) + '\nCan be pulled: ' + str(can_pull[i]) + '\n\n')
        
    # Plot classified radar to show ice / no ice
    def plot():
        matplotlib.pyplot.xlim(0, 299) # Environment needs to be set
        matplotlib.pyplot.ylim(0, 299)
        
        matplotlib.pyplot.imshow(radar_set)
    
    