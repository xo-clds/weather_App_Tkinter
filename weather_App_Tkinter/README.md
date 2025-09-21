# Weather App (Tkinter + OpenWeatherMap API)

A simple desktop GUI Weather App built with **Tkinter** in Python.  
It fetches real-time weather data for any city using the **OpenWeatherMap API** and displays temperature, humidity, weather description, and an icon.

## Features
- Enter a city name and get current weather information  
- Temperature in **Celsius** and **Fahrenheit**  
- Weather description (e.g., Clear, Clouds, Rain)  
- Humidity display  
- Weather icon displayed dynamically

## Screenshot

<p align="center">
  <img src="screenshots/screenshot1.png" alt="Weather App Screenshot" width="600">
</p>


## Installation

1. Clone the repository:
    ```
    git clone https://github.com/xo-clds/Weather_App_Tkinter.git
    cd Weather_App_Tkinter
    ```

2. **Install required Python packages:**
    ```
    pip install -r requirements.txt
    ```

## Usage

1. Open the folder containing `weather_app.py`.
2. Run the app using Python:
    ```
    python weather_app.py
    ```

## How to Add Your API Key

1. Sign up at [OpenWeatherMap](https://openweathermap.org/) to get your free API key.
2. Open `weather_app.py` in a code editor.
3. Replace the line:
    ```
    API_KEY = "YOUR_API_KEY_HERE"
    ```

## Troubleshooting

- If the app shows “City not found”, check the spelling or try another city.
- Make sure your internet connection is active.
- Ensure your OpenWeatherMap API key is correct.

## Dependencies

- Python 3.x
- Tkinter (usually included with Python)
- requests
- Pillow