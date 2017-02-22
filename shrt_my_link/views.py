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
            return redirect('/')
    else:
        form = LinkForm()
    links = Link.objects.all()
    return render(request, 'shrt_my_link/index.html', {
        'form': form,
        'links': links,
    })

def counter(request,token_id):
    checkToken = Link.objects.filter(token = token_id)
    if checkToken.count() > 0:
        links = Link.objects.get(token = token_id)
        links.clickCount += 1
        links.save()
        return redirect(links.url)
    else:
        return render(request, 'shrt_my_link/404.html')
