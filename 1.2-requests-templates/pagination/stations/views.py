from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
import csv
from django.core.paginator import Paginator

def index(request):
    return redirect(reverse('bus_stations'))

def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    with open(settings.BUS_STATION_CSV, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        bus_stations = list(reader)

    paginator = Paginator(bus_stations, 10)  # Разделить список на страницы по 10 объектов
    current_page = request.GET.get('page', 1)
    page = paginator.get_page(current_page)

    context = {'bus_stations': page, 'page': page}

    return render(request, 'stations/index.html', context)
