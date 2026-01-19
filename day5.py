import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City parameter is required'}), 400
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY')
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)