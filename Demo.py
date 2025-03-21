from flask import Flask, request, jsonify, render_template

api_key = "RANDOM_API_KEY"
url = "https://api.openweathermap.org/data/2.5/"

def weather_data(city):
    try:
        current_weather_url = f"{url}weather?q={city}&appid={api_key}&units=metric"
        forecast_url = f"{url}forecast?q={city}&appid={api_key}&units=metric"
        
        current_response = requests.get(current_weather_url)
        forecast_response = requests.get(forecast_url)
        
        if current_response.status_code != 200 or forecast_response.status_code != 200:
            return None
        
        current_data = current_response.json()
        forecast_data = forecast_response.json()
        
        result = {
            "city": current_data["name"],
            "temperature": current_data["main"]["temp"],
            "description": current_data["weather"][0]["description"],
            "humidity": current_data["main"]["humidity"],
            "forecast": [
                {
                    "date": item["dt_txt"],
                    "temp": item["main"]["temp"],
                    "desc": item["weather"][0]["description"]
                } for item in forecast_data["list"] if "12:00:00" in item["dt_txt"]
            ]
        }
        return result
    except Exception as e:
        return None
