import requests
from Demo import fetch_weather

app = Flask(__name__)

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "City parameter is required"}), 400
    
    weather_data = fetch_weather(city)
    if not weather_data:
        return jsonify({"error": "City not found or API error"}), 404
    
    return jsonify(weather_data)

if __name__ == '__main__':
    app.run(debug=True)
