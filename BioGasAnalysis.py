import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from scipy.integrate import odeint

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
    # df['Time_str'] = data["Time"].apply(lambda x: x.strftime("%H %M"))

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

    # plt.plot(data["time"], data["TC8 Temp [C]"], '.', label='8 - Front Gas Tank', color='blue')
    # plt.plot(data["time"], data["TC2 Temp [C]"], '.', label='2 - Back Gas Tank', color='orange')
    # plt.plot(data["time"], data["TC9 Temp [C]"], '.', label='9 - Back Cover', color='green')
    # plt.plot(data["time"], data["TC6 Temp [C]"], '.', label='6 -Ground', color='red')
    # plt.plot(data["time"], data["TC10 Temp [C]"], '.', label='10 - Front Cover', color='purple')
    # plt.plot(data["time"], data["TC12 Temp [C]"], '.', label='12 - Front Digester', color='brown')
    # plt.plot(data["time"], data["TC13 Temp [C]"], '.', label='13 - Back Digester', color='pink')
    # plt.plot(data["time"], data["TC14 Temp [C]"], '.', label='14 - Atmosphere', color='grey')
    plt.legend(loc='best', fancybox=True, framealpha=1, shadow=True, borderpad=1, prop={"size": 5})
    plt.grid()
    plt.xlabel('Time [hours]')
    plt.xticks(ticks=x_label, labels=x_label, fontsize=10, rotation=90)
    # plt.xticks(fontsize=5, rotation=90)
    plt.ylabel('Temp [C]')
    # plt.show()

    # plt.plot(data["time"], data["Radiation [W/m^2]"], '.', label='Radiation', color='red')

    ax1 = plt.subplots()
    radiation = data["Radiation [W/m^2]"]
    atmosphere = data["TC14 Temp [C]"]
    t = data["time"]
    ax1.plot(t, radiation, '.', label='Radiation', color='red')
    ax1.xlabel('Time [hours]')
    ax1.ylabel('Radiation [W/m^2]')

    ax2 = ax1.twinx()
    ax2.plot(t, atmosphere, '.', label='14 - Atmosphere', color='grey')
    ax2.ylabel("Temp [C]")

    plt.show()


    # plt.legend(loc='best', fancybox=True, framealpha=1, shadow=True, borderpad=1, prop={"size": 5})
    # plt.grid()
    # plt.xlabel('Time [hours]')
    # plt.xticks(ticks=x_label, labels=x_label, fontsize=10, rotation=90)
    # plt.ylabel('Radiation [W/m^2]')
    # plt.twinx(data["TC14 Temp [C]"])
    plt.show()

    time_arr = pd.read_csv(file_name, usecols=["Time"]).to_numpy()
    time_pd = pd.read_csv(file_name, usecols=["Time"])
    time_real = pd.to_datetime(time_pd, unit='s')
    # print(time_real)
    a = convert_time(time_arr[0][0])
    # print(a.strftime("%H %M"))
    # time_trans = np.transpose(time_arr)
    # time_list = time_trans.tolist()
    # time_converted = for i in range(len(time_list)): time_list[i][0] = convert_time(time_list[i][0])
    # time_new = []
    # for i in range(len(time_arr)-1):
    #     time_list[0][i] = convert_time(time_list[0][i])
        # time_new.append(time_list[0][i])
    # time = pd.read_csv(file_name, usecols=["Time"]).to_numpy()
    radiation = pd.read_csv(file_name, usecols=["Radiation [W/m^2]"]).to_numpy()
    wind_speed = pd.read_csv(file_name, usecols=["Wind Speed [m/s]"]).to_numpy()
    wind_direction = pd.read_csv(file_name, usecols=["Wind Direction [Deg]"]).to_numpy()
    # tc8 = pd.read_csv(file_name, usecols=["TC8 Temp [C]"]).to_numpy()
    # tc2 = pd.read_csv(file_name, usecols=["TC2 Temp [C]"]).to_numpy()
    # tc9 = pd.read_csv(file_name, usecols=["TC9 Temp [C]"]).to_numpy()
    # tc6 = pd.read_csv(file_name, usecols=["TC6 Temp [C]"]).to_numpy()
    # tc10 = pd.read_csv(file_name, usecols=["TC10 Temp [C]"]).to_numpy()
    # tc12 = pd.read_csv(file_name, usecols=["TC12 Temp [C]"]).to_numpy()
    # tc13 = pd.read_csv(file_name, usecols=["TC13 Temp [C]"]).to_numpy()
    # tc14 = pd.read_csv(file_name, usecols=["TC14 Temp [C]"]).to_numpy()

    # tc8_trans = np.transpose(tc8_arr)
    # tc8_list = tc8_trans.tolist()

    # print (convert_time(time[0]))
    # print(time_list[0][1794])
    # print(time_list)
    # plt.plot(time_arr, radiation, '.', label='Radiation [W/m^2]', color='red')

    # fig = plt.figure()
    # ax = fig.add_subplot(1, 1, 1)
    # major_ticks = np.arange(0, 101, 10)
    # minor_ticks = np.arange(0, 101, 2)
    # ax.set_xticks(major_ticks)
    # ax.set_xticks(minor_ticks, minor=True)
    # ax.set_yticks(major_ticks)
    # ax.set_yticks(minor_ticks, minor=True)
    # ax.grid(which='both')
    # ax.grid(which='minor', alpha=0.2)
    # ax.grid(which='major', alpha=0.5)

    # plt.plot(time_arr, tc8, '.', label='8 - Front Gas Tank')
    # plt.plot(time_arr, tc2, '.', label='2 - Back Gas Tank')
    # plt.plot(time_arr, tc9, '.', label='9 - Back Cover')
    # plt.plot(time_arr, tc6, '.', label='6 -Ground')
    # plt.plot(time_arr, tc10, '.', label='10 - Front Cover')
    # plt.plot(time_arr, tc12, '.', label='12 - Front Digester')
    # plt.plot(time_arr, tc13, '.', label='13 - Back Digester')
    # plt.plot(time_arr, tc14, '.', label='14 - Atmosphere')
    # plt.legend(loc='upper right', fancybox=True, framealpha=1, shadow=True, borderpad=1, prop={"size":5})
    # plt.grid()
    # plt.xlabel('Time')
    # plt.ylabel('Temp [C]')
    # plt.title("From " + str(convert_date(time_arr[0][0])) + " at " + str(convert_time(time_arr[0][0])) +
      #        " Until " + str(convert_date(time_arr[1439][0] + " at "
       #                                    + str(convert_time(time_arr[1439][0])))))
    # plt.show()



read("July3 (22-07-2021_16.08.15).csv")