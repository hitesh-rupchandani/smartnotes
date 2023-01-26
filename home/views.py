from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today':datetime.today()}

class Authorized(LoginRequiredMixin, TemplateView):
    template_name =  'home/authorized.html'
    login_url = 'admin/'

# def home(request):
#     """This is home function"""
#     return render(
#         request=request, 
#         template_name= 'home/welcome.html', 
#         context= {'today':datetime.today()}
#     )

# @login_required(login_url='admin/')
# def authorized(request):
#     """This is restricted page. User have to login into system """
#     return render(
#         request, 
#         'home/authorized.html',
#         {}
#     )