import csv

class Ice:
    # Set variables
    def __init__(self, lidar_set, radar_set):
        self.lidar_set = lidar_set
        self.radar_set = radar_set
        
    def lidar(self):
        lidar_set = []
        f = open('lidar1.txt', newline='')
        dataset_lidar = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
        for row in dataset_lidar:
            rowlist_lidar = []
            for value in row:
                rowlist_lidar.append(value)
            lidar_set.append(rowlist_lidar)
        f.close()
        
    def radar(self):
        radar_set = []
        f = open('radar1.txt', newline='')
        dataset_radar = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
        for row in dataset_radar:
            rowlist_radar = []
            for value in row:
                rowlist_radar.append(value)
            radar_set.append(rowlist_radar)
        f.close()