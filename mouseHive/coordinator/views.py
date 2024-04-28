from django.shortcuts import render
from .models import MouseCoordinate


def show_coordinates(request):

    # latest_coordinates = MouseCoordinate.objects.last()
    #
    # context = {
    #     'latest_coordinates': latest_coordinates
    # }
    #
    # return render(request, 'coordinator/home-page.html', context=context)
    return render(request, 'coordinator/home-page.html')
