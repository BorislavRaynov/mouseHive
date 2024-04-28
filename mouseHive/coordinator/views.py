from django.shortcuts import render


def show_coordinates(request):
    return render(request, 'coordinator/home-page.html')
