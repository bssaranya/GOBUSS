from django.db import models

# Create your models here.

class City(models.Model):
    cityname = models.CharField(max_length=40)

    def __str__(self):
        return self.cityname


class Stations(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    stationname = models.CharField(max_length=40)

    def __str__(self):
        return self.stationname

class Bus(models.Model):
    time = models.CharField(max_length=150)
    bus = models.CharField(max_length=150)
    station = models.ForeignKey(Stations,on_delete=models.CASCADE)
    day = models.CharField(max_length=150,default="monday")
    timeinterval = models.CharField(max_length=25, default='8:00')

    def __str__(self):
        return f"{self.timeinterval}-{self.station}"

class Display(models.Model):

    cities = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)
    stations = models.ForeignKey(Stations, on_delete=models.SET_NULL, blank=True, null=True)
    day = models.CharField(max_length=125)
    time = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.cities}-{self.stations}"