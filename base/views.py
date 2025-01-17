from django.shortcuts import render
from .models import *

# Create your views here.


def base(request):
    cand = Candidate.objects.first()
    projs = Project.objects.all()
    skills = Skill.objects.all().order_by('experience')
    print(skills)
    context = {'cand': cand, 'projs':projs, 'skills':skills}
    return render(request, 'base/home.html', context)


def message(request):
    if request.method == 'POST':
        title = request.POST['title']
        message = request.POST['message']
        email = request.POST['email']
        new_message = Message.objects.create(title = title, message = message, email =  email)
        new_message.save()
        cand = Candidate.objects.first()
        msg = 'Your message was sent successfully. I would get back to you ASAP'
        context = {'msg': msg, 'cand':cand}
        return render(request, 'base/message.html', context)
    else:

        cand = Candidate.objects.first()
        context ={'cand': cand}
        return render(request, 'base/message.html', context)
    
def booking(request):
    if request.method == 'POST':
        title = request.POST['title']
        details = request.POST['details']
        email = request.POST['email']
        new_booking = Booking.objects.create(title = title, details = details, email = email)
        new_booking.save()
        cand = Candidate.objects.first()
        msg = 'Your request has been booked, I will get back to you asap.'
        context = {'msg': msg, 'cand':cand}
        return render(request, 'base/booking.html', context)
    else:

        cand = Candidate.objects.first()
        context ={'cand': cand}
        return render(request, 'base/booking.html', context)