import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as pyplot
import csv
import tkinter

# Set empty parameters for data
lidar_set = [] 
radar_set = [] # These two are filled by calling on text files
volume = []
mass = []
can_pull = []


# Initialise main page
root = tkinter.Tk()
root.wm_title("Model")


# Start the GUI
fig = pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
carry_on = True
init = True
halted = False
rerunid = 0
total_ite = 0;


# Identify whether the material in the area is ice or not, and classify data
def identify_ice():
    for i in range(299):
        for j in range(299):
            if radar_set[i][j] >= 100:
                radar_set[i][j] = 1
            else:
                radar_set[i][j] = 0
                    
                    
# Calculate the total volume of each block of ice
def calc_volume():
    vol = 0 # Initialise basic volume for individual ice block
    for i in range(1, 298):
        for j in range(1, 298):
            if radar_set[i - 1][j] != 0:
                pass
            else: 
                if radar_set[i][j - 1] != 0: # Model will only calculate if at top left corner of ice block
                    pass
                else:
                    if radar_set[i][j] != 0:
                        for m in range(j, 299):
                            if radar_set[i][m] == 0:
                                break
                            else:
                                for k in range(i, 299):
                                    if radar_set[k][m] == 0: # Will finish adding heights if reaches a point with value 0
                                        break
                                    else:
                                        vol = vol + lidar_set[k][m] # Volume for individual ice block
                        volume.append(vol) # Create an array for volume of each
                        vol = 0 # Set volume back to 0 after each ice block to calculate individuals
                            
                            
# Calculate mass of each ice block within volume array
def calc_mass():
    for i in range(len(volume)):
        ice_mass = volume[i] * 900
        mass.append(ice_mass) # Create an array of mass
            
            
# Calculate if able to pull each ice block in array (can only pull if less than 36 million kg)
def calc_can_pull():
    for i in range(len(volume)):
        if mass[i] <=36000000:
            can_pull_ice = 'yes'
        else:
            can_pull_ice = 'no'
        can_pull.append(can_pull_ice) # Create array for ability to pull
            
# Print volume, mass and ability to move for each ice block in data, separately
def print_results():
    for i in range(len(volume)):
        print('Iceberg ' + str(i + 1) + ':\nVolume: ' + str(volume[i]) + '\nMass: ' + str(mass[i]) + '\nCan be pulled: ' + str(can_pull[i]) + '\n\n')
        
# Plot radar data for the data set
# This will be reclassified to only show ice in one colour, and non-ice in another
def plot():
    pyplot.xlim(0, 299) # Environment needs to be set
    pyplot.ylim(0, 299)  
    pyplot.imshow(radar_set)


# Run the model for first dataset
def model1():    
    
    # Reading data
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
    
    # Run based on data input above
    identify_ice()
    calc_volume()
    calc_mass()
    calc_can_pull()
    print_results()
    plot()
    
    


def model2():
    
    # Reading data
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
    
    # Run based on data input above
    identify_ice()
    calc_volume()
    calc_mass()
    calc_can_pull()
    print_results()
    plot()

# Set up menu on GUI to run models
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu) # Dropbox to select the model
model_menu.add_command(label="Run model 1", command=model1())
model_menu.add_command(label="Run model 2", command=model2())
model_menu.add_command(label="Exit", command=root.quit)
model_menu.add_command(label="Destroy", command=root.destroy)