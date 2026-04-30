from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view to return the index page """
    weather = {
        'temperature': -2,
        'description': 'Partly Cloudy',
        'wind_speed': 8,
        'wind_direction': 'NW',
        'humidity': 68,
        'temp_min': -4,
        'temp_max': -1,
    }
    return render(request, 'home/index.html', {'weather': weather})


def how_it_works(request):
    """ A view to return the how it works page """
    return render(request, 'home/how_it_works.html')