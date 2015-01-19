from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def members(request):
    return render(request, 'members.html')

def discography(request):
    return render(request, 'discography.html')

def tour(request):
    return render(request, 'tour.html')

