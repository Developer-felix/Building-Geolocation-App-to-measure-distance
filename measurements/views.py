from django.shortcuts import render,get_object_or_404
from .models import Measurement
from .forms import MeasurementModelForm

def calculate_distance_view(request):
    obj = get_object_or_404(Measurement, id=1)
    form = MeasurementModelForm(request.POST or None)
    context = {
        'distance': obj,
        'form' : form,
    }
    return render(request,'measurements/main.html',context)
