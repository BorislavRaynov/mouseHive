from django.urls import path
from mouseHive.coordinator.views import show_coordinates


urlpatterns = [
    path('', show_coordinates, name='home-page'),
]
