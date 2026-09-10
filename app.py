from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("API_KEY")
@app.route("/", methods=["GET", "POST"])
def home():
    weather = None
    error = None
    background = "default.jpg"
    icon_url = None

    if request.method == "POST":
        city = request.form.get("city")

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)

        if response.status_code == 200:
            weather = response.json()
            if weather and "weather" in weather:
             condition = weather["weather"][0]["main"].lower()
             icon_code = weather["weather"][0]["icon"]
             icon_url = f"https://openweathermap.org/img/wn/{icon_code}@2x.png"
            
        
             if "cloud" in condition:
                background = "cloudy.jpg"
             elif "rain" in condition:
                background = "rainy.jpg"
             elif "clear" in condition:
                background = "clear.jpg"
             elif "snow" in condition:
                background = "snowy.jpg"
             elif "mist" in condition or "haze" in condition or "fog" in condition:
                background = "mist.jpg"
             else:
                background = "default.jpg"
        else:
            error = "Weather data error"

    return render_template("index.html", weather=weather, error=error, background=background,icon=icon_url)

if __name__ == "__main__":
    app.run(debug=True)