from rest_framework import serializers
from .models import UserData

class Dataserializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ['id','name','roll','city']

        