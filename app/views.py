from django.shortcuts import render

# Create your views here.
from app.forms import *

from django.http import HttpResponse

from app.models import *


def register(request):

    form = userform()


    if request.method  == 'POST':

        form_data = userform(request.POST)
        if form_data.is_valid():
            name = form_data.cleaned_data['sname']
            age = form_data.cleaned_data['age']
            user.objects.create(name = name,age=age)
            return HttpResponse("data is inserted successfully")

    return render(request,'register.html',{'form':form})



def userModelView(request):
    form  = usermodelform()

    if request.method == 'POST':

        form_data = usermodelform(request.POST)

        if form_data.is_valid():
            form_data.save()
    return render(request,'regisetrmodel.html',{'form':form})