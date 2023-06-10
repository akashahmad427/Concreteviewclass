from django.shortcuts import render
from .models import UserData
from .serializer import Dataserializer
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView


# Create your views here.

'''class Studentlist(ListAPIView):
    queryset = UserData.objects.all()
    serializer_class = Dataserializer

class StudentCreate(CreateAPIView):
    queryset = UserData.objects.all()
    serializer_class = Dataserializer


class StudentRetrive(RetrieveAPIView):
    queryset = UserData.objects.all()
    serializer_class = Dataserializer


class StudentUpdate(UpdateAPIView):
    queryset = UserData.objects.all()
    serializer_class = Dataserializer

class StudentDestroy(DestroyAPIView):
    queryset = UserData.objects.all()
    serializer_class = Dataserializer'''

#Both list create work with each other write combine method

class Studentlistcreate(ListCreateAPIView):
    queryset = UserData.objects.all()
    serializer_class = Dataserializer


'''class Studentretriveupdate(RetrieveUpdateAPIView):
    queryset = UserData.objects.all()
    serializer_class = Dataserializer


class Studentretrivedestroy(RetrieveDestroyAPIView):
    queryset = UserData.objects.all()
    serializer_class = Dataserializer
'''
#three function in one line of code.
class StudentRUD(RetrieveUpdateDestroyAPIView):
    queryset = UserData.objects.all()
    serializer_class = Dataserializer