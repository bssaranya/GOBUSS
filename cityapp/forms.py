from django import forms

from cityapp.models import Display, Stations


class DisplayCreationForm(forms.ModelForm):
    class Meta:
        model = Display
        fields = '__all__'
        exclude = ['timeinterval']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['stations'].queryset = Stations.objects.none()

        if 'cities' in self.data:
            try:
                city_id = int(self.data.get('cities'))
                self.fields['stations'].queryset = Stations.objects.filter(city_id=city_id).order_by('stationname')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['stations'].queryset = self.instance.city.stations_set.order_by('stationname')