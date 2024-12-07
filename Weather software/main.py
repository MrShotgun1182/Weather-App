import tkinter as tk
from tkinter import messagebox
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
from PIL import Image, ImageTk

def get_weather():
    try:
        # location
        city = textfile.get()
        geolocator = Nominatim(user_agent="geopiExercises")
        location = geolocator.geocode(city)
        lat, lng = location.latitude, location.longitude
        TZF = TimezoneFinder()
        TZF_value = TZF.timezone_at(lat=lat, lng=lng)
        city_label.config(text=TZF_value.split("/")[1])
        
        # time
        home = pytz.timezone(TZF_value)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        time_label.config(text=current_time)
        local_time_label.config(text="LOCAL TIME")
        
        # weather
        api_key = "58ebdebf4976680cae5dbfe25c859f7d"
        api = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid={api_key}"
        jsond_data = requests.get(api).json()
        condition = jsond_data["weather"][0]["main"]
        description = jsond_data["weather"][0]["description"]
        temp = int(jsond_data["main"]["temp"] - 273.15)
        pressure = jsond_data["main"]["pressure"]
        humidity = jsond_data["main"]["humidity"]
        wind = jsond_data["wind"]["speed"]
        
        temp_label.config(text=f"{temp} °")
        PRESSURE_label.config(text=f"{pressure}")
        condition_label.config(text=f"{condition} | FEELS LIKE {temp} °")
        wind_label.config(text=wind)
        HUMIDITY_label.config(text=humidity)
        DESCRIPTION_label.config(text=description)
        
    except Exception as err:
        print(err)
        messagebox.showerror("Weater App", "Invalid Entry!!!")
        

# make defult window
root = tk.Tk()
root.title("Weather app")
root.geometry("900x500+300+200") # can set the size of window
root.resizable(False, False) # user can't change window size

# add serch box
top_img = tk.PhotoImage(file="search.png")
top_img_label = tk.Label(root, image=top_img)
top_img_label.pack(side=tk.TOP, pady=20)
# config  top_img
textfile = tk.Entry(root, justify="center",
                    width=25,
                    font=("poppins", 15, "bold"),
                    bg="#404040", fg="white",
                    border=0
                    )
textfile.place(x=280, y=45)

# add search icon
search_img = tk.PhotoImage(file="search_icon.png")
search_img_button = tk.Button(root, image=search_img,
                              cursor="hand2",
                              bg="#404040",
                              command=get_weather,
                              border=0
                              )
search_img_button.pack(side=tk.RIGHT)
search_img_button.place(x=590, y=32)

# add my logo
main_logo_ = Image.open("Screenshot 2024-11-18 114049.png")
main_logo_ = main_logo_.resize((200,242))
main_logo = ImageTk.PhotoImage(main_logo_)
main_logo_label = tk.Label(image=main_logo)
main_logo_label.pack(side=tk.TOP)

# add buttom box
buttom_img = tk.PhotoImage(file="box.png")
buttom_img_label = tk.Label(image=buttom_img)
buttom_img_label.pack(side=tk.TOP)

# city name
city_label = tk.Label(root, font=("arial", 40, "bold"),
                      fg="#e355cd")
city_label.place(x=100, y=120)

# local time
local_time_label = tk.Label(root, font=("arial", 20, "bold"),
                      fg="#4b4bcc")
local_time_label.place(x=100, y=200)

# time
time_label = tk.Label(root, font=("Helvetica", 20, "bold"),
                      fg="#4b4bcc")
time_label.place(x=100, y=270)

# buttom label 
## WIND 
buttom_label1 = tk.Label(root, text="WIND",
                        font=("Helvetica", 15, "bold"),
                        fg="white", bg="#1ab5ef"
                        )
buttom_label1.place(x=700, y=390)

### WIND value
wind_label = tk.Label(root, text="...",
                      font=("arial", 13, "bold"),
                      bg="#1ab5ef", fg="#404040")
wind_label.place(x=700, y=420)

## humidity
buttom_label2 = tk.Label(root, text="HUMIDITY",
                        font=("Helvetica", 15, "bold"),
                        fg="white", bg="#1ab5ef"
                        )
buttom_label2.place(x=500, y=390)

### HUMIDITY value
HUMIDITY_label = tk.Label(root, text="...",
                      font=("arial", 13, "bold"),
                      bg="#1ab5ef", fg="#404040")
HUMIDITY_label.place(x=500, y=420)

## description
buttom_label3 = tk.Label(root, text="DESCRIPTION",
                        font=("Helvetica", 15, "bold"),
                        fg="white", bg="#1ab5ef"
                        )
buttom_label3.place(x=300, y=390)

### DESCRIPTION value
DESCRIPTION_label = tk.Label(root, text="...",
                      font=("arial", 13, "bold"),
                      bg="#1ab5ef", fg="#404040")
DESCRIPTION_label.place(x=300, y=420)

## pressure
buttom_label4 = tk.Label(root, text="PRESSURE",
                        font=("Helvetica", 15, "bold"),
                        fg="white", bg="#1ab5ef"
                        )
buttom_label4.place(x=100, y=390)

### PRESSURE value
PRESSURE_label = tk.Label(root, text="...",
                      font=("arial", 13, "bold"),
                      bg="#1ab5ef", fg="#404040")
PRESSURE_label.place(x=100, y=420)

# temp label
temp_label = tk.Label(root, font=("arial", 70, "bold"),
                      fg="#e355cd")
temp_label.place(x=600, y=120)

# condition label
condition_label = tk.Label(root, font=("arial", 20, "bold"),
                      fg="#e355cd")
condition_label.place(x=550, y=270)


# for run app we must run this code and set own code in mainloop
root.mainloop()
