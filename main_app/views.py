import re
from django.contrib.auth.models import User
from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

from main_app.models import EnterInfo
from main_app.serializers import UserInfo
from rest_framework .decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import permission_required


@permission_required('UserInfo.home',login_url='/login/')
def home(request,username):
    return render(request, 'home.html',{'user':username})

@csrf_exempt
@api_view(['POST','GET'])
def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    elif request.method=='POST':
        data=request.POST
        try:
            dbase= EnterInfo.objects.get(username=data.get('username'), password1=data.get('password'))
        except Exception as e:
            return render(request,'login.html', {'error':"Username or Password doesn't exist!"})
        else:
            return redirect(f'/{str(data.get("username"))}/home/')



@csrf_exempt
@api_view(['POST','GET'])
def signup(request):
    if request.method=='GET':
        return render(request,'signup.html')
    elif request.method=='POST':
        
        serializer=UserInfo(data=request.POST)
        postData=request.POST

        error=serializer.validate_password(postData.get('password1'),postData.get('password2'))
        if error:
            return render(request,'signup.html',{'error':error})
        serializer.is_valid(raise_exception=True)
        
        serializer.save()
    

        return redirect('/login/')
        
# @permission_required('UserInfo.home',login_url='/login/')
def home(request,username):
    return render(request, 'home.html',{'user':username})
  

@api_view(['GET'])    
def about(request):
    return render(request, 'about.html')
        
@permission_required('UserInfo.home',login_url='/login/')
   
def myMeds(request, username):
    return render(request, 'myMeds.html',{'user':username})
    # return render(request, 'myMeds.html')

@api_view(['GET'])    
def stats(request, username):
    return render(request, 'stats.html',{'user':username})
    # return render(request, 'stats.html')

@api_view(['GET'])        
def profile(request, username):
    return render(request, 'profile.html',{'user':username})
    # return render(request, 'profile.html')

def error(request):
    return HttpResponse('Feature coming Soon!! Report the admin and hold tight!')