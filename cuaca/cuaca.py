import requests
from datetime import datetime

API_KEY = "1fe5f03e8b679377cbc41601289edfdd"
CITY = "Jakarta"
API_URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(API_URL)
data = response.json()

daily_forecast = {}
for forecast in data["list"]:
    date = datetime.utcfromtimestamp(forecast["dt"]).strftime("%a, %d %b %Y")
    if date not in daily_forecast:
        daily_forecast[date] = forecast["main"]["temp"]

print("Weather Forecast:")
for date, temp in list(daily_forecast.items())[:7]:  
    print(f"{date}: {temp:.2f}°C")
