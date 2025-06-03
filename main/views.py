from django.shortcuts import render
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def home(request):
   return render(request,'firstpage.html')
def mylogin_view(request):
   return render(request, 'main/login.html')
   
@csrf_exempt
@api_view(["POST"])
def myregister_view(request):
   return render(request, 'main/register.html')
