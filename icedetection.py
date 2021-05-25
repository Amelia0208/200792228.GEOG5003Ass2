import csv

class Ice:
    # Set variables
    def __init__(self, lidar_set1, radar_set1, lidar_set2, radar_set2):
        self.lidar_set1 = lidar_set1
        self.radar_set1 = radar_set1
        self.lidar_set2 = lidar_set2
        self.radar_set2 = radar_set2
        
    def lidar1(self, lidar_set1):
        f = open('lidar1.txt', newline='')
        dataset_lidar1 = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
        for row in dataset_lidar1:
            rowlist_lidar1 = []
            for value in row:
                rowlist_lidar1.append(value)
            lidar_set1.append(rowlist_lidar1)
        f.close()
        
    def radar1(self, radar_set1):
        radar_set1 = []
        f = open('radar1.txt', newline='')
        dataset_radar1 = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
        for row in dataset_radar1:
            rowlist_radar1 = []
            for value in row:
                rowlist_radar1.append(value)
            radar_set1.append(rowlist_radar1)
        f.close()
        
    def lidar2(self, lidar_set2):
        lidar_set2 = []
        f = open('lidar2.txt', newline='')
        dataset_lidar2 = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
        for row in dataset_lidar2:
            rowlist_lidar2 = []
            for value in row:
                rowlist_lidar2.append(value)
            lidar_set2.append(rowlist_lidar2)
        f.close()
        
    def radar2(self, radar_set2):
        radar_set2 = []
        f = open('radar2.txt', newline='')
        dataset_radar2 = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
        for row in dataset_radar2:
            rowlist_radar2 = []
            for value in row:
                rowlist_radar2.append(value)
            radar_set2.append(rowlist_radar2)
        f.close()