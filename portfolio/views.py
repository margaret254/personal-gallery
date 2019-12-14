# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt

# Create your views here.
def welcome(request):
    return render(request, 'Welcome.html')
    
def photo_category(request):
    date = dt.date.today()
    return HttpResponse

def convert_dates(dates):
    # function that gets the weekday number for the date
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wedneasday','Thursday','Friday','Saturday','Sunday']

    # Returning the actual day of the week
    day = days[day_number]
    return day
    
