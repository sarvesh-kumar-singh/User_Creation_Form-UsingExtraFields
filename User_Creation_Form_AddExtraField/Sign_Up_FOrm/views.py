from django.shortcuts import render
from .form import Sign_Up_Form 

def Signup(request):
    if request.method == "POST":
        fm=Sign_Up_Form(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm=Sign_Up_Form()
    return render(request,'signup/signup.html',{'form':fm})

