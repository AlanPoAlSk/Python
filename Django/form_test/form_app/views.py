from django.shortcuts import render,redirect

def index(request):
    return render (request, 'index.html')

def create_user(request):
    # print('Got Post Info...........')
    name_from_form = request.POST['name']
    email_from_form = request.POST['email']
    age_from_form = request.POST['age']
    
    context = {
        'name_on_template' : name_from_form,
        'email_on_template' : email_from_form,
        'age_on_template' : age_from_form
    }
    return redirect('/success')

def success(request):
    return render(request, 'success.html' )
