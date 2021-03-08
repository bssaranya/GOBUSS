from django.urls import path

from . import views

urlpatterns = [
    path('add/', views.display_create_view, name='display_add'),
    path('<int:pk>/', views.display_update_view, name='display_change'),

    path('ajax/load-stations/', views.load_stations, name='ajax_load_stations'),  # AJAX
]