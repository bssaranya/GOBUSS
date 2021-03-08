
from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import DisplayCreationForm
from .models import Stations, Display, Bus


def display_create_view(request):
    form = DisplayCreationForm()
    if request.method == 'POST':
        form = DisplayCreationForm(request.POST)
        if form.is_valid():
            viewstations = form.cleaned_data['stations']
            viewtime = form.cleaned_data['time']
            viewday = form.cleaned_data['day']
            print(viewstations)

            bus = Bus()
            if Bus.objects.filter(station=viewstations).exists():
                data=Bus.objects.filter(station=viewstations) & Bus.objects.filter(time=viewtime) & Bus.objects.filter(day=viewday)



                return render(request,'cityapp/result.html',{'data':data})


            form.save()
            return redirect('display_add')
    return render(request, 'cityapp/home.html', {'form': form})


def display_update_view(request, pk):
    display = get_object_or_404(Display, pk=pk)
    form = DisplayCreationForm(instance=display)
    if request.method == 'POST':
        form = DisplayCreationForm(request.POST, instance=display)
        if form.is_valid():
            form.save()
            return redirect('display_change', pk=pk)
    return render(request, 'cityapp/home.html', {'form': form})


# AJAX
def load_stations(request):
    city_id = request.GET.get('city_id')
    stations = Stations.objects.filter(city_id=city_id).all()
    # return render(request, 'cityapp/city_dropdown_list_options.html', {'stations': stations})
    return JsonResponse(list(stations.values('id', 'stationname')), safe=False)