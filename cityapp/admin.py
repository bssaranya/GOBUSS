from django.contrib import admin
from .models import Display
from .models import City
from .models import Stations
from .models import Bus
# Register your models here.

admin.site.register(Display)
admin.site.register(Stations)
admin.site.register(City)
admin.site.register(Bus)