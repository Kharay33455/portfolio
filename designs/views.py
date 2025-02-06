from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def project(request, proj_id):
    try:
        page = PageData.objects.get(project = proj_id)
        images = Image.objects.filter(page = page)
    except PageData.DoesNotExist:
        return HttpResponse('Does not exist')
    context = {'page' : page, 'images' : images}
    return render(request, f'designs/{page.project}-{page.page}.html', context)