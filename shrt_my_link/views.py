from django.shortcuts import render
from django.http import Http404
from shrt_my_link.models import Link


def index(request):
    links = Link.objects.all()
    return render(request, 'shrt_my_link/index.html', {
        'links': links,
    })
