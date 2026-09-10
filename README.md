# 🌦️ Real-Time Weather Forecast Web Application

A simple and user-friendly **Real-Time Weather Forecast Web Application** developed using **Python, Flask, HTML, CSS, and the OpenWeatherMap API**.

The application allows users to enter a city name and retrieve real-time weather information. The interface dynamically changes its background according to the current weather condition.

---

## 📌 Project Overview

Weather information is an important part of everyday life, helping people plan travel, outdoor activities, work, and other daily tasks.

This project provides a web-based solution for obtaining real-time weather information for a selected city. The application connects to the **OpenWeatherMap API**, retrieves the latest weather data, processes the API response using Python and Flask, and displays the information through a simple and interactive web interface.

The application also provides weather-specific background images and icons to make the interface more visually interactive.

---

## ✨ Features

- 🌍 Search weather information by city name
- 🌡️ Display current temperature
- ☁️ Display current weather condition
- 💧 Display humidity information
- 💨 Display wind speed
- 🌤️ Weather-specific icons
- 🖼️ Dynamic background images based on weather conditions
- 🔎 Simple city search interface
- ❌ Handles invalid or unavailable city names
- 📱 User-friendly web interface
- 🔐 API key protected using environment variables
- ⚡ Real-time weather data using OpenWeatherMap API

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Backend programming |
| Flask | Web application framework |
| HTML | Web page structure |
| CSS | Web page styling |
| OpenWeatherMap API | Real-time weather data |
| Requests | API communication |
| python-dotenv | Secure API key management |
| Git & GitHub | Version control and project hosting |

---

## 🏗️ System Architecture

The application follows a simple client-server architecture.

```text
                 ┌──────────────────────┐
                 │       User           │
                 │  Enters City Name    │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │      HTML / CSS      │
                 │    Web Interface     │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │       Flask          │
                 │   Python Backend     │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │ OpenWeatherMap API   │
                 │  Real-Time Weather   │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │    JSON Response     │
                 │ Weather Information  │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │ Flask Processes Data │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │ Weather Result Page  │
                 │ Temperature, Humidity│
                 │ Wind & Condition     │
                 └──────────────────────┘
```
----

## 📁 Project Structure

```
real-time-weather-forecast/
├── app.py
├── requirements.txt
├── .gitignore
├── templates/
│   └── index.html
└── static/
    └── images/
```
---

## ⚙️ Installation & Setup
```
git clone https://github.com/ff221625-code/real-time-weather-forecast.git
cd real-time-weather-forecast
pip install -r requirements.txt
```
---

## 📸 Screenshots

### 🌦️ Weather Forecast Interface
```
![Weather Forecast](screenshots/weather.png)
```
---

## 🚀 Future Enhancements

- 📅 5-day or 7-day weather forecast
- 📍 Automatic location detection
- 🗺️ Interactive weather maps
- 🌅 Sunrise and sunset information
- 🌡️ Feels-like temperature
- 📊 Weather charts and graphs
- 🌧️ Precipitation probability
- 🌍 Multiple location comparison

---

## 👩‍💻 Author

Firdous Fathima

Computer Science & Engineering
