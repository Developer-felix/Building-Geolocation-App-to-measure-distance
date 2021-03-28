from django.shortcuts import render,get_object_or_404
from .models import Measurement
from .forms import MeasurementModelForm
from geopy.geocoders import Photon
from geopy.distance import geodesic
from .utils import get_geo
# Nominatim
def calculate_distance_view(request):
    obj = get_object_or_404(Measurement, id=1)
    form = MeasurementModelForm(request.POST or None)
    geolocator = Photon(user_agent="measurements")

    ip = "72.14.207.99"
    country, city, lat, lon = get_geo(ip)
    print("location country", country)
    print("location city", city)
    print("location lat", lat)
    print("location lon", lon)
    
    location = geolocator.geocode(city)
    print('###', location)
    
    l_lat = lat
    l_lon = lon
    pointA = (l_lat , l_lon)

    if form.is_valid():
        instance = form.save(commit=False)
        destination_ = form.cleaned_data.get('destination')
        destination = geolocator.geocode(destination_)
        print(destination)
        d_lat = destination.latitude
        d_lon = destination.longitude

        pointB = (d_lat , d_lon)



        instance.location = "Kitale"
        instance.distance = 1000.00
        # instance.save()
    context = {
        'distance': obj,
        'form' : form,
    }
    return render(request,'measurements/main.html',context)
