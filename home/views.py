from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    """This is home function"""
    return render(
        request=request, 
        template_name='home/welcome.html', 
        context={'today':datetime.today()}
    )

@login_required(login_url='admin/')
def authorized(request):
    """This is restricted page. User have to login into system """
    return render(
        request, 
        'home/authorized.html',
        {}
    )