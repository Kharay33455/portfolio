from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Candidate)
admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Message)
admin.site.register(Booking)
admin.site.register(KeyFeature)
admin.site.register(ChallengeAndSolution)
admin.site.register(TechnologyUsed)