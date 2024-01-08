from django.shortcuts import render
from django.http import JsonResponse
import requests
import json
from datetime import datetime
from .models import City
from .config import API_OPENW

def weather(request):
    if request.method == 'POST':
        city_name = request.POST.get('city_name')
        
        # Reservamos API response with matching cities
        res_api = f'https://search.reservamos.mx/api/v2/places?q={city_name}'
        response_res = requests.get(res_api)
        cities_data = response_res.json()
        
        # get cities only
        cities_only = [entry for entry in cities_data if entry['result_type'] == "city"]
        
        temperature_data = list()
        for city in cities_only:
            # Create OpenWeather API request
            lat, long = city['lat'], city['long']
            city_name, state, country = city['city_name'], city['state'], city['country']
            api_url = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={long}&exclude=hourly,minutely,alerts,current&appid={API_OPENW}'

            response = requests.get(api_url)
            data = response.json()

            if 'cod' not in data.keys():
                # Get temperatures in metric units and other relevant data
                for i in range(len(data['daily'])):
                    data['daily'][i]['temp']['max_c'] = "{:.2f}".format(data['daily'][i]['temp']['max'] - 273.15)
                    data['daily'][i]['temp']['min_c'] = "{:.2f}".format(data['daily'][i]['temp']['min'] - 273.15)
                    utc_date = datetime.utcfromtimestamp(data['daily'][i]['dt']).date()
                    data['daily'][i]['dt'] = utc_date.strftime('%Y-%m-%d')
                data['state'] = state
                data['country'] = country
                data['city'] = city_name
                temperature_data.append(data)
        
        # There is data to process    
        if len(temperature_data):
            temperature_data = json.dumps(temperature_data)
            temperature_data = json.loads(temperature_data)
            return render(request, 'weather_app/weather.html', {"temperature_data": temperature_data})
        else:
            return render(request, 'weather_app/weather.html',
                          {'success': False, 'message': "{}: {}".format(data['cod'],data['message'])})
    return render(request, 'weather_app/weather.html')