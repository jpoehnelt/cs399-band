from django.shortcuts import render
from app.models import events, discography as albums


def home(request):
    return render(request, 'home.html', {'events': events, 'discography': albums})


def members(request):
    return render(request, 'members.html')


def discography(request):
    return render(request, 'discography.html', {'discography': albums})


def tour(request):
    return render(request, 'tour.html', {'events': events})

