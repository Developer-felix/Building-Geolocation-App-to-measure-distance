from django.shortcuts import render,get_bject_or_404
from .models import Measurement

def calculate_distance_view(request):
    obj = get_bject_or_404(Measurement, id=1)
    context = {
        'distance' : obj,
    }
    return render(request,'measurements/main.html',context)
