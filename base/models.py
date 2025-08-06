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
    proj_type = models.CharField(max_length = 20)
    phone_view = models.FileField(null=True, blank=True)
    laptop_view = models.FileField(null=True, blank=True)
    tablet_view = models.ImageField(null=True, blank=True)
    details = models.CharField(max_length = 250)
    # why was it built
    objective = models.TextField(null=True, blank=True)
    # role on projects
    role = models.TextField(null=True, blank=True)
    # outcome after project
    outcome = models.TextField(null=True, blank=True)
    # what you leared on project
    takeaways = models.TextField(null=True, blank=True)
    url = models.URLField()
    github = models.URLField()

    def __str__(self):
        return f'Project {self.name}'
    
class ChallengeAndSolution(models.Model):
    challenge = models.TextField()
    solution = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f'Challenge and solution for {self.project.name}'
    
class TechnologyUsed(models.Model):
    name = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} used for {self.project.name}'

class KeyFeature(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} implementation for {self.project}'
    
class Skill(models.Model):
    name = models.CharField(max_length =40)
    candidate = models.ForeignKey(Candidate, on_delete = models.CASCADE)
    experience = models.IntegerField()

    def __str__(self):
        return self.name
    
class Message(models.Model):
    title = models.CharField(max_length = 20)
    message = models.TextField()
    email = models.EmailField()
    sender = models.CharField(max_length = 100)

    def __str__(self):
        return self.title
    
class Booking(models.Model):
    title = models.CharField(max_length = 20)
    details = models.CharField(max_length = 200)
    email = models.EmailField()

    def __str__(self):
        return self.title

