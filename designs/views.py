from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from base.models import Candidate

# Create your views here.

def project(request, proj_id):
    try:
        page = PageData.objects.get(project = proj_id)
        images = Image.objects.filter(page = page)
    except PageData.DoesNotExist:
        return HttpResponse('Does not exist')
    context = {'page' : page, 'images' : images}
    return render(request, f'designs/{page.project}-{page.page}.html', context)

def designs(request):
    pages = PageData.objects.all().order_by('?')
    page_list = []
    i = 1
    for _ in pages:
        page_list.append({'id' : i , 'page' : _})
        i += 1
    cand = Candidate.objects.first()
    context = { "pages" : page_list, 'cand' : cand}
    return render(request, 'designs/design.html', context)