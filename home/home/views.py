from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from django.shortcuts import render
from django.conf import settings
import requests

ms_identity_web = settings.MS_IDENTITY_WEB

def index(request):
    print('Authenticated?',request.identity_context_data.authenticated)
    
    print(request.identity_context_data._id_token_claims)

    print(request.identity_context_data)
    
    
    user_details = None
    if request.identity_context_data.authenticated:
        user_email = request.identity_context_data._id_token_claims.get('preferred_username', None)
        profile_name = request.identity_context_data._id_token_claims.get('name', None)

        if user_email:
            user, created = User.objects.get_or_create(email=user_email)

            if created:
                user.username = user_email  
                user.first_name = profile_name
                user.save()
            
        found_user = User.objects.get(email=user_email)

        if(found_user):
            user_details = {
                'email': found_user.email,
                'first_name': found_user.first_name,
            }
        
    return render(request, "auth/status.html",{'user_details':user_details})

@ms_identity_web.login_required
def token_details(request):
    return render(request, 'auth/token.html')