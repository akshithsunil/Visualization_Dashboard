from django.shortcuts import render
from .models import DataPoint


def index(request):
    data_points = DataPoint.objects.all()
    return render(request, 'Dashboard/index.html', {'data_points': data_points})