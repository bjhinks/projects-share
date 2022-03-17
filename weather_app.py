import requests
import tkinter as tk
from tkinter import ttk

# Program that takes a city as input from the user and gives the current weather data
# for the city input


def get_weather_data():
    """"
    Function that requests weather data from the openweathermap server
    :return weather_data - returns all the current weather data of the city input by the user
    """

    city = str_user_city.get()
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    api_key = "66e5b7a5d893e1f61fe161ad680a2ad4"  # Get from https://home.openweathermap.org/api_keys
    url = f'{base_url}q={city}&appid={api_key}'
    weather_data = requests.get(url)

    print(weather_data)
    return weather_data.json()


def set_weather_data():
    # Function that sets the weather data into its appropriate entry box
    if str_user_city.get() == "":
        str_user_city.set("Please enter valid city :)")
    else:
        try:
            data = get_weather_data()
            current_temp = data.get('main')['temp']
            feels_like_temp = data.get('main')['feels_like']
            min_temp = data.get('main')['temp_min']
            max_temp = data.get('main')['temp_max']
            descript = data.get('weather')[0]['description']
            wind_speed = data.get('wind')['speed']
            wind_gust = data.get('wind')['gust']

            str_current_temp.set(f'{round(current_temp - 273.15, 1)} C')
            str_feels_like.set(f'{round(feels_like_temp - 273.15, 1)} C')
            str_min_temp.set(f'{round(min_temp - 273.15, 1)} C')
            str_max_temp.set(f'{round(max_temp - 273.15, 1)} C')
            str_descript.set(f'{descript}')
            str_wind_speed.set(f'{round(wind_speed * 3.6)} km/h')
            str_wind_gust.set(f'{round(wind_gust * 3.6)} km/h')
        except Exception as e:
            str_user_city.set("Something went wrong :(")
            print(e)


root = tk.Tk()

# Create root window
root.title('My Weather App')
root.geometry('300x250')

# Create the main frame
frame_home = ttk.Frame(root)
frame_home.pack(fill=tk.BOTH, expand=True)

# Create labels for text boxes to display the city input by the user as well as the current
# weather data for that city
ttk.Label(frame_home, text='Enter City:').grid(column=0, row=0)
ttk.Label(frame_home, text='Current Temp:').grid(column=0, row=2)
ttk.Label(frame_home, text='Feels Like Temp:').grid(column=0, row=3)
ttk.Label(frame_home, text='Min. Temp:').grid(column=0, row=4)
ttk.Label(frame_home, text='Max. Temp:').grid(column=0, row=5)
ttk.Label(frame_home, text='Weather Description:').grid(column=0, row=6)
ttk.Label(frame_home, text='Wind Speed:').grid(column=0, row=7)
ttk.Label(frame_home, text='Wind Gust:').grid(column=0, row=8)

# Entry Box for the user to input the city they want to get the weather for
str_user_city = tk.StringVar()
ttk.Entry(frame_home, width=25, textvariable=str_user_city).grid(column=1, row=0)

# Get Weather Data button that gets all the current weather data for the user's input city
ttk.Button(frame_home, text='Get Weather Data', width=18, command=set_weather_data).grid(column=0, row=1, columnspan=55)

# Entry box to display current temp in celsius
str_current_temp = tk.StringVar()
ttk.Entry(frame_home, width=15, textvariable=str_current_temp, state=tk.DISABLED).grid(column=1, row=2)

# Entry box to display feels like temp in celsius
str_feels_like = tk.StringVar()
ttk.Entry(frame_home, width=15, textvariable=str_feels_like, state=tk.DISABLED).grid(column=1, row=3)

# Entry box to display the minimum expected temp for the day in celsius
str_min_temp = tk.StringVar()
ttk.Entry(frame_home, width=15, textvariable=str_min_temp, state=tk.DISABLED).grid(column=1, row=4)

# Entry box to display the maximum expected temp for the day in celsius
str_max_temp = tk.StringVar()
ttk.Entry(frame_home, width=15, textvariable=str_max_temp, state=tk.DISABLED).grid(column=1, row=5)

# Entry box to display description of the weather (Ex. Cloudy, Snow, Rain, etc.)
str_descript = tk.StringVar()
ttk.Entry(frame_home, width=15, textvariable=str_descript, state=tk.DISABLED).grid(column=1, row=6)

# Entry box to display wind speed in km/h
str_wind_speed = tk.StringVar()
ttk.Entry(frame_home, width=15, textvariable=str_wind_speed, state=tk.DISABLED).grid(column=1, row=7)

# Entry box to display wind gust speed in km/h
str_wind_gust = tk.StringVar()
ttk.Entry(frame_home, width=15, textvariable=str_wind_gust, state=tk.DISABLED).grid(column=1, row=8)

root.mainloop()

"""
Format of weather data:

coord {'lon': -79.4163, 'lat': 43.7001}
weather [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]
base stations
main {'temp': 268.58, 'feels_like': 268.58, 'temp_min': 267.88, 'temp_max': 269.87, 'pressure': 1017, 'humidity': 80}
visibility 10000
wind {'speed': 0.45, 'deg': 76, 'gust': 4.02}
clouds {'all': 100}
dt 1643343038
sys {'type': 2, 'id': 2010632, 'country': 'CA', 'sunrise': 1643287165, 'sunset': 1643322072}
timezone -18000
id 6167865
name Toronto
cod 200
"""
