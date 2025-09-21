import requests
from tkinter import *
from tkinter import messagebox
from datetime import datetime, timedelta
from PIL import Image, ImageTk
import io


# OpenWeatherMap
API_KEY = "6820c35475ef7e5aa01989e60c9575a6"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather():
    city = city_entry.get().strip()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric" 
    }

    try:
        response = requests.get(BASE_URL, params=params)
        if response.status_code == 200:
            data = response.json()
            
            # Extract data
            temp_c = data.get("main", {}).get("temp")
            temp_f = (temp_c * 9/5) + 32 if temp_c is not None else None
            humidity = data.get("main", {}).get("humidity", "N/A")
            weather_desc = data.get("weather", [{}])[0].get("description", "N/A").capitalize()
            icon_code = data.get("weather", [{}])[0].get("icon")
            
            # Local time
            dt_utc = datetime.utcfromtimestamp(data.get("dt", 0))
            timezone_offset = data.get("timezone", 0)
            local_time = dt_utc + timedelta(seconds=timezone_offset)
            local_time_str = local_time.strftime("%Y-%m-%d %H:%M:%S")
            
            # Update labels
            city_label.config(text=f"🌍 Weather in {city.title()}")
            time_label.config(text=f"📅 Time: {local_time_str}")
            temp_label.config(text=f"🌡 Temperature: {temp_c:.1f}°C / {temp_f:.1f}°F")
            condition_label.config(text=f"☁️ Condition: {weather_desc}")
            humidity_label.config(text=f"💧 Humidity: {humidity}%")

        
            if icon_code:
                icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
                icon_response = requests.get(icon_url)
                image_data = icon_response.content
                image = Image.open(io.BytesIO(image_data))
                image = image.resize((100, 100), Image.ANTIALIAS)
                weather_icon = ImageTk.PhotoImage(image)
                icon_label.config(image=weather_icon)
                icon_label.image = weather_icon

        else:
            messagebox.showerror("Error", f" Error {response.status_code}: City not found or invalid API key.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{e}")


root = Tk()
root.title("🌤 Weather App")
root.geometry("400x500")
root.resizable(False, False)


city_entry = Entry(root, font=("Arial", 16))
city_entry.pack(pady=20)
search_btn = Button(root, text="Get Weather", command=get_weather, font=("Arial", 14))
search_btn.pack(pady=10)

city_label = Label(root, text="", font=("Arial", 16, "bold"))
city_label.pack(pady=10)
time_label = Label(root, text="", font=("Arial", 12))
time_label.pack(pady=5)
temp_label = Label(root, text="", font=("Arial", 14))
temp_label.pack(pady=5)
condition_label = Label(root, text="", font=("Arial", 14))
condition_label.pack(pady=5)
humidity_label = Label(root, text="", font=("Arial", 14))
humidity_label.pack(pady=5)
icon_label = Label(root)
icon_label.pack(pady=10)

root.mainloop()
