from django.shortcuts import render
from .models import *
from designs.models import *
from designs.serializers import *
import os, json
from dotenv import load_dotenv
load_dotenv()
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
# Create your views here.


def base(request):
    cand = Candidate.objects.first()
    projs = Project.objects.all().order_by('?')
    skills = Skill.objects.all().order_by('?')
    context = {'cand': cand, 'projs':projs, 'skills':skills}
    return render(request, 'base/home.html', context)

@api_view(['POST'])
def message(request):
    # extract data
    body = request.POST
    try:
        title = body['title']
        message = body['message']
        email = body['email']
        sender = body['sender']
    except Exception as e:
        return Response({"err":"Invalid message data. Please fill all fields."},status = 400)
    
    # check for empty strings
    for item, value in body.items():
        if value.strip() == "":
            return Response({"err":"Invalid message data. Please fill all fields."},status = 400)
    
    # check for duplicates
    try:
        old_message = Message.objects.get(title = title, message = message, email =  email, sender = sender)
        return Response({"err":"Duplicate Message"},status = 400)
    except Message.DoesNotExist:
        pass
    
    new_message = Message.objects.create(title = title, message = message, email =  email, sender = sender)
    msg = 'Your message was sent successfully. I would get back to you as soon as possible'
    context = {'msg': msg}
    return Response(context, status = 200)

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
    
def web3(request):
    return render(request, 'base/web3.html', {})

@api_view(['GET'])
def fetch_data(request):
    # fetch and serialize skills
    skills = SkillSerializer(Skill.objects.all().order_by("-experience"), many = True).data

    # fetch and serialize projects
    project_list = []
    projects = Project.objects.all()
    for proj in projects:
        project_serialized = ProjectSerializer(proj).data
        project_serialized['challenges'] = ChallengeAndSolutionSerializer(ChallengeAndSolution.objects.filter(project = proj), many = True).data
        project_serialized['tech_used'] = TechnologyUsedSerializer(TechnologyUsed.objects.filter(project = proj), many = True).data
        project_serialized['key_features'] = KeyFeatureSerializer(KeyFeature.objects.filter(project = proj), many = True).data
        project_list.append(project_serialized)
    echos = PageDataSerializer(PageData.objects.all(), many = True).data
    context = {"skills":skills, "projects":project_list, "echos":echos}
    return Response(context, status = 200)
