from rest_framework.serializers import ModelSerializer
from .models import *

class SkillSerializer(ModelSerializer):
    class Meta:
        model = Skill
        exclude = ['id', 'candidate']

class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        exclude = ['id', 'candidate']

class ChallengeAndSolutionSerializer(ModelSerializer):
    class Meta:
        model = ChallengeAndSolution
        exclude = ['id', 'project']

class KeyFeatureSerializer(ModelSerializer):
    class Meta:
        model = KeyFeature
        exclude = ['id', 'project']
class TechnologyUsedSerializer(ModelSerializer):
    class Meta:
        model = TechnologyUsed
        exclude = ['id', 'project']
