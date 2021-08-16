# biogas

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def convert_date(num):
    # need to fix date
    date = datetime.fromtimestamp(num).date()
    return(date)

def convert_time(num):
    time = datetime.fromtimestamp(num).time()
    time = time.strftime("%H:%M")
    return(time)

def read(file_name):
    cols = ["Time", "Radiation [W/m^2]", "Wind Speed [m/s]", "Wind Direction [Deg]",
            "TC8 Temp [C]", "TC2 Temp [C]", "TC9 Temp [C]", "TC6 Temp [C]", "TC10 Temp [C]",
            "TC12 Temp [C]", "TC13 Temp [C]", "TC14 Temp [C]"]
    data = pd.read_csv(file_name, usecols=cols)
    
    # Read the data to a list
    only_time_col = data['Time']
    dates_list = []
    times_list = []

    # Iterate over the list and convert to date & hour
    for item in only_time_col:
        date = convert_date(item)
        time = convert_time(item)
        dates_list.append(date)
        times_list.append(time)

    # Add each list as a new col to the dataframe
    data['date'] = dates_list
    data['time'] = times_list

    arr_time = data["time"].to_numpy()
    x_label = arr_time[0::120]
    
    # Remove the Time col
    data.drop('Time', axis=1, inplace=True)
    
    plt.plot(data["time"], data["TC8 Temp [C]"], '.', label='8 - Front Gas Tank', color='blue')
    plt.plot(data["time"], data["TC2 Temp [C]"], '.', label='2 - Back Gas Tank', color='orange')
    plt.plot(data["time"], data["TC9 Temp [C]"], '.', label='9 - Back Cover', color='green')
    plt.plot(data["time"], data["TC6 Temp [C]"], '.', label='6 -Ground', color='red')
    plt.plot(data["time"], data["TC10 Temp [C]"], '.', label='10 - Front Cover', color='purple')
    plt.plot(data["time"], data["TC12 Temp [C]"], '.', label='12 - Front Digester', color='brown')
    plt.plot(data["time"], data["TC13 Temp [C]"], '.', label='13 - Back Digester', color='pink')
    plt.plot(data["time"], data["TC14 Temp [C]"], '.', label='14 - Atmosphere', color='grey')
    plt.legend(loc='best', fancybox=True, framealpha=1, shadow=True, borderpad=1, prop={"size": 5})
    plt.grid()
    plt.xlabel('Time [hours]')
    plt.xticks(ticks=x_label, labels=x_label, fontsize=10, rotation=90)
    # plt.xticks(fontsize=5, rotation=90)
    plt.ylabel('Temp [C]')
    plt.show()
   
read("July3 (22-07-2021_16.08.15).csv")
