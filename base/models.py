from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Candidate(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    picture = models.FileField(null = True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Project(models.Model):
    name = models.CharField(max_length = 40)
    candidate = models.ForeignKey(Candidate, on_delete = models.CASCADE)
    type = models.CharField(max_length = 20)
    phone_view = models.FileField(null=True, blank=True)
    laptop_view = models.FileField(null=True, blank=True)
    details = models.CharField(max_length = 300)
    tools = models.CharField(max_length = 200, null = True, blank = True)
    url = models.URLField()
    github = models.URLField()

    def __str__(self):
        return f'Project {self.name}'
    
class Skill(models.Model):
    name = models.CharField(max_length =40)
    candidate = models.ForeignKey(Candidate, on_delete = models.CASCADE)
    experience = models.IntegerField()

    def __str__(self):
        return self.name
    
class Message(models.Model):
    title = models.CharField(max_length = 20)
    message = models.CharField(max_length = 200)
    email = models.EmailField()

    def __str__(self):
        return self.title
    
class Booking(models.Model):
    title = models.CharField(max_length = 20)
    details = models.CharField(max_length = 200)
    email = models.EmailField()

    def __str__(self):
        return self.title

