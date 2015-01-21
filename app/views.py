from django.shortcuts import render
from app.models import members as band_members, events


def home(request):
    return render(request, 'home.html', {'members': band_members, 'events': events})


def members(request):
    return render(request, 'members.html', {'members': band_members})


def discography(request):
    return render(request, 'discography.html')


def tour(request):
    return render(request, 'tour.html', {'events': events})

