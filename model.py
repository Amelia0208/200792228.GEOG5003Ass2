import icedetection
import matplotlib

def model1():
    icedetection.Ice.lidar1()
    icedetection.Ice.radar1()
    matplotlib.pyplot.xlim(0, 99) # Environment needs to be set
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.imshow(icedetection.Ice.lidar_set, icedetection.Ice.radar_set)
    
    
model1()