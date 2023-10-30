from django.shortcuts import render
from django.conf import settings
import requests

def index(request):
    return render(request, "auth/status.html")
