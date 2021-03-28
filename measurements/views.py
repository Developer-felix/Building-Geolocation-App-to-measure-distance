from django.shortcuts import render,get_object_or_404
from .models import Measurement
from .forms import MeasurementModelForm
from geopy.geocoders import Photon
# Nominatim
def calculate_distance_view(request):
    obj = get_object_or_404(Measurement, id=1)
    form = MeasurementModelForm(request.POST or None)
    geolocator = Photon(user_agent="measurements")
    if form.is_valid():
        instance = form.save(commit=False)
        destination_ = form.cleaned_data.get('destination')
        destination = geolocator.geocode(destination_)
        print(destination)
        print(destination.latitude)
        print(destination.longitude)
        instance.location = "Kitale"
        instance.distance = 1000.00
        # instance.save()
    context = {
        'distance': obj,
        'form' : form,
    }
    return render(request,'measurements/main.html',context)
