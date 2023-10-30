from django.shortcuts import render
from django.conf import settings
import requests

def index(request):
    return render(request, "auth/status.html")


@ms_identity_web.login_required
def token_details(request):
    return render(request, 'auth/token.html')