from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import PersonalInformation
from .form import PersonalDataForm

# Create your views here.

def first(request):
    return HttpResponse("Hello World")

def Home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def AddDetails(request):
    form = PersonalDataForm()
    if request.method == 'POST':
        form = PersonalDataForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    template = loader.get_template('formTemplate.html')
    return HttpResponse(template.render(context, request))

def ShowDetails(request):
    alldata = PersonalInformation.objects.all().values().order_by('-name')
    template = loader.get_template('showDetails.html')
    context = {
        'alldata': alldata,
    }
    return HttpResponse(template.render(context,request))
