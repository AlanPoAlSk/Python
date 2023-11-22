from django.shortcuts import render 
from .models import User

def index(request):
    context = {
        'all_users' :
            User.objects.all()
    }
    return render(request, 'index.html', context)

def create(request):

    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email_address = request.POST.get('email_address')
    age = request.POST.get('age')
    
    new_user = User.objects.create(
        first_name=first_name,
        last_name=last_name,
        email_address=email_address,
        age=age
    )
    
    all_users = User.objects.all()
    
    context = {
        'new_user': new_user,
        'all_users': all_users
    }
    return render (request,'index.html', context)
