from django.shortcuts import render,get_object_or_404
from .models import Measurement
from .forms import MeasurementModelForm
from geopy.geocoders import Photon
from geopy.distance import geodesic
from .utils import get_geo, get_center_coodinates,get_zoom
import folium

# Nominatim
def calculate_distance_view(request):
    #initial distance
    distance = None
    destination = None
    obj = get_object_or_404(Measurement, id=1)
    form = MeasurementModelForm(request.POST or None)
    geolocator = Photon(user_agent="measurements")

    ip = "72.14.207.99"
    country, city, lat, lon = get_geo(ip)
    
    location = geolocator.geocode(city)
    
    l_lat = lat
    l_lon = lon
    pointA = (l_lat, l_lon)
    
    #initial folium map
    m = folium.Map(width=750, height=500, location=get_center_coodinates(l_lat, l_lon),zoom_start=8)
    #location maker
    folium.Marker([l_lat , l_lon],tooltip="Click Here For More",popup=city['city'] ,icon=folium.Icon(color='purple')).add_to(m)

    if form.is_valid():
        instance = form.save(commit=False)
        destination_ = form.cleaned_data.get('destination')
        destination = geolocator.geocode(destination_)
        
        #destination cordinate
        d_lat = destination.latitude
        d_lon = destination.longitude

        pointB = (d_lat, d_lon)
        
        #distance calculations
        distance = round(geodesic(pointA , pointB).km , 2)

        #folium map modification
        m = folium.Map(width=750, height=500, location=get_center_coodinates(l_lat, l_lon, d_lat, d_lon), zoom_start=get_zoom(distance))
        #location maker
        folium.Marker([l_lat , l_lon],tooltip="Click Here For More",popup=city['city'], icon=folium.Icon(color='purple')).add_to(m)
        #destination maker
        folium.Marker([d_lat , d_lon],tooltip="Click Here For More",popup=destination ,icon=folium.Icon(color='red',icon='cloud')).add_to(m)

        #Draw the line between location and destination
        line = folium.PolyLine(locations=[pointA, pointB], weight=2, color='blue')
        m.add_child(line)

        instance.location = location
        instance.distance = distance
        instance.save()
    m = m._repr_html_()
    context = {
        'distance': distance,
        'destination':destination,
        'form': form,
        'map' : m,
    }
    return render(request,'measurements/main.html',context)
