import requests
import matplotlib.pyplot as plt

API_KEY = "aba11ee3b15cf997ba5c1bf3bb3693ef"

def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        print("Error fetching data:", data.get("message", "Unknown error"))
        return None

    weather_info = {
        "City": city.title(),
        "Temperature (°C)": data['main']['temp'],
        "Humidity (%)": data['main']['humidity'],
        "Pressure (hPa)": data['main']['pressure'],
    }
    return weather_info

def plot_weather_data(weather_data):
    labels = list(weather_data.keys())[1:]  # Skip city name
    values = list(weather_data.values())[1:]

    plt.figure(figsize=(8, 5))
    bars = plt.bar(labels, values, color=['skyblue', 'lightgreen', 'salmon'])

    plt.title(f"Weather in {weather_data['City']}")
    plt.ylabel("Values")
    plt.xlabel("Weather Parameters")

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval + 1, f'{yval}', ha='center', va='bottom')

    plt.tight_layout()
    plt.savefig("weather_visualization.png")
    plt.show()

# --- MAIN EXECUTION ---
city = input("Enter a city name: ")
weather = get_weather_data(city)

if weather:
    print("\nFetched Weather Data:")
    for key, value in weather.items():
        print(f"{key}: {value}")
    plot_weather_data(weather)
