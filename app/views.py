from django.shortcuts import render

# Create your views here.
from app.forms import *
from app.models import *
from django.http import HttpResponse


def insert_topic(request):
    TFO=TopicForm()
    d={'TFO':TFO}

    if request.method=='POST':
        TDFO=TopicForm(request.POST)
        if TDFO.is_valid():
            TDFO.save()
            return HttpResponse('insertion successfully')
    return render(request,'insert_topic.html',d)



def insert_webpage(request):
    WPO=WebpageForm()
    d={'WPO':WPO}

    if request.method=='POST':
        WDFO=WebpageForm(request.POST)
        if WDFO.is_valid():
            WDFO.save()
            return HttpResponse('insertion  is successfully')
    return render(request,'insert_webpage.html',d)




def insert_accessrecord(request):
    APO=AccessForm()
    d={'APO':APO}

    if request.method=='POST':
        ADFO=AccessForm(request.POST)
        if ADFO.is_valid():
            ADFO.save()
            return HttpResponse('insertion  is successfully')
    return render(request,'insert_accessrecord.html',d)











