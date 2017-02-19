from django.shortcuts import render
from django.shortcuts import redirect
from django.http import Http404
from shrt_my_link.models import Link
from shrt_my_link.forms import LinkForm
import random
import string


def index(request):
    if request.method == "POST":
        form = LinkForm(request.POST)
        if form.is_valid():
            link = form.save(commit=False)
            s = string.lowercase+string.digits
            link.token = ''.join(random.sample(s,5))
            link.save()
            return redirect('index')
    else:
        form = LinkForm()
    links = Link.objects.all()
    return render(request, 'shrt_my_link/index.html', {
        'form': form,
        'links': links,
    })
