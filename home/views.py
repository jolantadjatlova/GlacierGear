from django.shortcuts import render
import requests
 
 
def index(request):
    """ A view to return the index page with live weather for Borlänge """
    weather = None
    try:
        url = (
            "https://api.open-meteo.com/v1/forecast"
            "?latitude=60.4858&longitude=15.4369"
            "&current=temperature_2m,relative_humidity_2m,"
            "weather_code,wind_speed_10m,wind_direction_10m"
            "&daily=temperature_2m_max,temperature_2m_min"
            "&timezone=Europe%2FStockholm&forecast_days=1"
        )
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            current = data.get('current', {})
            daily = data.get('daily', {})
 
            # Map WMO weather codes to descriptions
            code = current.get('weather_code', 0)
            description = get_weather_description(code)
 
            weather = {
                'temperature': round(current.get('temperature_2m', 0)),
                'description': description,
                'wind_speed': round(current.get('wind_speed_10m', 0)),
                'humidity': current.get('relative_humidity_2m', 0),
                'temp_min': round(daily.get('temperature_2m_min', [0])[0]),
                'temp_max': round(daily.get('temperature_2m_max', [0])[0]),
            }
    except Exception:
        # Graceful fallback if API fails
        weather = {
            'temperature': None,
            'description': 'Weather unavailable',
            'wind_speed': None,
            'humidity': None,
            'temp_min': None,
            'temp_max': None,
        }
 
    return render(request, 'home/index.html', {'weather': weather})
 
 
def get_weather_description(code):
    """Convert WMO weather code to human-readable description"""
    descriptions = {
        0: 'Clear Sky',
        1: 'Mainly Clear',
        2: 'Partly Cloudy',
        3: 'Overcast',
        45: 'Foggy',
        48: 'Icy Fog',
        51: 'Light Drizzle',
        53: 'Drizzle',
        55: 'Heavy Drizzle',
        61: 'Light Rain',
        63: 'Rain',
        65: 'Heavy Rain',
        71: 'Light Snow',
        73: 'Snow',
        75: 'Heavy Snow',
        77: 'Snow Grains',
        80: 'Light Showers',
        81: 'Showers',
        82: 'Heavy Showers',
        85: 'Snow Showers',
        86: 'Heavy Snow Showers',
        95: 'Thunderstorm',
        96: 'Thunderstorm with Hail',
        99: 'Thunderstorm with Heavy Hail',
    }
    return descriptions.get(code, 'Partly Cloudy')
 
 
def how_it_works(request):
    """ A view to return the how it works page """
    return render(request, 'home/how_it_works.html')
 
 
def terms(request):
    return render(request, 'home/terms.html')