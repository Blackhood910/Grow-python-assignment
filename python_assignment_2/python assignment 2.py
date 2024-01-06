"""
Python Assignment Grow data set

this assignment has 2 main function 
1. cleaning the data given in the data set 
2. ploting the clean data set to the map image
    """


#loading the pandas , matplot and pyplot
import pandas as pd 
import matplotlib.pyplot as plt

# here define the variable according to the  bounding box given

H_lat =57.985 # highest latitude
L_lat =50.681 # lowest latitude
H_long = 1.6848  # highest Longitude
L_long =-10.592 # lowest Longitude

def data_cleaning(df) :
    """
    this function take a data frame as an argument and clean the  dataframe by  removing duplicate value from the dataset 
    swaping the values of longitude and latitude to get the correct value and filtering the value of the coordinate of the sensors
    according to the bounding box given
    """
        
    df['Latitude'], df['Longitude'] = df['Longitude'], df['Latitude'] # swap value
        
    df = df[(df['Latitude'] >= L_lat) & (df['Latitude'] <= H_lat) & #provide boundry to the oordinate of the sensors
        (df['Longitude'] >= L_long) & (df['Longitude'] <=H_long)]
        
    df = df.groupby(['Latitude', 'Longitude']).first().reset_index() # revoming duplicate values
        
    return df


def map_ploting(df , map):
    
    """
    this function take a data frame and the map image as  arguments and creates a subplot with a specified size using plt.subplots.
    to displays the map image on the subplot with the specified extent then It plots the sensor locations on the map using red scatter points.
    The plot is saved as 'ouputfile_image.png'.
    """
    fig, ax = plt.subplots(figsize=(12, 12))           
    ax.imshow(map, extent=[L_long,H_long, L_lat, H_lat])
    ax.scatter(df['Longitude'], df['Latitude'], color='red', s=20, label='Sensor')
    plt.title('Grow Sensors')
    plt.legend()
    plt.savefig('ouputfile_image.png')
        
        

df = pd.read_csv('GrowLocations.csv', encoding='utf-8') # fetching data from GrowLocations.csv and storing in df dataframe
pic = plt.imread('map7.png')  # fetching image map7.png and storing in pic variable

cl_df=data_cleaning(df) # calling the data cleaning function and storing it in cl_df
map_ploting(cl_df , pic) # use map ploting function to plot sensors in the map



