from flask import Flask, jsonify

app = Flask(__name__)

# Environment variables (mocked for now)
import os
api_token = os.getenv("API_TOKEN", "MySecureToken")
api_url = os.getenv("API_URL", "https://fakeweatherservice.com/getforecast")

# Routes
@app.route("/")
def home():
    return f"Welcome Sir!"

@app.route("/dashboard")
def dashboard():
    weather_data = {
        "API_TOKEN": api_token,
        "API_URL": api_url
    }
    return jsonify(weather_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
