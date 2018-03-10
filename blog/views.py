# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def helloWorld(request):
    return HttpResponse('<html><body><h2>Hello World.<h2></body></html>')