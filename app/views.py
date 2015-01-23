from django.shortcuts import render
from app.models import events, discography as albums


def home(request):
    """
    View for home page. Events and discography models passed to template.
    :param request:
    :return:
    """
    return render(request, 'home.html', {'events': events, 'discography': albums})


def members(request):
    """
    View for member bios. All data is stored statically in template.
    :param request:
    :return:
    """
    return render(request, 'members.html')


def discography(request):
    """
    View for discography page. Loads album data from fake model and passes it to the template.
    :param request:
    :return:
    """
    return render(request, 'discography.html', {'discography': albums})


def tour(request):
    """
    View for tour events. Events are passed to the template.
    :param request:
    :return:
    """
    return render(request, 'tour.html', {'events': events})

