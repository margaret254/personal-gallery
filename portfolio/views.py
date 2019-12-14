# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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

