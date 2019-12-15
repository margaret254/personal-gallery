

from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

# displaying different photo categories in cards
def photo_category(request):
    date = dt.date.today()
    return render(request, 'all-folios/category.html', {"date": date,})

def travel(request):
    date = dt.date.today()
    return render(request, 'all-folios/travel.html', {"date": date,})

def school(request):
    date = dt.date.today()
    return render(request, 'all-folios/school.html', {"date": date,})

def party(request):
    date = dt.date.today()
    return render(request, 'all-folios/party.html', {"date": date,})

def nature(request):
    date = dt.date.today()
    return render(request, 'all-folios/nature.html', {"date": date,})

def hiking(request):
    date = dt.date.today()
    return render(request, 'all-folios/hiking.html', {"date": date,})

def family(request):
    date = dt.date.today()
    return render(request, 'all-folios/family.html', {"date": date,})



