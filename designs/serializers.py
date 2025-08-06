from rest_framework.serializers import ModelSerializer
from .models import *

class PageDataSerializer(ModelSerializer):
    class Meta:
        model = PageData
        exclude =['id']