"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from userapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('data/',views.Studentlist.as_view()),
    #path('data/',views.StudentCreate.as_view()),
    #path('data/<int:pk>/',views.StudentRetrive.as_view()),
    #path('data/<int:pk>/',views.StudentUpdate.as_view()),
    #path('data/<int:pk>/',views.StudentDestroy.as_view()),
    #doubal function work with each other
    path('data/',views.Studentlistcreate.as_view()),
    #path('data/<int:pk>/',views.Studentretriveupdate.as_view()),
    #path('data/<int:pk>/',views.Studentretrivedestroy.as_view()),
    path('data/<int:pk>/',views.StudentRUD.as_view()),
]
